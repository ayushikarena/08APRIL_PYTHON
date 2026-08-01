from rest_framework import serializers
from .models import Category, MenuItem, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Category name cannot be empty.")
        return value

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("MenuItem name cannot be empty.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("MenuItem price must be greater than 0.")
        return value

class OrderSerializer(serializers.ModelSerializer):
    # Customer will be automatically assigned from request.user, so we can make it read_only
    customer = serializers.ReadOnlyField(source='customer.username')

    class Meta:
        model = Order
        fields = '__all__'

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Order quantity must be greater than or equal to 1.")
        return value
