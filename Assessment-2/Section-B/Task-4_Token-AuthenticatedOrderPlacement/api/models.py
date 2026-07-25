"""
models.py — Task 4: Token-Authenticated Order Placement
========================================================
Changes from Task 3:
  • Added a ForeignKey to Django's built-in User model so every Order is
    owned by a specific authenticated user.
  • 'customer_name' is now derived from the user; kept as a free-text field
    for backward compatibility but auto-populated in the view.
  • Added 'created_at' timestamp for better record keeping.
"""

from django.db import models
from django.contrib.auth.models import User   # ✅ Django's built-in User model


class Order(models.Model):
    """
    Represents a food delivery order placed by a registered user.

    Ownership:
        The 'user' ForeignKey ensures each order is tied to one authenticated
        user.  on_delete=CASCADE means if the user is deleted, all their
        orders are deleted too.

    Access control is enforced at the VIEW layer — users can only see/create
        their own orders (request.user).
    """

    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('confirmed', 'Confirmed'),
        ('delivered', 'Delivered'),
    ]

    # ✅ ForeignKey to User — links each order to an authenticated user
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',          # user.orders.all() → all orders by that user
        help_text="The authenticated user who placed this order."
    )

    # Order details
    item          = models.CharField(max_length=255, help_text="Name of the food item ordered.")
    quantity      = models.PositiveIntegerField(default=1, help_text="Number of units ordered.")
    status        = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        help_text="Current status of the order."
    )

    # Timestamp — auto-set on creation
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']    # newest orders appear first
        verbose_name        = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order #{self.pk} — {self.user.username} | {self.item} x{self.quantity} [{self.status}]"
