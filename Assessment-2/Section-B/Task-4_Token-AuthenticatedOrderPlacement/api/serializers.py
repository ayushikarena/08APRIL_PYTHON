"""
serializers.py — Task 4: Token-Authenticated Order Placement
=============================================================
OrderSerializer:
  • Uses ModelSerializer for automatic field mapping.
  • 'user' field is read-only — it is set automatically from request.user
    inside the view (not accepted from client payload).
  • 'status' has a safe default ('pending') so clients don't need to send it.
  • 'created_at' is read-only (auto-set by the database).
"""

from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.

    Read-only fields:
        - id         : auto-generated primary key
        - user       : set automatically from request.user (not client input)
        - created_at : auto-set timestamp

    Writable fields (sent in POST body):
        - item       : name of the food item
        - quantity   : number of units (must be >= 1)
        - status     : order status (optional; defaults to 'pending')
    """

    # ✅ Show username string instead of just user ID for better readability
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model  = Order
        fields = ['id', 'user', 'item', 'quantity', 'status', 'created_at']

        # These fields are never written by the client
        read_only_fields = ['id', 'user', 'created_at']

    # ------------------------------------------------------------------
    # Custom validation
    # ------------------------------------------------------------------
    def validate_quantity(self, value):
        """Ensure quantity is at least 1."""
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1.")
        return value

    def validate_item(self, value):
        """Ensure item name is not blank."""
        if not value.strip():
            raise serializers.ValidationError("Item name cannot be blank.")
        return value.strip()
