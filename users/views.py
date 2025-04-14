from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserProfileForm
from transactions.models import Transaction
from budgets.models import Budget, SavingsGoal
from notifications.models import Notification

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def dashboard(request):
    recent_transactions = Transaction.objects.filter(user=request.user).order_by('-date')[:5]
    active_budgets = Budget.objects.filter(user=request.user, is_active=True)
    savings_goals = SavingsGoal.objects.filter(user=request.user, is_completed=False)
    
    context = {
        'recent_transactions': recent_transactions,
        'active_budgets': active_budgets,
        'savings_goals': savings_goals,
    }
    return render(request, 'users/dashboard.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})

@login_required
def settings(request):
    return render(request, 'users/settings.html')
