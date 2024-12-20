from django.urls import path
from .views import (
    WalletListView, WalletDetailView, WalletCreateView,
    WalletUpdateView, WalletDeleteView, CryptoAssetListView,
    TransactionListView, home, about, contact, crypto_asset_detail,
    DashboardView, NotificationListView, NotificationCreateView,
    NotificationUpdateView, NotificationDeleteView, user_profile
)

app_name = 'crypto_wallet'

urlpatterns = [
    # Public pages
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/', user_profile, name='user-profile'), #11:47

    # Wallet Views
    path('wallets/', WalletListView.as_view(), name='wallet-list'),
    path('wallets/<int:pk>/', WalletDetailView.as_view(), name='wallet-detail'),
    path('wallets/create/', WalletCreateView.as_view(), name='wallet-create'),
    path('wallets/<int:pk>/update/', WalletUpdateView.as_view(), name='wallet-update'),
    path('wallets/<int:pk>/delete/', WalletDeleteView.as_view(), name='wallet-delete'),

    # Crypto Asset Views
    path('crypto-assets/', CryptoAssetListView.as_view(), name='crypto-asset-list'),
    path('crypto-assets/<int:pk>/', crypto_asset_detail, name='crypto-asset-detail'),

    # Transaction Views
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),

    # Notification Views
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/create/', NotificationCreateView.as_view(), name='notification-create'),
    path('notifications/<int:pk>/update/', NotificationUpdateView.as_view(), name='notification-update'),
    path('notifications/<int:pk>/delete/', NotificationDeleteView.as_view(), name='notification-delete'),
]
