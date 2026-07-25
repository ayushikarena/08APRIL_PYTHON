from rest_framework import serializers
from .models import Category, MenuItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class MenuItemSerializer(serializers.ModelSerializer):
    """
    Serializer for MenuItem model with price validation.
    """
    class Meta:
        model = MenuItem
        fields = '__all__'
    
    def validate_price(self, value):
        """
        Custom validation to ensure price is greater than 0.
        """
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value
