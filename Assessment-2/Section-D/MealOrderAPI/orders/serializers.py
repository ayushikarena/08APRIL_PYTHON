from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model to handle validation and data transformation.
    """
    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'item', 'quantity']

    def validate_quantity(self, value):
        """
        Custom validation to ensure the quantity is a positive integer greater than 0.
        """
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0.")
        return value
