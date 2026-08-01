import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FoodDeliveryAPI.settings')
django.setup()

from foodapp.models import Category, MenuItem, Order
from django.contrib.auth.models import User

# Get the user
user = User.objects.get(username='testuser')

# Create Categories
cat_bev, _ = Category.objects.get_or_create(name='Beverages', description='Cold and hot drinks')
cat_main, _ = Category.objects.get_or_create(name='Main Course', description='Heavy meals for lunch or dinner')
cat_dessert, _ = Category.objects.get_or_create(name='Desserts', description='Sweet treats to finish your meal')

# Create Menu Items
item1, _ = MenuItem.objects.get_or_create(name='Coca Cola', price=2.50, category=cat_bev, is_available=True)
item2, _ = MenuItem.objects.get_or_create(name='Grilled Chicken', price=12.99, category=cat_main, is_available=True)
item3, _ = MenuItem.objects.get_or_create(name='Cheeseburger', price=8.50, category=cat_main, is_available=True)
item4, _ = MenuItem.objects.get_or_create(name='Chocolate Cake', price=4.50, category=cat_dessert, is_available=True)
item5, _ = MenuItem.objects.get_or_create(name='Iced Tea', price=3.00, category=cat_bev, is_available=True)

# Create Orders
Order.objects.get_or_create(customer=user, item=item2, quantity=2, status='pending')
Order.objects.get_or_create(customer=user, item=item4, quantity=1, status='delivered')

print("Database populated with sample data successfully!")
