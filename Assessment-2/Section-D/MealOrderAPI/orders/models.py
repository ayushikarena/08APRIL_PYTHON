from django.db import models

class Order(models.Model):
    """
    Order model representing a food delivery order.
    """
    customer_name = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order {self.id} by {self.customer_name}"
