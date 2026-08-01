import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FoodDeliveryAPI.settings')
django.setup()

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create a test user
user, created = User.objects.get_or_create(username='testuser', email='test@example.com')
if created:
    user.set_password('testpassword123')
    user.save()

# Generate or get token
token, _ = Token.objects.get_or_create(user=user)

print(f"USERNAME: {user.username}")
print(f"PASSWORD: testpassword123")
print(f"TOKEN: {token.key}")
