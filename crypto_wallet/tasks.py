
from celery import shared_task
from .models import CryptoAsset
import random

@shared_task
def update_crypto_prices():
    for asset in CryptoAsset.objects.all():
        asset.price = random.uniform(10, 10000)
        asset.save()
