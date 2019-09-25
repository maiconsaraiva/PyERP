"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.event import (
    DeleteEvent, EventCreateView, EventDetailView, EventListView, EventUpdateView)

urlpatterns = [
    path('events', EventListView.as_view(), name='events'),
    path('event/add/', EventCreateView.as_view(), name='event-add'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/<int:pk>/update', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', DeleteEvent, name='event-delete'),
]