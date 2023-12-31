import factory
from factory.django import DjangoModelFactory
from .models import Transfer
from account.factories import AccountFactory


class TransferFactory(DjangoModelFactory):
    class Meta:
        model = Transfer

    from_account = factory.SubFactory(AccountFactory)
    to_account = factory.SubFactory(AccountFactory)
    amount = 200
