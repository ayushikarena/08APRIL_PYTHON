from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\d{10}$',
    message='Phone number must be exactly 10 digits.'
)

class InfluencerProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    display_name = models.CharField(max_length=100)

    bio = models.TextField()

    profile_pic = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True
    )

    phone_number = models.CharField(
        max_length=10,
        validators=[phone_validator]
    )

    def __str__(self):
        return self.display_name