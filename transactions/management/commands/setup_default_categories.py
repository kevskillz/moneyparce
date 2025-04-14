from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from transactions.models import Category

DEFAULT_CATEGORIES = [
    # Income Categories
    {'name': 'Salary', 'description': 'Regular employment income'},
    {'name': 'Freelance', 'description': 'Income from freelance work'},
    {'name': 'Investments', 'description': 'Income from investments'},
    {'name': 'Gifts', 'description': 'Gifts and donations received'},
    
    # Expense Categories
    {'name': 'Housing', 'description': 'Rent, mortgage, utilities'},
    {'name': 'Food', 'description': 'Groceries and dining out'},
    {'name': 'Transportation', 'description': 'Car, public transport, fuel'},
    {'name': 'Healthcare', 'description': 'Medical expenses, insurance'},
    {'name': 'Entertainment', 'description': 'Movies, games, hobbies'},
    {'name': 'Shopping', 'description': 'Clothing, electronics, etc.'},
    {'name': 'Education', 'description': 'Tuition, books, courses'},
    {'name': 'Travel', 'description': 'Vacations and trips'},
    {'name': 'Bills', 'description': 'Phone, internet, subscriptions'},
    {'name': 'Savings', 'description': 'Money set aside for savings'},
]

class Command(BaseCommand):
    help = 'Creates default categories for all users'

    def handle(self, *args, **options):
        User = get_user_model()
        users = User.objects.all()
        if not users:
            self.stdout.write(self.style.WARNING('No users found in the database'))
            return

        for user in users:
            self.stdout.write(f'Setting up categories for user: {user.username}')
            for category_data in DEFAULT_CATEGORIES:
                category, created = Category.objects.get_or_create(
                    name=category_data['name'],
                    created_by=user,
                    defaults={'description': category_data['description']}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Category already exists: {category.name}')) 