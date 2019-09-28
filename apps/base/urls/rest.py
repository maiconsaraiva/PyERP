from django.contrib import admin
from django.urls import path
from ..views.rest import loginApiRest

urlpatterns = [
    path('login', loginApiRest)
]