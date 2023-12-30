from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(max_digits=12, decimal_places=2)
    customer = serializers.StringRelatedField()

    class Meta:
        model = Account
        fields = ['id', 'customer', 'balance']


class AccountWithoutCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'balance']


class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'customer', 'balance']
