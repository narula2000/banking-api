from factory import SubFactory
from factory.django import DjangoModelFactory

from customer.factories import CustomerFactory
from .models import Account


class AccountFactory(DjangoModelFactory):
    class Meta:
        model = Account

    customer = SubFactory(CustomerFactory)
    balance = 1000
