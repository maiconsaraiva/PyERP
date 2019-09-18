# Librerias Future
from __future__ import unicode_literals

# Librerias Django
from django.shortcuts import render

# Librerias en carpetas locales
from ...base.models.base_config import BaseConfig


def IndexEasy(request):
    if BaseConfig.objects.all().exists():
        return render(request, 'base/index.html')
    else:
        return render(request, 'base/install.html')
