"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.channel import (
    ChannelCreateView, ChannelDeleteView, ChannelDetailView, ChannelListView,
    ChannelUpdateView)

app_name = 'PyChannel'

urlpatterns = [
    path('', ChannelListView.as_view(), name='list'),
    path('add/', ChannelCreateView.as_view(), name='add'),
    path('<int:pk>/', ChannelDetailView.as_view(), name='detail'),
    path('<int:pk>/update', ChannelUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ChannelDeleteView.as_view(), name='delete'),
]
