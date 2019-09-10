# Librerias Django
from django.contrib.auth import views as auth_views
from django.urls import path

app_name = 'bim'

# Librerias en carpetas locales
from .views.bim_project import (
    BimProjectListView, BimProjectDetailView, BimProjectCreateView,
    BimProjectUpdateView, DeleteBimProject)

urlpatterns = [
    path('project', BimProjectListView.as_view(), name='project'),
    path('project/add/', BimProjectCreateView.as_view(), name='project-add'),
    path('project/<int:pk>/', BimProjectDetailView.as_view(), name='project-detail'),
    path('project/<int:pk>/update', BimProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', DeleteBimProject, name='project-delete'),
]