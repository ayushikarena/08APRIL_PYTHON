# urls.py
# Application URL pattern routing for restaurants app.

from django.urls import path
from . import views

urlpatterns = [
    # Public Pages
    path('', views.home, name='home'),
    
    # Authentication & OTP URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('otp-verify/', views.otp_verify_view, name='otp_verify'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
    
    # User Profile & Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    
    # Restaurant Search & Map Feature
    path('restaurants/', views.restaurant_search_view, name='restaurant_search'),
    path('map/', views.map_view, name='map'),
]
