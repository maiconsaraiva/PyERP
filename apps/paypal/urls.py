# Librerias Django
from django.urls import path
from .views.paypal_config import UpdatePaypalConfigView

app_name = 'paypal'

urlpatterns = [
    path('paypal-config/<int:pk>', UpdatePaypalConfigView.as_view(), name='paypal-config'),
]
