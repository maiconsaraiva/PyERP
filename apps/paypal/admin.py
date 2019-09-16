# Librerias Django
from django.contrib import admin

# Librerias en carpetas locales
from .models.paypal_config import PaypalConfig

admin.site.register(PaypalConfig)
