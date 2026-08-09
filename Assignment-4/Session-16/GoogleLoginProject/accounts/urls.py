from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path("", views.login_view, name="login"),
    path("home/", views.home, name="home"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('register/', views.register, name='register'),
    path("send-otp/",send_otp,name="send_otp"),
    path("verify-otp/",verify_otp,name="verify_otp"),
]