
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Wallet, Transaction, CryptoAsset
from .forms import WalletForm, TransactionForm, CryptoAssetForm
from django.contrib.auth.mixins import LoginRequiredMixin


class WalletListView(LoginRequiredMixin, ListView):
    model = Wallet
    template_name = "wallet_list.html"
    context_object_name = "wallets"


class WalletDetailView(LoginRequiredMixin, DetailView):
    model = Wallet
    template_name = "wallet_detail.html"
    context_object_name = "wallet"


class WalletCreateView(LoginRequiredMixin, CreateView):
    model = Wallet
    form_class = WalletForm
    template_name = "wallet_form.html"
    success_url = reverse_lazy("wallet-list")


class WalletUpdateView(LoginRequiredMixin, UpdateView):
    model = Wallet
    form_class = WalletForm
    template_name = "wallet_form.html"
    success_url = reverse_lazy("wallet-list")


class WalletDeleteView(LoginRequiredMixin, DeleteView):
    model = Wallet
    template_name = "wallet_confirm_delete.html"
    success_url = reverse_lazy("wallet-list")


class CryptoAssetListView(ListView):
    model = CryptoAsset
    template_name = "crypto_asset_list.html"
    context_object_name = "assets"


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "transaction_list.html"
    context_object_name = "transactions"

from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Wallet, Transaction, CryptoAsset
from .serializers import WalletSerializer, TransactionSerializer, CryptoAssetSerializer


class WalletListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class CryptoAssetListAPIView(generics.ListAPIView):
    queryset = CryptoAsset.objects.all()
    serializer_class = CryptoAssetSerializer
