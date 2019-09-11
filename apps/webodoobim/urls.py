# Librerias Django
from django.conf.urls import url
from django.urls import path
from .views.views import index, about, services, contact, blog

app_name = 'webodoobim'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'about/', about, name='about'),
    url(r'services/', services, name='services'),
    url(r'contact/', contact, name='contact'),
    url(r'blog/', blog, name='blog'),

]