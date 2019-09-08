# Librerias Future
from __future__ import unicode_literals

# Librerias Django
from django.shortcuts import HttpResponse, render


def IndexEasy(request):
    return render(request, 'base/index.html')
