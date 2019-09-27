"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.channel import (
    ChannelCreateView, ChannelDeleteView, ChannelDetailView, ChannelListView,
    ChannelUpdateView)

urlpatterns = [
    path('channels', ChannelListView.as_view(), name='channels'),
    path('channel/add/', ChannelCreateView.as_view(), name='channel-add'),
    path('channel/<int:pk>/', ChannelDetailView.as_view(), name='channel-detail'),
    path('channel/<int:pk>/update', ChannelUpdateView.as_view(), name='channel-update'),
    path('channel/<int:pk>/delete/', ChannelDeleteView.as_view(), name='channel-delete'),
]
