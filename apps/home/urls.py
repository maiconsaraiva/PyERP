# Librerias Django
from django.conf.urls import url
from django.urls import path


from .views.views import (
    BlogView, PostDetailView, UnderConstruction, WebProductDetailView,
    WebProductView, contact, index)


app_name = 'home'

urlpatterns = [
    url(r'^$', index, name='home-index'),

    path('blog/', BlogView.as_view(), name='home-blog'),
    path('blog/post/<int:pk>/', PostDetailView.as_view(), name='post'),

    path(r'shop/', WebProductView.as_view(), name='home-shop'),
    path(r'shop/product/<int:pk>/', WebProductDetailView.as_view(), name='home-product'),

    url(r'^license/', license, name='home-license'),
    url(r'^under-construction/', UnderConstruction, name='under-construction'),
    url(r'^contact_me$', contact, name='contact-me'),

    

    
]
