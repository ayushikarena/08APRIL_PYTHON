from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('delivered', 'Delivered'),
    ]

    customer_name = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.customer_name} - {self.item} ({self.status})"
