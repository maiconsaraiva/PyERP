"""uRLs para gestionar los plugin
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.plugin import (
    PluginInstall, PluginListView, PluginUninstall, PluginUpdate)

app_name = 'PyPlugin'

urlpatterns = [
    path('', PluginListView.as_view(), name='list'),
    path('update', PluginUpdate, name='update'),
    path('install/<int:pk>/', PluginInstall, name='create'),
    path('uninstall/<int:pk>/', PluginUninstall, name='delete'),
]
