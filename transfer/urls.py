from django.urls import path
from .views import TransferCreateView, TransferRetrieveView, TransfersListView

urlpatterns = [
    path('transfer/', TransferCreateView.as_view(), name='create_transfer'),
    path('transfer/<int:pk>/', TransferRetrieveView.as_view(), name='retrieve_transfer'),
    path('transfers/', TransfersListView.as_view(), name='list_transfers'),
]
