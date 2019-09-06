from django.urls import path
from .views.other_views import IndexEasy

urlpatterns = [
    path('', IndexEasy, name='home_easy'),
]
