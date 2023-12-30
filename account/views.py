from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Account
from .serializers import AccountSerializer, AccountCreateSerializer
from transfer.models import Transfer
from transfer.serializers import TransferSerializer
from customer.serializers import CutomerWithoutAccountsSerializer


class AccountCreateView(generics.CreateAPIView):
    """
    Create a new account for a given customer.
    """
    # permission_classes = [IsAuthenticated]

    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer


class AccountRetrieveView(generics.RetrieveAPIView):
    """
    Retrieve a single account.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AccountSerializer(instance)
        response_data = serializer.data
        customer = instance.customer
        response_data['customer'] = CutomerWithoutAccountsSerializer(customer).data
        return Response(response_data)


class AccountsListView(generics.ListAPIView):
    """
    List all accounts.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = AccountSerializer(queryset, many=True)
        response_data = serializer.data
        for i in range(len(response_data)):
            customer = queryset[i].customer
            response_data[i]['customer'] = CutomerWithoutAccountsSerializer(customer).data
        return Response(response_data)


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
        response_data = serializer.data
        for i in range(len(response_data)):
            from_account = transfers[i].from_account
            to_account = transfers[i].to_account
            from_account_customer = CutomerWithoutAccountsSerializer(from_account.customer).data
            to_account_customer = CutomerWithoutAccountsSerializer(to_account.customer).data
            response_data[i]['from_account']['customer'] = from_account_customer
            response_data[i]['to_account']['customer'] = to_account_customer
        return Response(response_data)


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
        response_data = serializer.data
        for i in range(len(response_data)):
            from_account = transfers[i].from_account
            to_account = transfers[i].to_account
            from_account_customer = CutomerWithoutAccountsSerializer(from_account.customer).data
            to_account_customer = CutomerWithoutAccountsSerializer(to_account.customer).data
            response_data[i]['from_account']['customer'] = from_account_customer
            response_data[i]['to_account']['customer'] = to_account_customer
        return Response(response_data)


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
        response_data = serializer.data
        for i in range(len(response_data)):
            from_account = transfers[i].from_account
            to_account = transfers[i].to_account
            from_account_customer = CutomerWithoutAccountsSerializer(from_account.customer).data
            to_account_customer = CutomerWithoutAccountsSerializer(to_account.customer).data
            response_data[i]['from_account']['customer'] = from_account_customer
            response_data[i]['to_account']['customer'] = to_account_customer
        return Response(response_data)


