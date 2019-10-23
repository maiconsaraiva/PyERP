"""uRLs para base
"""
# Django Library
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('move/', include('apps.account.urls.plan')),
    path('plan/', include('apps.account.urls.move')),
    path('invoice/', include('apps.account.urls.invoice')),
    path('journal/', include('apps.account.urls.journal')),
]
