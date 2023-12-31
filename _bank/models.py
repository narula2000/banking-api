from django.db import models
from django.conf import settings


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.user.is_staff:
            raise ValueError("Staff users cannot be customers.")
        super().save(*args, **kwargs)


class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2)


class Transfer(models.Model):
    from_account = models.ForeignKey(
        Account,
        related_name='transfers_made',
        on_delete=models.CASCADE)
    to_account = models.ForeignKey(
        Account,
        related_name='transfers_received',
        on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
