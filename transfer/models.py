from django.db import models
from account.models import Account


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
