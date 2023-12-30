from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Customer
from account.serializers import AccountSerializer

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


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    accounts = AccountSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user', 'accounts']
