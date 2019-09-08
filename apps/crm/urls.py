# Librerias Django
from django.contrib.auth import views as auth_views
from django.urls import path

# Librerias en carpetas locales
from .views.dashboard import DashboardCrmView
from .views.lead import (
    DeleteLead, LeadCreateView, LeadDetailView, LeadListView, LeadUpdateView)
from .views.stage import (
    DeleteStage, StageCreateView, StageDetailView, StageListView,
    StageUpdateView)

urlpatterns = [
    path('dashboard-crm', DashboardCrmView, name='dashboard-crm'),

    path('lead', LeadListView.as_view(), name='lead'),
    path('lead/add/', LeadCreateView.as_view(), name='lead-add'),
    path('lead/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('lead/<int:pk>/update', LeadUpdateView.as_view(), name='lead-update'),
    path('lead/<int:pk>/delete/', DeleteLead, name='lead-delete'),

    path('stage', StageListView.as_view(), name='stage'),
    path('stage/add/', StageCreateView.as_view(), name='stage-add'),
    path('stage/<int:pk>/', StageDetailView.as_view(), name='stage-detail'),
    path('stage/<int:pk>/update', StageUpdateView.as_view(), name='stage-update'),
    path('stage/<int:pk>/delete/', DeleteStage, name='stage-delete'),
]
