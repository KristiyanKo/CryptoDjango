from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Wallet, Transaction, CryptoAsset
from .forms import WalletForm, TransactionForm, CryptoAssetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404
from django import forms
from django.urls import reverse
from django.views.generic import TemplateView

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

# NEW 19:55
def home(request):
    return render(request, 'home.html', {'title': 'Home'})

# Public View: About Page
def about(request):
    return render(request, 'about.html', {'title': 'About Us'})

# Public View: Contact Page
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the valid form data here
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'title': 'Contact Us'})

# Exception Handling Example in a View
def crypto_asset_detail(request, pk):
    try:
        asset = get_object_or_404(CryptoAsset, pk=pk)
    except CryptoAsset.DoesNotExist:
        raise Http404("Crypto Asset not found")
    except Exception as e:
        return render(request, 'error.html', {'error_message': str(e)})

    return render(request, 'crypto_asset_detail.html', {'asset': asset})

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, label="Message")

def dashboard(request):
    return render(request, 'dashboard.html', {'title': 'Dashboard'})

class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    extra_context = {'title': 'Dashboard'}
