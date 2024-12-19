
from django.db import models
from django.contrib.auth.models import User

class CryptoAsset(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10, unique=True)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.symbol})"

    class Meta:
        ordering = ['name']

class Wallet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wallets")
    balance = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Wallet of {self.owner.username}"

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self.save()

    class Meta:
        ordering = ['-created_at']

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('buy', 'Buy'),
        ('sell', 'Sell')
    ]

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="transactions")
    asset = models.ForeignKey(CryptoAsset, on_delete=models.CASCADE, related_name="transactions")
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def total_value(self):
        return self.amount * self.asset.price

    def __str__(self):
        return f"{self.transaction_type.capitalize()} {self.amount} {self.asset.symbol}"

    class Meta:
        ordering = ['-timestamp']

class PriceHistory(models.Model):
    asset = models.ForeignKey(CryptoAsset, on_delete=models.CASCADE, related_name="price_history")
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asset.symbol} - {self.price} at {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
