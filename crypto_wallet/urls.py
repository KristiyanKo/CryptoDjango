
from django.contrib import admin
from django.urls import path
from crypto_wallet.views import (
    WalletListView, WalletDetailView, WalletCreateView, 
    WalletUpdateView, WalletDeleteView, CryptoAssetListView, 
    TransactionListView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wallets/', WalletListView.as_view(), name='wallet-list'),
    path('wallets/<int:pk>/', WalletDetailView.as_view(), name='wallet-detail'),
    path('wallets/create/', WalletCreateView.as_view(), name='wallet-create'),
    path('wallets/<int:pk>/update/', WalletUpdateView.as_view(), name='wallet-update'),
    path('wallets/<int:pk>/delete/', WalletDeleteView.as_view(), name='wallet-delete'),
    path('crypto-assets/', CryptoAssetListView.as_view(), name='crypto-asset-list'),
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
]
