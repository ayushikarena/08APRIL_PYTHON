"""
admin.py — Task 4: Token-Authenticated Order Placement
=======================================================
Registers the Order model with the Django admin site.
Admins can also manage auth tokens from /admin/authtoken/token/.
"""

from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Order model.

    Features:
        - Displays user, item, quantity, status, and created_at in the list.
        - Allows filtering by status.
        - Supports search by username and item name.
        - 'user' and 'created_at' are read-only (auto-managed).
    """

    # Columns shown in the list view
    list_display  = ('id', 'user', 'item', 'quantity', 'status', 'created_at')

    # Sidebar filters
    list_filter   = ('status',)

    # Search bar — searches user's username and item name
    search_fields = ('user__username', 'item')

    # Fields that cannot be edited directly in admin
    readonly_fields = ('user', 'created_at')

    # Order newest first in admin list
    ordering = ('-created_at',)
