from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def send_test_email(request):

    send_mail(
        subject="Test Email",
        message="Hello! This is a test email from Django.",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=["miranena1017@gmail.com"],
        fail_silently=False,
    )

    return HttpResponse("Email sent successfully!")