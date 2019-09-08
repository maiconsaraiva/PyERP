# Librerias Django
from django.contrib import admin

# Librerias en carpetas locales
from .models import WebsiteConfig

admin.site.register(WebsiteConfig)
