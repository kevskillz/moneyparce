from django.urls import path
from . import views

urlpatterns = [
    path('', views.reports, name='reports'),
    path('spending/', views.spending_report, name='spending_report'),
    path('income/', views.income_report, name='income_report'),
    path('budget/', views.budget_report, name='budget_report'),
    path('savings/', views.savings_report, name='savings_report'),
    path('export/', views.export_data, name='export_data'),
] 