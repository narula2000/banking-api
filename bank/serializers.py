from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Customer, Account, Transfer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class CutomerWithoutAccountsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user']


class AccountSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(max_digits=12, decimal_places=2)
    customer = CutomerWithoutAccountsSerializer(read_only=True)

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


class TransferSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    from_account = AccountSerializer(read_only=True)
    to_account = AccountSerializer(read_only=True)

    class Meta:
        model = Transfer
        fields = ['from_account', 'to_account', 'amount', 'timestamp']


class TransferCreateSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        model = Transfer
        fields = ['from_account', 'to_account', 'amount']


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    accounts = AccountSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user', 'accounts']
