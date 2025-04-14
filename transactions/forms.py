from django import forms
from django.core.exceptions import ValidationError
from .models import Transaction, Category

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'transaction_type', 'category', 'description', 'date', 'is_recurring', 'recurring_frequency']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = Category.objects.filter(created_by=user)
        else:
            self.fields['category'].queryset = Category.objects.none()

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data['name']
        if self.user:
            # Check if a category with this name already exists for this user
            if Category.objects.filter(name=name, created_by=self.user).exists():
                if not self.instance.pk:  # Only check for new categories
                    raise ValidationError('A category with this name already exists.')
        return name 