from django.urls import path
from . import views

urlpatterns = [
    path('', views.budget_list, name='budget_list'),
    path('create/', views.budget_create, name='budget_create'),
    path('<int:pk>/edit/', views.budget_edit, name='budget_edit'),
    path('<int:pk>/delete/', views.budget_delete, name='budget_delete'),
    path('savings-goals/', views.savings_goals, name='savings_goals'),
    path('savings-goals/create/', views.savings_goal_create, name='savings_goal_create'),
    path('savings-goals/<int:pk>/edit/', views.savings_goal_edit, name='savings_goal_edit'),
    path('savings-goals/<int:pk>/delete/', views.savings_goal_delete, name='savings_goal_delete'),
] 