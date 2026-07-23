from django.contrib import admin
from .models import City, Restaurant, MenuItem, Cart, CartItem, Order, OrderItem

admin.site.register(City)
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
