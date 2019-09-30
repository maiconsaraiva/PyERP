# Librerias Django
# Django Library
from django.urls import path

# Localfolder Library
# Librerias en carpetas locales
from .views.paypal_config import UpdatePaypalConfigView

# http://www.secnot.com/django-shop-paypal-rest-1.html

app_name = 'paypal'

urlpatterns = [
    path('paypal-config/<int:pk>', UpdatePaypalConfigView.as_view(), name='paypal-config'),
]
