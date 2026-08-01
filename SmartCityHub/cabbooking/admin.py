from django.contrib import admin
from .models import PickupLocation

@admin.register(PickupLocation)
class PickupLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'latitude', 'longitude', 'address', 'created_at')
    search_fields = ('user__username', 'address')
    list_filter = ('created_at',)
