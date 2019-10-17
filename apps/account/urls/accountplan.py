# Django Library
from django.urls import path

# Localfolder Library
from ..views.accountplan import (
    AccountPlanCreateView, AccountPlanDetailView, AccountPlanListView,
    AccountPlanUpdateView, DeleteAccountPlan)

app_name = 'PyAccountPlan'

urlpatterns = [
    # ========================= Account Plan URL's ========================= #
    path('', AccountPlanListView.as_view(), name='list'),
    path('add/', AccountPlanCreateView.as_view(), name='add'),
    path('<int:pk>/', AccountPlanDetailView.as_view(), name='detail'),
    path('<int:pk>/update', AccountPlanUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteAccountPlan, name='delete'),
]
