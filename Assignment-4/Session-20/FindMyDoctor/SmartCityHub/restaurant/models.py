from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='restaurants/', blank=True, null=True)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
