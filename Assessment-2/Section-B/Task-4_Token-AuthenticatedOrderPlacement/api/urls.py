"""
api/urls.py — Task 4: Token-Authenticated Order Placement
==========================================================
Routes:
    GET  /api/my-orders/  →  List the authenticated user's orders
    POST /api/my-orders/  →  Place a new order (authenticated)
"""

from django.urls import path
from .views import PlaceOrderAPIView

urlpatterns = [
    # ✅ Single endpoint supporting both GET (list) and POST (create)
    path('my-orders/', PlaceOrderAPIView.as_view(), name='my-orders'),
]
