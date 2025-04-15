from django import forms
from django.core.exceptions import ValidationError
from .models import Transaction, Category

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount',
            'transaction_type',
            'category',
            'description',
            'date',
            'is_recurring',
            'recurring_frequency'
        ]
        widgets = {
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00'
            }),
            'transaction_type': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'is_recurring': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'recurring_frequency': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # Limit categories to those created by this user
        if user:
            self.fields['category'].queryset = Category.objects.filter(created_by=user)
        else:
            self.fields['category'].queryset = Category.objects.none()

    def clean_name(self):
        # (if you have name validation, but here omitted)
        return self.cleaned_data.get('name', '')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data['name']
        if self.user and not self.instance.pk:
            if Category.objects.filter(name=name, created_by=self.user).exists():
                raise ValidationError('A category with this name already exists.')
        return name
