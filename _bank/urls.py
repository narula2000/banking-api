from django.urls import path
from .views import *

urlpatterns = [
    path('customer/<int:pk>/', CustomerRetrieveView.as_view(), name='customer_account'),
    path('customers/', CustomersListView.as_view(), name='list_customers'),
    path('account/', AccountCreateView.as_view(), name='create_account'),
    path('account/<int:pk>/', AccountRetrieveView.as_view(), name='retrieve_account'),
    path('account/<int:pk>/transfer_from/', AccountTransferFromRetrieveView.as_view(), name='retrieve_account_transfer_from'),
    path('account/<int:pk>/transfer_to/', AccountTransferToRetrieveView.as_view(), name='retrieve_account_transfer_to'),
    path('account/<int:pk>/transfers/', AccountTransfersRetrieveView.as_view(), name='retrieve_account_transfers'),
    path('accounts/', AccountsListView.as_view(), name='list_accounts'),
    path('transfer/', TransferCreateView.as_view(), name='create_transfer'),
    path('transfer/<int:pk>/', TransferRetrieveView.as_view(), name='retrieve_transfer'),
    path('transfers/', TransfersListView.as_view(), name='list_transfers'),
]
