from django.contrib import admin
from .models import Budget, SavingsGoal

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'period', 'start_date', 'end_date', 'is_active')
    list_filter = ('period', 'is_active', 'start_date', 'end_date')
    search_fields = ('user__username', 'category__name')
    ordering = ('-start_date',)
    date_hierarchy = 'start_date'
    
    fieldsets = (
        (None, {
            'fields': ('user', 'category', 'amount', 'period')
        }),
        ('Date Information', {
            'fields': ('start_date', 'end_date')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )

@admin.register(SavingsGoal)
class SavingsGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'target_amount', 'current_amount', 'target_date', 'is_completed')
    list_filter = ('is_completed', 'target_date')
    search_fields = ('user__username', 'name')
    ordering = ('-target_date',)
    date_hierarchy = 'target_date'
    
    fieldsets = (
        (None, {
            'fields': ('user', 'name', 'target_amount', 'current_amount')
        }),
        ('Target Information', {
            'fields': ('target_date',)
        }),
        ('Status', {
            'fields': ('is_completed',)
        }),
    )
