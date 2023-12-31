from django.db import models
from django.conf import settings


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # # This is a custom save method to prevent staff users from being customers.
    # def save(self, *args, **kwargs):
    #     if self.user.is_staff:
    #         raise ValueError("Staff users cannot be customers.")
    #     super().save(*args, **kwargs)
