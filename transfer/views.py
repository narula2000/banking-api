from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Transfer
from .serializers import TransferSerializer, TransferCreateSerializer
from account.models import Account
from decimal import Decimal


class TransferCreateView(generics.CreateAPIView):
    """
    Create a new transfer between two accounts.
    """
    # permission_classes = [IsAuthenticated]

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
