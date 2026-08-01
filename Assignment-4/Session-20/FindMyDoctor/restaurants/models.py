# models.py
# Database models for the Restaurant Finder application.

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


# UserProfile model extending standard Django User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True, default='')
    address = models.TextField(blank=True, default='')
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default_profile.png', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


# OTPVerification model for Forgot Password functionality
class OTPVerification(models.Model):
    email = models.EmailField()
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def is_valid(self):
        """
        Returns True if the OTP was generated within the last 3 minutes (180 seconds)
        and has not already been used.
        """
        if self.is_verified:
            return False
        
        # Calculate time difference in seconds
        now = timezone.now()
        time_difference = (now - self.created_at).total_seconds()
        
        # OTP is valid for 3 minutes (180 seconds)
        return time_difference <= 180

    def __str__(self):
        return f"OTP for {self.email} ({self.otp_code})"


# Restaurant model for Search and Directory
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    rating = models.FloatField(default=4.5)
    description = models.TextField(blank=True, default='')
    image_url = models.CharField(max_length=255, blank=True, default='https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=600&q=80')

    def __str__(self):
        return f"{self.name} - {self.cuisine} ({self.location})"
