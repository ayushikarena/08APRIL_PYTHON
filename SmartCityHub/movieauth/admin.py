from django.contrib import admin
from .models import OTP

@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('user', 'otp', 'created_at', 'is_verified')
    search_fields = ('user__username', 'otp')
    list_filter = ('is_verified', 'created_at')
