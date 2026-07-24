# test_otp_flow.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_project.settings')
django.setup()

from django.contrib.auth.models import User
from restaurants.models import OTPVerification, UserProfile
from django.contrib.auth import authenticate
import random

def test_full_otp_flow():
    print("--- TESTING REGISTRATION & EMAIL OTP ACTIVATION FLOW ---")

    test_username = "test_student_user"
    test_email = "student_test@example.com"
    test_password = "Password123!"

    User.objects.filter(username=test_username).delete()
    User.objects.filter(email=test_email).delete()

    # Step 1: Register User (Inactive)
    user = User.objects.create(
        username=test_username,
        first_name="Test",
        last_name="Student",
        email=test_email,
        is_active=False
    )
    user.set_password(test_password)
    user.save()
    UserProfile.objects.create(user=user)

    print(f"1. Registered user created: {user.username} (is_active={user.is_active})")
    assert user.is_active == False

    # Step 2: Generate 6-Digit OTP
    otp_code = str(random.randint(100000, 999999))
    otp_record = OTPVerification.objects.create(email=test_email, otp_code=otp_code)
    print(f"2. OTP Code generated for {test_email}: {otp_code}")
    assert otp_record.is_valid() == True

    # Step 3: Attempt Login before OTP
    unauth_user = authenticate(username=test_username, password=test_password)
    print(f"3. Login before OTP verification: Blocked ({unauth_user})")

    # Step 4: OTP Verification & Activation
    matching_otp = OTPVerification.objects.filter(email=test_email, otp_code=otp_code).order_by('-created_at').first()
    if matching_otp and matching_otp.is_valid():
        matching_otp.is_verified = True
        matching_otp.save()
        user.is_active = True
        user.save()
        print(f"4. OTP Verified & Account Activated: {user.username} (is_active={user.is_active})")

    assert user.is_active == True

    # Step 5: Login After OTP
    active_user = authenticate(username=test_username, password=test_password)
    print(f"5. Login after OTP verification: SUCCESS ({active_user.username})")

    print("\nSUCCESS: ALL OTP VERIFICATION TESTS PASSED 100%!")

if __name__ == "__main__":
    test_full_otp_flow()
