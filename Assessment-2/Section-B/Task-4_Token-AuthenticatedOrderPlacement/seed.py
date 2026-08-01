"""
seed.py — Task 4: Token-Authenticated Order Placement
======================================================
Creates two test users with known passwords and generates
DRF auth tokens for each. Run with:
    python seed.py
"""

import os
import django

# ── Bootstrap Django ──────────────────────────────────────────────────────
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FoodDeliveryAPI.settings')
django.setup()

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# ── Test user definitions ─────────────────────────────────────────────────
TEST_USERS = [
    {
        'username'  : 'alice',
        'password'  : 'alice@1234',
        'email'     : 'alice@fooddelivery.com',
        'first_name': 'Alice',
        'last_name' : 'Smith',
    },
    {
        'username'  : 'bob',
        'password'  : 'bob@1234',
        'email'     : 'bob@fooddelivery.com',
        'first_name': 'Bob',
        'last_name' : 'Jones',
    },
]

print("\n" + "="*55)
print("   Task 4 — Token-Authenticated Order Placement")
print("   Seeding test users & generating auth tokens")
print("="*55)

for user_data in TEST_USERS:
    username = user_data['username']

    # get_or_create avoids duplicates when re-running seed.py
    user, created = User.objects.get_or_create(
        username=username,
        defaults={
            'email'     : user_data['email'],
            'first_name': user_data['first_name'],
            'last_name' : user_data['last_name'],
        }
    )

    if created:
        user.set_password(user_data['password'])
        user.save()
        print(f"\n[CREATED] User   : {username}")
    else:
        print(f"\n[EXISTS]  User   : {username}")

    # Generate or retrieve the DRF token for this user
    token, token_created = Token.objects.get_or_create(user=user)
    action = "Generated" if token_created else "Existing "
    print(f"  [{action}] Token : {token.key}")
    print(f"   Password       : {user_data['password']}")

print("\n" + "="*55)
print("   Copy the tokens above into Postman headers:")
print("   Key   : Authorization")
print("   Value : Token <paste_token_here>")
print("="*55 + "\n")
