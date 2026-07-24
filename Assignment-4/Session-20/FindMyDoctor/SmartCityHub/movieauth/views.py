from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import OTP
from django.core.mail import send_mail

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
            
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')
            
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Registration successful. Please login.")
        return redirect('login')
        
    return render(request, 'register.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Generate OTP
            otp_obj = OTP.generate_otp(user)
            # Send OTP email
            send_mail(
                'Your Login OTP',
                f'Your OTP for login is {otp_obj.otp}. It is valid for 3 minutes.',
                'noreply@smartcityhub.com',
                [user.email],
                fail_silently=False,
            )
            # We don't log them in fully yet, we store the user_id in session
            request.session['pre_otp_user_id'] = user.id
            messages.success(request, "OTP sent to your email.")
            return redirect('verify_otp')
        else:
            messages.error(request, "Invalid username or password.")
            
    return render(request, 'login.html')

def verify_otp(request):
    user_id = request.session.get('pre_otp_user_id')
    if not user_id:
        return redirect('login')
        
    if request.method == 'POST':
        otp_input = request.POST.get('otp')
        try:
            user = User.objects.get(id=user_id)
            otp_obj = OTP.objects.filter(user=user).latest('created_at')
            
            if otp_obj.otp == otp_input and otp_obj.is_valid():
                otp_obj.is_verified = True
                otp_obj.save()
                
                # Log the user in
                auth_login(request, user)
                del request.session['pre_otp_user_id']
                
                messages.success(request, "Login successful.")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid or expired OTP.")
        except (User.DoesNotExist, OTP.DoesNotExist):
            messages.error(request, "Error verifying OTP.")
            return redirect('login')
            
    return render(request, 'verify_otp.html')

def resend_otp(request):
    user_id = request.session.get('pre_otp_user_id')
    if not user_id:
        return redirect('login')
        
    try:
        user = User.objects.get(id=user_id)
        otp_obj = OTP.generate_otp(user)
        send_mail(
            'Your New Login OTP',
            f'Your new OTP for login is {otp_obj.otp}. It is valid for 3 minutes.',
            'noreply@smartcityhub.com',
            [user.email],
            fail_silently=False,
        )
        messages.success(request, "A new OTP has been sent to your email.")
    except User.DoesNotExist:
        messages.error(request, "User not found.")
        
    return redirect('verify_otp')

def user_logout(request):
    auth_logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
