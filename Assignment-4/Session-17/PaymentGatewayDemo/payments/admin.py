from django.contrib import admin
from .models import Booking, FoodOrder, Payment

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer_name', 'match_name', 'num_tickets', 'amount', 'status', 'created_at')
    list_filter = ('status', 'match_name', 'created_at')
    search_fields = ('customer_name', 'email', 'order_id', 'match_name')
    readonly_fields = ('order_id', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    list_per_page = 25

@admin.register(FoodOrder)
class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer_name', 'food_name', 'quantity', 'price_per_item', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'food_name', 'created_at')
    search_fields = ('customer_name', 'email', 'order_id', 'food_name', 'stripe_session_id')
    readonly_fields = ('order_id', 'stripe_session_id', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    list_per_page = 25

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer_name', 'gateway', 'amount', 'status', 'payment_mode', 'transaction_id', 'created_at')
    list_filter = ('status', 'gateway', 'payment_mode', 'created_at')
    search_fields = ('customer_name', 'email', 'order_id', 'transaction_id')
    readonly_fields = ('order_id', 'transaction_id', 'raw_response', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    list_per_page = 25
    date_hierarchy = 'created_at'

admin.site.site_header  = "Payment Gateway Demo Admin"
admin.site.site_title   = "Payment Gateway Admin"
admin.site.index_title  = "Welcome to Dashboard"
