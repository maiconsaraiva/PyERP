# Librerias Django
from django.contrib.auth import views as auth_views
from django.urls import path

# Librerias en carpetas locales
from .views import (
    CampaignCreateView, CampaignDetailView, CampaignListView,
    CampaignUpdateView, ChannelCreateView, ChannelDetailView, ChannelListView,
    ChannelUpdateView, DeleteCampaign, DeleteChannel, DeleteMform,
    MformCreateView, MformDetailView, MformListView, MformUpdateView)

urlpatterns = [
    path('channel', ChannelListView.as_view(), name='channel'),
    path('channel/add/', ChannelCreateView.as_view(), name='channel-add'),
    path('channel/<int:pk>/', ChannelDetailView.as_view(), name='channel-detail'),
    path('channel/<int:pk>/update', ChannelUpdateView.as_view(), name='channel-update'),
    path('channel/<int:pk>/delete/', DeleteChannel, name='channel-delete'),

    path('campaign', CampaignListView.as_view(), name='campaign'),
    path('campaign/add/', CampaignCreateView.as_view(), name='campaign-add'),
    path('campaign/<int:pk>/', CampaignDetailView.as_view(), name='campaign-detail'),
    path('campaign/<int:pk>/update', CampaignUpdateView.as_view(), name='campaign-update'),
    path('campaign/<int:pk>/delete/', DeleteCampaign, name='campaign-delete'),

    path('mform', MformListView.as_view(), name='mform'),
    path('mform/add/', MformCreateView.as_view(), name='mform-add'),
    path('mform/<int:pk>/', MformDetailView.as_view(), name='mform-detail'),
    path('mform/<int:pk>/update', MformUpdateView.as_view(), name='mform-update'),
    path('mform/<int:pk>/delete/', DeleteMform, name='mform-delete'),
]
