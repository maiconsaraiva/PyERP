"""uRLs para base
"""
# Django Library
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('account-move/', include('apps.account.urls.accountplan')),
    path('account-plan/', include('apps.account.urls.accountmove')),
    path('invoice/', include('apps.account.urls.invoice')),
]
