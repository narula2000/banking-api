from django.db import models
from customer.models import Customer


class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
