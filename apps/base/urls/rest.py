# Librerias Django
# Django Library
from django.contrib import admin
from django.urls import path

# Localfolder Library
# Librerias en carpetas locales
from ..views.rest import loginApiRest

urlpatterns = [
    path('login', loginApiRest)
]
