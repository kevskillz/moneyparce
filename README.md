# MoneyParce

A personal finance management application built with Django.

## Features

### Admin Features
- User management (view, suspend, reactivate accounts)
- Transaction monitoring
- Spending trend reports
- User notifications
- Fraud detection alerts
- User activity logs
- Account status filtering

### User Features
- Transaction management
- Expense categorization
- Budget setting and tracking
- Financial dashboard
- Budget alerts
- Spending insights
- Savings goals
- Financial advice
- Transaction history export
- Recurring transactions
- Weekly spending reports

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the project root with:
```
DEBUG=True
SECRET_KEY=your-secret-key
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Project Structure
- `moneyparce/` - Main project configuration
- `users/` - User management app
- `transactions/` - Transaction management app
- `budgets/` - Budget management app
- `reports/` - Reporting and analytics app
- `notifications/` - Notification system app 