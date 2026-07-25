import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FoodDeliveryAPI.settings')
django.setup()

from api.models import Order

# Clear existing data
Order.objects.all().delete()

# Seed sample orders
orders = [
    {"customer_name": "Alice Smith",   "item": "Sushi Platter",      "quantity": 2, "status": "pending"},
    {"customer_name": "Bob Johnson",   "item": "Margherita Pizza",   "quantity": 1, "status": "confirmed"},
    {"customer_name": "Charlie Brown", "item": "Butter Chicken",     "quantity": 3, "status": "delivered"},
    {"customer_name": "Diana Prince",  "item": "Veggie Burger",      "quantity": 2, "status": "pending"},
    {"customer_name": "Ethan Hunt",    "item": "Pasta Carbonara",    "quantity": 1, "status": "confirmed"},
    {"customer_name": "Fiona Green",   "item": "Tandoori Chicken",   "quantity": 4, "status": "delivered"},
    {"customer_name": "George Miller", "item": "Dal Makhani",        "quantity": 2, "status": "pending"},
    {"customer_name": "Hannah White",  "item": "Caesar Salad",       "quantity": 1, "status": "confirmed"},
    {"customer_name": "Ivan Drago",    "item": "Chicken Biryani",    "quantity": 3, "status": "delivered"},
    {"customer_name": "Julia Roberts", "item": "Paneer Tikka",       "quantity": 2, "status": "pending"},
]

for order_data in orders:
    Order.objects.create(**order_data)

print(f"[OK] Successfully seeded {Order.objects.count()} orders!")
for o in Order.objects.all():
    print(f"  [{o.id}] {o.customer_name} - {o.item} x{o.quantity} ({o.status})")
