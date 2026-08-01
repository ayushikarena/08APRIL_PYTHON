from rest_framework import serializers


class RestaurantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    cuisine = serializers.CharField(max_length=100)