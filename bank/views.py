from rest_framework import generics, status
from rest_framework.response import Response
from .models import Account, Transfer, Customer
from .serializers import AccountWithoutCustomerSerializer, CustomerSerializer, AccountSerializer, AccountCreateSerializer, TransferSerializer, TransferCreateSerializer
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
            total_balance += account.balance
        response_data['accounts'] = AccountWithoutCustomerSerializer(accounts, many=True).data
        response_data['total_balance'] = total_balance
        return Response(response_data)


class CustomersListView(generics.ListAPIView):
    """
    List all customers.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AccountCreateView(generics.CreateAPIView):
    """
    Create a new account for a given customer.
    """
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer


class AccountRetrieveView(generics.RetrieveAPIView):
    """
    Retrieve a single account.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountsListView(generics.ListAPIView):
    """
    List all accounts.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountTransfersRetrieveView(generics.RetrieveAPIView):
    """
    List all transfers for a given account.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def retrieve(self, request, *args, **kwargs):
        account = self.get_object()
        transfers = Transfer.objects.filter(from_account=account.id)
        transfers = transfers | Transfer.objects.filter(to_account=account.id)
        serializer = TransferSerializer(transfers, many=True)
        return Response(serializer.data)


class AccountTransferFromRetrieveView(generics.RetrieveAPIView):
    """
    List all transfers from a given account.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def retrieve(self, request, *args, **kwargs):
        account = self.get_object()
        transfers = Transfer.objects.filter(from_account=account.id)
        serializer = TransferSerializer(transfers, many=True)
        return Response(serializer.data)


class AccountTransferToRetrieveView(generics.RetrieveAPIView):
    """
    List all transfers to a given account.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def retrieve(self, request, *args, **kwargs):
        account = self.get_object()
        transfers = Transfer.objects.filter(to_account=account.id)
        serializer = TransferSerializer(transfers, many=True)
        return Response(serializer.data)


class TransferCreateView(generics.CreateAPIView):
    """
    Create a new transfer between two accounts.
    """
    queryset = Transfer.objects.all()
    serializer_class = TransferCreateSerializer

    def create(self, request, *args, **kwargs):
        transfer_data = request.data
        from_account = Account.objects.get(id=transfer_data['from_account'])
        to_account = Account.objects.get(id=transfer_data['to_account'])
        amount = Decimal(transfer_data['amount'])

        if from_account.balance < amount:
            return Response({'error': 'Insufficient balance.'},
                            status=status.HTTP_400_BAD_REQUEST)

        from_account.balance -= amount
        from_account.save()

        to_account.balance += amount
        to_account.save()

        return super().create(request, *args, **kwargs)


class TransferRetrieveView(generics.RetrieveAPIView):
    """
    List a single transfer.
    """
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer


class TransfersListView(generics.ListAPIView):
    """
    List all transfers.
    """
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
