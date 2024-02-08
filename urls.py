from django.contrib import admin
from django.urls import path, include
from .api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/accounts/', api_views.AccountListView.as_view(), name='account-list'),
    path('api/transactions/', api_views.TransactionListView.as_view(), name='transaction-list'),
    path('api/user-profile/', api_views.UserProfileView.as_view(), name='user-profile'),
    path('api/initiate-transaction/', api_views.TransactionInitiationView.as_view(), name='initiate-transaction'),
    path('api/wallet/', api_views.WalletManagementView.as_view(), name='wallet-management'),
    path('api/ethereum-transactions/', api_views.EthereumTransactionsView.as_view(), name='ethereum-transactions'),
    path('api/wallet-connector/', api_views.WalletConnectorView.as_view(), name='wallet-connector'),
]
