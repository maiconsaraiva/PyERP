"""Rutas de PyErp
"""
# Librerias Django
from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.static import serve

urlpatterns = [
    path('', include('apps.base.home_urls')),
    path('admin/', admin.site.urls),
    path('base/', include('apps.base.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT, }),
    path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT, }),
]


with open('installed_apps.py', 'r') as ins_apps_file:
    for line in ins_apps_file.readlines():
        app, _ = line.split('.')
        urlpatterns += [path('%s/' % app, include('%s.urls' % line.strip()))]
