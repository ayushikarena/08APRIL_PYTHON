from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegisterForm
import random
from django.shortcuts import render
from django.conf import settings
from twilio.rest import Client

from .models import OTP

def login_view(request):
    return render(request, "login.html")

@login_required
def home(request):
    return render(request, "home.html")

#=============================Task-2=================================



def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('success')

    else:

        form = RegisterForm()


    return render(
        request,
        'register.html',
        {
            'form': form
        }
    )

@login_required
def dashboard(request):

    return render(request,'dashboard.html')


#===================Task-4==================
def send_otp(request):

    message = ""

    if request.method == "POST":

        mobile = request.POST.get("mobile")


        # Generate 6 digit OTP
        otp = random.randint(100000,999999)


        # Save OTP in database
        OTP.objects.create(
            mobile=mobile,
            otp_code=str(otp)
        )


        # Send SMS
        client = Client(
            settings.TWILIO_ACCOUNT_SID,
            settings.TWILIO_AUTH_TOKEN
        )


        client.messages.create(
            body=f"Your OTP is {otp}",
            from_=settings.TWILIO_PHONE_NUMBER,
            to=mobile
        )


        message = "OTP sent successfully"


    return render(
        request,
        "send_otp.html",
        {
            "message": message
        }
    )


def verify_otp(request):

    message = ""

    if request.method == "POST":

        mobile = request.POST.get("mobile")

        entered_otp = request.POST.get("otp")


        try:

            otp_record = OTP.objects.filter(
                mobile=mobile
            ).last()


            if otp_record.is_expired():

                message = "OTP expired"


            elif otp_record.otp_code == entered_otp:

                message = "OTP verified successfully"


            else:

                message = "Invalid OTP"


        except OTP.DoesNotExist:

            message = "OTP not found"


    return render(
        request,
        "verify_otp.html",
        {
            "message": message
        }
    )