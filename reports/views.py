from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
import csv
from transactions.models import Transaction
from budgets.models import Budget, SavingsGoal

@login_required
def reports(request):
    return render(request, 'reports/reports.html')

@login_required
def spending_report(request):
    # Get transactions for the last 30 days
    end_date = timezone.now().date()
    start_date = end_date - timedelta(days=30)
    
    transactions = Transaction.objects.filter(
        user=request.user,
        transaction_type='expense',
        date__range=[start_date, end_date]
    ).order_by('date')
    
    # Calculate total spending
    total_spending = sum(t.amount for t in transactions)
    
    # Group by category
    category_totals = {}
    for transaction in transactions:
        if transaction.category:
            category_name = transaction.category.name
            category_totals[category_name] = category_totals.get(category_name, 0) + transaction.amount
    
    context = {
        'transactions': transactions,
        'total_spending': total_spending,
        'category_totals': category_totals,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'reports/spending_report.html', context)

@login_required
def income_report(request):
    # Get transactions for the last 30 days
    end_date = timezone.now().date()
    start_date = end_date - timedelta(days=30)
    
    transactions = Transaction.objects.filter(
        user=request.user,
        transaction_type='income',
        date__range=[start_date, end_date]
    ).order_by('date')
    
    # Calculate total income
    total_income = sum(t.amount for t in transactions)
    
    context = {
        'transactions': transactions,
        'total_income': total_income,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'reports/income_report.html', context)

@login_required
def budget_report(request):
    budgets = Budget.objects.filter(user=request.user, is_active=True)
    budget_status = []
    
    for budget in budgets:
        # Get transactions for the current period
        transactions = Transaction.objects.filter(
            user=request.user,
            category=budget.category,
            date__range=[budget.start_date, budget.end_date or timezone.now().date()]
        )
        
        total_spent = sum(t.amount for t in transactions if t.transaction_type == 'expense')
        remaining = budget.amount - total_spent
        
        budget_status.append({
            'budget': budget,
            'total_spent': total_spent,
            'remaining': remaining,
            'percentage_used': (total_spent / budget.amount * 100) if budget.amount > 0 else 0
        })
    
    return render(request, 'reports/budget_report.html', {'budget_status': budget_status})

@login_required
def savings_report(request):
    goals = SavingsGoal.objects.filter(user=request.user)
    return render(request, 'reports/savings_report.html', {'goals': goals})

@login_required
def export_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transactions.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Date', 'Type', 'Amount', 'Category', 'Description'])
    
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    for transaction in transactions:
        writer.writerow([
            transaction.date,
            transaction.get_transaction_type_display(),
            transaction.amount,
            transaction.category.name if transaction.category else '',
            transaction.description
        ])
    
    return response
