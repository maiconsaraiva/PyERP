# Librerias Django
from django.contrib.auth import views as auth_views
from django.urls import path

# Librerias en carpetas locales
from .views.accountmove import (
    AccountMoveCreateView, AccountMoveDetailView, AccountMoveListView,
    AccountMoveUpdateView, DeleteAccountMove)
from .views.accountplan import (
    AccountPlanCreateView, AccountPlanDetailView, AccountPlanListView,
    AccountPlanUpdateView, DeleteAccountPlan)

urlpatterns = [
    path('accountplan', AccountPlanListView.as_view(), name='accountplan'),
    path('accountplan/add/', AccountPlanCreateView.as_view(), name='accountplan-add'),
    path('accountplan/<int:pk>/', AccountPlanDetailView.as_view(), name='accountplan-detail'),
    path('accountplan/<int:pk>/update', AccountPlanUpdateView.as_view(), name='accountplan-update'),
    path('accountplan/<int:pk>/delete/', DeleteAccountPlan, name='accountplan-delete'),

    path('account-move', AccountMoveListView.as_view(), name='account-move'),
    path('account-move/add/', AccountMoveCreateView.as_view(), name='account-move-add'),
    path('account-move/<int:pk>/', AccountMoveDetailView.as_view(), name='account-move-detail'),
    path('account-move/<int:pk>/update', AccountMoveUpdateView.as_view(), name='account-move-update'),
    path('account-move/<int:pk>/delete/', DeleteAccountMove, name='account-move-delete'),
]
