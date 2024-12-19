
from django import forms
from .models import Wallet, Transaction, CryptoAsset


class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ["balance"]


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["wallet", "amount"]


class CryptoAssetForm(forms.ModelForm):
    class Meta:
        model = CryptoAsset
        fields = ["name", "symbol", "price"]
