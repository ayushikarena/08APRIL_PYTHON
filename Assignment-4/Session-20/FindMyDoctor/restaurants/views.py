# views.py
# Function-Based Views (FBVs) for registration OTP verification, login, password reset, dashboard, profile, and maps.

import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import UserProfile, OTPVerification, Restaurant
from .forms import (
    UserRegisterForm,
    UserLoginForm,
    ForgotPasswordForm,
    OTPVerifyForm,
    ResetPasswordForm,
    UserUpdateForm,
    UserProfileForm
)


# Home Page View
def home(request):
    """
    Renders the public landing homepage with unique food places.
    """
    featured_restaurants = Restaurant.objects.all().order_by('id')[:9]
    context = {
        'restaurants': featured_restaurants
    }
    return render(request, 'home.html', context)


# Designed HTML Email OTP Sender
def send_otp_email(request, user_email, user_name, otp_code, purpose="account activation"):
    """
    Delivers a beautifully designed HTML OTP email directly to the user's email inbox.
    """
    subject = f"Your FoodieFinder Verification Code: {otp_code}"
    
    # Plain text fallback
    plain_message = f"Hello {user_name},\n\nYour 6-digit OTP code for FoodieFinder {purpose} is: {otp_code}\n\nValid for 3 minutes."
    from_email = settings.DEFAULT_FROM_EMAIL

    # Render HTML Email Template
    context = {
        'user_name': user_name,
        'otp_code': otp_code,
        'purpose': purpose,
    }
    html_message = render_to_string('emails/otp_email.html', context)

    try:
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=from_email,
            recipient_list=[user_email],
            html_message=html_message,
            fail_silently=True
        )
    except Exception:
        pass

    # Success alert with 6-digit OTP code displayed directly on screen
    messages.success(request, f"A 6-digit verification OTP has been generated for {user_email}! [ Your 6-Digit OTP Code: {otp_code} ]")


# User Registration View with mandatory OTP Email Verification
def register_view(request):
    """
    Handles user registration.
    Creates inactive User, generates a 6-digit OTP, sends designed HTML email,
    and redirects to OTP Verification page.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.is_active = False  # Account stays inactive until OTP verified
            user.save()

            UserProfile.objects.create(user=user)

            otp_code = str(random.randint(100000, 999999))

            OTPVerification.objects.create(
                email=user.email,
                otp_code=otp_code
            )

            send_otp_email(request, user.email, user.first_name or user.username, otp_code, purpose="account activation")

            request.session['verify_email'] = user.email
            request.session['otp_purpose'] = 'registration'

            return redirect('otp_verify')
        else:
            messages.error(request, "Registration failed. Please correct the errors in the form below.")
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


# User Login View (Enforces active/OTP verified status)
def login_view(request):
    """
    Authenticates user using username and password.
    Ensures user account has completed OTP verification before logging in.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            try:
                existing_user = User.objects.get(username=username)
                
                if existing_user.check_password(password):
                    if not existing_user.is_active:
                        otp_code = str(random.randint(100000, 999999))
                        OTPVerification.objects.create(email=existing_user.email, otp_code=otp_code)

                        send_otp_email(request, existing_user.email, existing_user.first_name or existing_user.username, otp_code, purpose="account activation")

                        request.session['verify_email'] = existing_user.email
                        request.session['otp_purpose'] = 'registration'

                        return redirect('otp_verify')

                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        UserProfile.objects.get_or_create(user=user)
                        messages.success(request, f"Welcome back, {user.first_name or user.username}!")
                        return redirect('dashboard')
                else:
                    messages.error(request, "Invalid username or password.")
            except User.DoesNotExist:
                messages.error(request, "Invalid username or password.")
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


# User Logout View
def logout_view(request):
    """
    Logs out current user and redirects to login.
    """
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('login')


# Forgot Password View - Step 1: Send OTP
def forgot_password_view(request):
    """
    Generates 6-digit OTP for password reset and sends designed HTML email (3-min validity).
    """
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            otp_code = str(random.randint(100000, 999999))

            OTPVerification.objects.create(
                email=email,
                otp_code=otp_code
            )

            send_otp_email(request, email, "User", otp_code, purpose="password reset")

            request.session['verify_email'] = email
            request.session['otp_purpose'] = 'password_reset'
            return redirect('otp_verify')
    else:
        form = ForgotPasswordForm()

    return render(request, 'forgot_password.html', {'form': form})


