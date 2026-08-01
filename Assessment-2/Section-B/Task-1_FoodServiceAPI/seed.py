import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Category

# Add sample data
categories = [
    {'name': 'Appetizers', 'description': 'Small dishes or drinks taken before a meal to stimulate the appetite.'},
    {'name': 'Main Course', 'description': 'The featured or primary dish in a meal consisting of several courses.'},
    {'name': 'Desserts', 'description': 'Sweet courses typically served at the end of a meal.'},
]

for cat in categories:
    Category.objects.get_or_create(name=cat['name'], defaults={'description': cat['description']})

print("Sample data added successfully!")
