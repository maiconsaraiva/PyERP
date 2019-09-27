"""uRLs para base
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views import (
    Install, ProviderListView, UpdateBaseConfigView)
from ..views.base_config import LoadData
from ..views.home import erp_home
from ..views.website_config import UpdateWebsiteConfigView

app_name = 'base'

urlpatterns = [
    path('', erp_home, name='home'),
    path('install', Install, name='install'),
    # path('install-erp', InstallPyERP, name='install-erp'),
    # path('logoutmodal/', LogOutModalView.as_view(), name='logout-modal'),
    path('config/<int:pk>', UpdateBaseConfigView.as_view(), name='base-config'),
    path('load-data', LoadData, name='load-data'),

    path('website-config/<int:pk>', UpdateWebsiteConfigView.as_view(), name='website-config'),

    path('provider', ProviderListView.as_view(), name='provider'),
]
