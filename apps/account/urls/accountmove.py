# Django Library
from django.urls import path

# Localfolder Library
from ..views.accountmove import (
    AccountMoveCreateView, AccountMoveDeleteView, AccountMoveDetailView,
    AccountMoveListView, AccountMoveUpdateView)

app_name = 'PyAccountMove'

urlpatterns = [
    # ========================= Account Move URL's ========================= #
    path('', AccountMoveListView.as_view(), name='list'),
    path('add/', AccountMoveCreateView.as_view(), name='add'),
    path('<int:pk>/', AccountMoveDetailView.as_view(), name='detail'),
    path('<int:pk>/update', AccountMoveUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', AccountMoveDeleteView.as_view(), name='delete'),
]
