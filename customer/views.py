from rest_framework import generics
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
from account.serializers import AccountWithoutCustomerSerializer
from account.models import Account
from decimal import Decimal


class CustomerRetrieveView(generics.RetrieveAPIView):
    """
    Retrieve a single customer with their total balance.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def retrieve(self, request, *args, **kwargs):
        customer = self.get_object()
        serializer = CustomerSerializer(customer)
        response_data = serializer.data
        accounts = Account.objects.filter(customer=customer.id)
        total_balance = 0
        for account in accounts:
            total_balance += Decimal(account.balance)
        response_data['accounts'] = AccountWithoutCustomerSerializer(accounts, many=True).data
        response_data['total_balance'] = total_balance
        return Response(response_data)


class CustomersListView(generics.ListAPIView):
    """
    List all customers.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
