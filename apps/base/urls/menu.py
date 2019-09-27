# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.menu import (
    MenuDeleteView, MenuCreateView, MenuDetailView, MenuListView, MenuUpdateView)

urlpatterns = [
    path('menus', MenuListView.as_view(), name='menus'),
    path('menu/add/', MenuCreateView.as_view(), name='menu-add'),
    path('menu/<int:pk>/', MenuDetailView.as_view(), name='menu-detail'),
    path('menu/<int:pk>/update', MenuUpdateView.as_view(), name='menu-update'),
    path('menu/<int:pk>/delete/', MenuDeleteView.as_view(), name='menu-delete'),
]