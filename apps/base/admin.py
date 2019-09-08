# Librerias Django
from django.contrib import admin

# Librerias en carpetas locales
from .models import (
    PyApp, PyCompany, PyCountry, PyPartner, PyProduct, PyProductCategory)

admin.site.register(PyPartner)
admin.site.register(PyProduct)
admin.site.register(PyCountry)
admin.site.register(PyProductCategory)
admin.site.register(PyCompany)
admin.site.register(PyApp)
