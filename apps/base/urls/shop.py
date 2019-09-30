"""The store routes
"""
# Django Library
# Librerias Django
from django.urls import path

# Localfolder Library
# Librerias en carpetas locales
from ..views.shop import WebProductDetailView, WebProductListView

app_name = 'PyShop'

urlpatterns = [
    path('', WebProductListView.as_view(), name='shop'),
    path('product/<int:pk>/', WebProductDetailView.as_view(), name='product'),
]
