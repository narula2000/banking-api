from rest_framework import serializers
from .models import Transfer
from account.serializers import AccountSerializer


class TransferSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    from_account = AccountSerializer(read_only=True)
    to_account = AccountSerializer(read_only=True)

    class Meta:
        model = Transfer
        fields = ['id', 'from_account', 'to_account', 'amount', 'timestamp']


class TransferCreateSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        model = Transfer
        fields = ['from_account', 'to_account', 'amount']
