from django.urls import path
from .views import CustomerRetrieveView, CustomersListView

urlpatterns = [
    path('customer/<int:pk>/', CustomerRetrieveView.as_view(), name='customer_account'),
    path('customers/', CustomersListView.as_view(), name='list_customers'),
]
