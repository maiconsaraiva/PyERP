"""Rutas de PyErp
"""
# Librerias Django
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from django.views.static import serve

# Librerias de terceros
from apps.base.views import ActivateLanguageView

urlpatterns = [
    path('', include('apps.base.home_urls')),
    # path('admin/', admin.site.urls),
    # path('base/', include('apps.base.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT, }),
    path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT, }),
    # path('', include('apps.home.urls')),
]

urlpatterns += i18n_patterns(
    # path('', include('apps.base.home_urls')),
    path('base/', include('apps.base.urls')),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path(
        '<language_code>/language/activate/',
        ActivateLanguageView.as_view(),
        name='activate_language'
    ),
)


with open('installed_apps.py', 'r') as ins_apps_file:
    for line in ins_apps_file.readlines():
        if line.strip() == 'apps.home':
            urlpatterns.pop(0)
            urlpatterns += [path('', include('apps.home.urls'))]
        else:
            _, app = line.split('.')
            urlpatterns += [path('%s/' % app, include('%s.urls' % line.strip()))]
