
from django.core.mail import send_mail
from django.conf import settings

def send_transaction_notification(user_email, transaction_details):
    """Send an email notification for a transaction."""
    subject = "Transaction Notification"
    message = f"Dear User,\n\nA transaction has been recorded:\n{transaction_details}\n\nThank you for using Crypto Wallet."
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, email_from, recipient_list)
