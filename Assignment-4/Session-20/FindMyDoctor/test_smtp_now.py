# test_smtp_now.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_project.settings')
django.setup()

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def test_send():
    recipient = "karenaayushi19@gmail.com"
    otp_code = "544327"
    
    subject = f"Your FoodieFinder Verification Code: {otp_code}"
    plain_message = f"Hello Ayushi,\n\nYour 6-digit OTP code for FoodieFinder is: {otp_code}\n\nValid for 3 minutes."
    
    context = {
        'user_name': 'Ayushi',
        'otp_code': otp_code,
        'purpose': 'account activation',
    }
    html_content = render_to_string('emails/otp_email.html', context)
    
    print(f"Backend: {settings.EMAIL_BACKEND}")
    print(f"Host: {settings.EMAIL_HOST}:{settings.EMAIL_PORT}")
    print(f"User: {settings.EMAIL_HOST_USER}")
    
    try:
        msg = EmailMultiAlternatives(subject, plain_message, settings.DEFAULT_FROM_EMAIL, [recipient])
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)
        print("SUCCESS: Live HTML email sent via SMTP successfully to recipient inbox!")
    except Exception as e:
        print(f"SMTP EXCEPTION: {type(e).__name__}: {str(e)}")

if __name__ == "__main__":
    test_send()
