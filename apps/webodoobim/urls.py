# Librerias Django
from django.conf.urls import url
from django.urls import path
from .views.views import index

app_name = 'webodoobim'

urlpatterns = [
    url(r'^$', index, name='index'),
]