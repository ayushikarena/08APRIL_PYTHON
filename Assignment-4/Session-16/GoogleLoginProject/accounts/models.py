from django.db import models
from django.utils import timezone


class OTP(models.Model):

    mobile = models.CharField(max_length=15)

    otp_code = models.CharField(max_length=6)

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def is_expired(self):

        time_difference = timezone.now() - self.created_at

        return time_difference.total_seconds() > 300