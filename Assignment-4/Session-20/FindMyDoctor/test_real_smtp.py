# test_real_smtp.py
# Test script to send a real email using configured Gmail SMTP credentials.

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_project.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings
import random

def test_live_gmail_sending():
    recipient = "karenaaayushi19@gmail.com"
    otp_code = str(random.randint(100000, 999999))

    subject = f"Your FoodieFinder Verification Code: {otp_code}"
    message = (
        f"Hello Ayushi,\n\n"
        f"Your 6-digit verification OTP code for your FoodieFinder account is: {otp_code}\n\n"
        f"This verification code is valid for exactly 3 minutes.\n"
        f"If you did not request this code, please ignore this email.\n\n"
        f"Best regards,\n"
        f"FoodieFinder Security Team"
    )

    print(f"Connecting to {settings.EMAIL_HOST}:{settings.EMAIL_PORT} via {settings.EMAIL_HOST_USER}...")
    try:
        sent_count = send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient], fail_silently=False)
        print(f"SUCCESS: Real OTP email sent successfully to {recipient}! (Sent count: {sent_count})")
    except Exception as e:
        print(f"ERROR: Failed to send real email: {str(e)}")

if __name__ == "__main__":
    test_live_gmail_sending()
