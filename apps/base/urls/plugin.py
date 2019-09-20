"""uRLs para gestionar los plugin
"""
# Librerias Django
from django.contrib.auth.decorators import login_required
from django.urls import path

# Librerias en carpetas locales
from ..views.plugin import (
    PluginInstall, PluginListView, PluginUninstall, PluginUpdate)

urlpatterns = [
    path('', login_required(PluginListView.as_view()), name='list-plugin'),
    path(
        'update-plugin',
        login_required(PluginUpdate),
        name='update-plugin'
    ),
    path(
        'install-plugin/<int:pk>/',
        login_required(PluginInstall),
        name='install-plugin'
    ),
    path(
        'uninstall-plugin/<int:pk>/',
        login_required(PluginUninstall),
        name='uninstall-plugin'
    ),
]
