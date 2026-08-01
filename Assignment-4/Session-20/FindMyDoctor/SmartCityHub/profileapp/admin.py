from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'mobile', 'city', 'state')
    search_fields = ('user__username', 'full_name', 'mobile', 'email')
    list_filter = ('state', 'city')
