# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from .views.other_views import IndexEasy

app_name = 'home'
urlpatterns = [
    path('', IndexEasy, name='home_easy'),
]
