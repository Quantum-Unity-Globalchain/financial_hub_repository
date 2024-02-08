from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.AccountListView.as_view(), name='account-list'),
    path('transactions/', views.TransactionListView.as_view(), name='transaction-list'),
    path('user-profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('initiate-transaction/', views.TransactionInitiationView.as_view(), name='initiate-transaction'),
    path('wallet/', views.WalletManagementView.as_view(), name='wallet-management'),
    path('ethereum-transactions/', views.EthereumTransactionsView.as_view(), name='ethereum-transactions'),
    path('wallet-connector/', views.WalletConnectorView.as_view(), name='wallet-connector'),
]
