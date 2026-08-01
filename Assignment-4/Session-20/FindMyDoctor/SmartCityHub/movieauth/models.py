from django.db import models
from django.contrib.auth.models import User
import random
from django.utils import timezone
import datetime

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def is_valid(self):
        # OTP is valid for 3 minutes
        now = timezone.now()
        diff = now - self.created_at
        return diff.total_seconds() <= 180 and not self.is_verified

    @classmethod
    def generate_otp(cls, user):
        otp_val = str(random.randint(100000, 999999))
        otp_obj = cls.objects.create(user=user, otp=otp_val)
        return otp_obj
