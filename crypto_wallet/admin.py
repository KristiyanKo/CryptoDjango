
from django.contrib import admin
from .models import Wallet, Transaction, CryptoAsset, PriceHistory


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "balance", "created_at")
    list_filter = ("owner", "created_at")
    search_fields = ("owner__username",)
    ordering = ("created_at",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "wallet", "amount", "created_at")
    list_filter = ("created_at", "wallet")
    search_fields = ("wallet__owner__username",)


@admin.register(CryptoAsset)
class CryptoAssetAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "symbol", "price")
    search_fields = ("name", "symbol")
    ordering = ("name",)


@admin.register(PriceHistory)
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ("id", "asset", "price", "timestamp")
    list_filter = ("asset", "timestamp")
    ordering = ("-timestamp",)
