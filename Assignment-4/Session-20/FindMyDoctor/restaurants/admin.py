# admin.py
# Register models in Django Admin panel with basic custom list views, search fields, and filters.

from django.contrib import admin
from .models import UserProfile, OTPVerification, Restaurant


# UserProfile Admin registration
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')
    search_fields = ('user__username', 'user__email', 'phone', 'address')


# OTPVerification Admin registration
@admin.register(OTPVerification)
class OTPVerificationAdmin(admin.ModelAdmin):
    list_display = ('email', 'otp_code', 'created_at', 'is_verified')
    search_fields = ('email', 'otp_code')
    list_filter = ('is_verified', 'created_at')


# Restaurant Admin registration
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine', 'location', 'rating')
    search_fields = ('name', 'cuisine', 'location')
    list_filter = ('cuisine', 'location')
