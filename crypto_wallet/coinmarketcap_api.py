
import requests
from .models import CryptoAsset

COINMARKETCAP_API_KEY = "4a779c7d-7b91-4858-8fb7-57278f3244a2"
COINMARKETCAP_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

class CoinMarketCapAPI:
    @staticmethod
    def fetch_crypto_prices():
        """Fetch the latest cryptocurrency prices from CoinMarketCap."""
        headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": COINMARKETCAP_API_KEY,
        }
        params = {
            "start": "1",
            "limit": "100",
            "convert": "USD",
        }
        response = requests.get(COINMARKETCAP_URL, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()["data"]
        else:
            raise Exception(f"Error fetching data from CoinMarketCap: {response.status_code}")

    @staticmethod
    def update_crypto_prices():
        """Update cryptocurrency prices in the database."""
        try:
            data = CoinMarketCapAPI.fetch_crypto_prices()
            for asset_data in data:
                symbol = asset_data["symbol"]
                price = asset_data["quote"]["USD"]["price"]

                asset, created = CryptoAsset.objects.get_or_create(symbol=symbol, defaults={"name": asset_data["name"]})
                asset.price = price
                asset.save()

                if created:
                    print(f"Created new asset: {symbol}")
                else:
                    print(f"Updated asset: {symbol}")
        except Exception as e:
            print(f"Error updating prices: {e}")
