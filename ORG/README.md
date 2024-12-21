
# Crypto Wallet Django Application

## Project Overview
Crypto Wallet is a Django-based web application for managing cryptocurrency portfolios. Users can track their wallets, transactions, and cryptocurrency assets. The application provides an intuitive interface for financial management and supports essential CRUD operations for wallet management.

## Key Features
- User authentication (registration, login, and logout).
- Manage wallets with balance tracking and transaction history.
- Cryptocurrency asset management.
- Price history tracking for assets.
- Dynamic PDF generation for transaction reports.
- Mobile-friendly responsive design using Bootstrap.
- Secure user management with CSRF and XSS protection.
- Automated tests for functionality, security, and performance.

## Technologies Used
- **Backend**: Django Framework, PostgreSQL (or SQLite for local development)
- **Frontend**: Django Template Engine, Bootstrap 5
- **Testing**: Django Test Framework
- **Monitoring**: Integrated logging for important actions

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/KristiyanKo/CryptoDjango/crypto-wallet.git
   ```

2. Navigate to the project directory:
   ```bash
   cd crypto-wallet
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Running Tests
To execute tests, run:
```bash
python manage.py test
```

## Deployment
For deployment, ensure the following:
- Set `DEBUG = False` in `settings.py`.
- Configure database settings for production (e.g., PostgreSQL).
- Use a WSGI server like Gunicorn.
