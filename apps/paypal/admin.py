# Librerias Django
# Django Library
from django.contrib import admin

# Localfolder Library
# Librerias en carpetas locales
from .models.paypal_config import PaypalConfig

admin.site.register(PaypalConfig)
