from django.db import models
import uuid

def generate_order_id():
    # Helper function to generate unique order ID
    return 'ORD-' + str(uuid.uuid4()).replace('-', '').upper()[:12]

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    match_name = models.CharField(max_length=200)
    num_tickets = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_id = models.CharField(max_length=50, unique=True, default=generate_order_id)
    
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.match_name} - {self.order_id}"

class FoodOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    food_name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=8, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_id = models.CharField(max_length=50, unique=True, default=generate_order_id)
    stripe_session_id = models.CharField(max_length=200, blank=True, null=True)
    
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.food_name} x{self.quantity}"

class Payment(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    order_id = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=200, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    GATEWAY_CHOICES = [
        ('PAYTM', 'Paytm'),
        ('STRIPE', 'Stripe'),
        ('PAYPAL', 'PayPal'),
    ]
    gateway = models.CharField(max_length=20, choices=GATEWAY_CHOICES)
    
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    payment_mode = models.CharField(max_length=50, blank=True, null=True)
    raw_response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.gateway} | {self.order_id} | {self.status}"
