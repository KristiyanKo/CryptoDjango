
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Wallet, Transaction, CryptoAsset

class WalletTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.wallet = Wallet.objects.create(owner=self.user, balance=1000)

    def test_wallet_list_view(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("wallet-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.wallet.balance)

    def test_wallet_detail_view(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("wallet-detail", args=[self.wallet.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.wallet.owner.username)

    def test_wallet_create_view(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("wallet-create"), {"balance": 500})
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertEqual(Wallet.objects.count(), 2)

    def test_wallet_update_view(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("wallet-update", args=[self.wallet.id]), {"balance": 1500})
        self.assertEqual(response.status_code, 302)  # Redirect after update
        self.wallet.refresh_from_db()
        self.assertEqual(self.wallet.balance, 1500)

    def test_wallet_delete_view(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("wallet-delete", args=[self.wallet.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after deletion
        self.assertEqual(Wallet.objects.count(), 0)


class CryptoAssetTests(TestCase):
    def setUp(self):
        self.crypto_asset = CryptoAsset.objects.create(name="Bitcoin", symbol="BTC", price=50000)

    def test_crypto_asset_list_view(self):
        response = self.client.get(reverse("crypto-asset-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.crypto_asset.name)


class TransactionTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.wallet = Wallet.objects.create(owner=self.user, balance=1000)
        self.transaction = Transaction.objects.create(wallet=self.wallet, amount=200)

    def test_transaction_list_view(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("transaction-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.transaction.amount)


class APITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="apitestuser", password="password")
        self.wallet = Wallet.objects.create(owner=self.user, balance=1000)
        self.crypto_asset = CryptoAsset.objects.create(name="Ethereum", symbol="ETH", price=3000)
        self.client.login(username="apitestuser", password="password")

    def test_wallet_api_list(self):
        response = self.client.get(reverse("api-wallets"))
        self.assertEqual(response.status_code, 200)

    def test_crypto_asset_api_list(self):
        response = self.client.get(reverse("api-crypto-assets"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.crypto_asset.name)
