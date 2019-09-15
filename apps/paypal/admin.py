# Librerias Django
from django.contrib import admin
from .models.paypal_config import PaypalConfig

admin.site.register(PaypalConfig)
