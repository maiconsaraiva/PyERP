# Librerias Django
from django.conf.urls import url
from django.urls import path

# Librerias en carpetas locales
from .views.post import (
    DeletePost, PostCreateView, PostDetailView, PostListView, PostUpdateView)

from .views.views import (
    BlogView, PostDetailView, UnderConstruction, WebProductDetailView,
    WebProductView, contact, index)

from .views.website_config import UpdateWebsiteConfigView

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

    path('post', PostListView.as_view(), name='post'),
    path('post/add/', PostCreateView.as_view(), name='post-add'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DeletePost, name='post-delete'),

    path('config/<int:pk>', UpdateWebsiteConfigView.as_view(), name='website-config'),
]
