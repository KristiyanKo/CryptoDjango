
import logging

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("crypto_wallet.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("CryptoWallet")

# Example usage in views.py
# logger.info("User created a new wallet.")
# logger.error("Failed transaction attempt.")
