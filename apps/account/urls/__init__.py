"""uRLs para base
"""
# Django Library
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('account/move/', include('apps.account.urls.plan')),
    path('account/plan/', include('apps.account.urls.move')),
    path('invoice/', include('apps.account.urls.invoice')),
]