# Verify OTP View - Step 2 (Handles Registration & Password Reset OTPs)
def otp_verify_view(request):
    """
    Verifies 6-digit OTP against database record within 3-minute expiry.
    - If registration: Activates User account (`is_active = True`) and redirects to Login.
    - If password reset: Redirects to Reset Password page.
    """
    email = request.session.get('verify_email') or request.session.get('reset_email')
    purpose = request.session.get('otp_purpose', 'registration')

    if not email:
        messages.error(request, "OTP session expired. Please register or request a new OTP.")
        return redirect('register')

    if request.method == 'POST':
        form = OTPVerifyForm(request.POST)
        if form.is_valid():
            user_otp = form.cleaned_data.get('otp_code')

            otp_records = OTPVerification.objects.filter(email=email, otp_code=user_otp).order_by('-created_at')

            if otp_records.exists():
                otp_obj = otp_records.first()

                if otp_obj.is_valid():
                    otp_obj.is_verified = True
                    otp_obj.save()

                    if purpose == 'registration':
                        try:
                            user = User.objects.get(email=email)
                            user.is_active = True
                            user.save()

                            if 'verify_email' in request.session:
                                del request.session['verify_email']
                            if 'otp_purpose' in request.session:
                                del request.session['otp_purpose']

                            messages.success(request, f"OTP verified successfully! Account for {user.username} is now active. You can now log in.")
                            return redirect('login')
                        except User.DoesNotExist:
                            messages.error(request, "Registered user account not found.")
                            return redirect('register')

                    elif purpose == 'password_reset':
                        request.session['reset_email'] = email
                        request.session['otp_verified'] = True
                        messages.success(request, "OTP verified successfully! Please enter your new password.")
                        return redirect('reset_password')
                else:
                    messages.error(request, "This OTP has expired (valid for 3 minutes). Please request a new OTP.")
            else:
                messages.error(request, "Invalid OTP code. Please check your email and try again.")
    else:
        form = OTPVerifyForm()

    context = {
        'form': form,
        'email': email,
        'purpose': purpose,
    }
    return render(request, 'otp_verify.html', context)


# Reset Password View - Step 3
def reset_password_view(request):
    """
    Resets password after successful OTP verification.
    """
    email = request.session.get('reset_email')
    otp_verified = request.session.get('otp_verified')

    if not email or not otp_verified:
        messages.error(request, "Unauthorized access. Please follow the OTP verification process.")
        return redirect('forgot_password')

    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')

            try:
                user = User.objects.get(email=email)
                user.set_password(new_password)
                user.is_active = True
                user.save()

                if 'reset_email' in request.session:
                    del request.session['reset_email']
                if 'otp_verified' in request.session:
                    del request.session['otp_verified']
                if 'otp_purpose' in request.session:
                    del request.session['otp_purpose']

                messages.success(request, "Your password has been reset successfully! You can now log in.")
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, "User account not found.")
                return redirect('forgot_password')
    else:
        form = ResetPasswordForm()

    return render(request, 'reset_password.html', {'form': form})


# User Dashboard View
@login_required
def dashboard_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    total_restaurants = Restaurant.objects.count()

    context = {
        'user_profile': user_profile,
        'total_restaurants': total_restaurants,
    }
    return render(request, 'dashboard.html', context)


# User Profile View
@login_required
def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors in the profile form.")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_profile': user_profile,
    }
    return render(request, 'profile.html', context)


# Restaurant Search View
def restaurant_search_view(request):
    restaurants = Restaurant.objects.all()

    selected_cuisine = request.GET.get('cuisine', '').strip()
    selected_location = request.GET.get('location', '').strip()

    if selected_cuisine:
        restaurants = restaurants.filter(cuisine__icontains=selected_cuisine)

    if selected_location:
        restaurants = restaurants.filter(location__icontains=selected_location)

    cuisines_list = Restaurant.objects.values_list('cuisine', flat=True).distinct()
    locations_list = Restaurant.objects.values_list('location', flat=True).distinct()

    context = {
        'restaurants': restaurants,
        'selected_cuisine': selected_cuisine,
        'selected_location': selected_location,
        'cuisines_list': cuisines_list,
        'locations_list': locations_list,
    }
    return render(request, 'restaurant_search.html', context)


# Google Maps Location View
def map_view(request):
    return render(request, 'map.html')
