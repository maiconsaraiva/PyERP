# Librerias Django
from django.contrib import admin
from django.urls import path

# Librerias en carpetas locales
from ..views.rest import loginApiRest

urlpatterns = [
    path('login', loginApiRest)
]
