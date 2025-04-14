from django.contrib import admin
from .models import Transaction, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')
    list_filter = ('created_by',)
    search_fields = ('name', 'description')
    ordering = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'transaction_type', 'category', 'date', 'is_recurring')
    list_filter = ('transaction_type', 'is_recurring', 'date', 'category')
    search_fields = ('user__username', 'description', 'category__name')
    ordering = ('-date', '-created_at')
    date_hierarchy = 'date'
    
    fieldsets = (
        (None, {
            'fields': ('user', 'amount', 'transaction_type', 'category', 'description')
        }),
        ('Date Information', {
            'fields': ('date',)
        }),
        ('Recurring Settings', {
            'fields': ('is_recurring', 'recurring_frequency'),
            'classes': ('collapse',)
        }),
    )
