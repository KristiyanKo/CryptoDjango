from rest_framework import serializers
from .models import Wallet, Transaction, CryptoAsset

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'owner', 'balance', 'created_at']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'wallet', 'asset', 'amount', 'transaction_type', 'timestamp']

class CryptoAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoAsset
        fields = ['id', 'name', 'symbol', 'price']
