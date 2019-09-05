from django.urls import path
from .views.views import IndexEasy

urlpatterns = [
    path('', IndexEasy, name='home_easy'),
]
