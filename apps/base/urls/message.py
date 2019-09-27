"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.message import (
    MessageCreateView, MessageDeleteView, MessageDetailView, MessageListView,
    MessageUpdateView)

urlpatterns = [
    path('messages', MessageListView.as_view(), name='messages'),
    path('message/add/', MessageCreateView.as_view(), name='message-add'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
    path('message/<int:pk>/update', MessageUpdateView.as_view(), name='message-update'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message-delete'),
]
