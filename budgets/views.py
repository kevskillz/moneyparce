from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Budget, SavingsGoal
from .forms import BudgetForm, SavingsGoalForm
from transactions.models import Category

@login_required
def budget_list(request):
    budgets = Budget.objects.filter(user=request.user, is_active=True)
    return render(request, 'budgets/budget_list.html', {'budgets': budgets})

@login_required
def budget_create(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            messages.success(request, 'Budget created successfully!')
            return redirect('budget_list')
    else:
        form = BudgetForm()
        form.fields['category'].queryset = Category.objects.filter(created_by=request.user)
    return render(request, 'budgets/budget_form.html', {'form': form})

@login_required
def budget_edit(request, pk):
    budget = get_object_or_404(Budget, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            messages.success(request, 'Budget updated successfully!')
            return redirect('budget_list')
    else:
        form = BudgetForm(instance=budget)
        form.fields['category'].queryset = Category.objects.filter(created_by=request.user)
    return render(request, 'budgets/budget_form.html', {'form': form})

@login_required
def budget_delete(request, pk):
    budget = get_object_or_404(Budget, pk=pk, user=request.user)
    if request.method == 'POST':
        budget.delete()
        messages.success(request, 'Budget deleted successfully!')
        return redirect('budget_list')
    return render(request, 'budgets/budget_confirm_delete.html', {'budget': budget})

@login_required
def savings_goals(request):
    savings_goals = SavingsGoal.objects.filter(user=request.user)
    return render(request, 'budgets/savings_goals.html', {'savings_goals': savings_goals})

@login_required
def savings_goal_create(request):
    if request.method == 'POST':
        form = SavingsGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, 'Savings goal created successfully!')
            return redirect('savings_goals')
    else:
        form = SavingsGoalForm()
    return render(request, 'budgets/savings_goal_form.html', {'form': form})

@login_required
def savings_goal_edit(request, pk):
    goal = get_object_or_404(SavingsGoal, pk=pk, user=request.user)
    if request.method == 'POST':
        form = SavingsGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Savings goal updated successfully!')
            return redirect('savings_goals')
    else:
        form = SavingsGoalForm(instance=goal)
    return render(request, 'budgets/savings_goal_form.html', {'form': form})

@login_required
def savings_goal_delete(request, pk):
    savings_goal = get_object_or_404(SavingsGoal, pk=pk, user=request.user)
    if request.method == 'POST':
        savings_goal.delete()
        messages.success(request, 'Savings goal deleted successfully!')
        return redirect('savings_goals')
    return render(request, 'budgets/savings_goal_confirm_delete.html', {'savings_goal': savings_goal})
