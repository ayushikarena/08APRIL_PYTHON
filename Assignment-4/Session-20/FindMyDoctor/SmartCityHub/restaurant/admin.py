from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine', 'location', 'rating', 'created_at')
    search_fields = ('name', 'cuisine', 'location')
    list_filter = ('cuisine', 'rating')
