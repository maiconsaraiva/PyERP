# Librerias Future
from __future__ import unicode_literals
from django.shortcuts import HttpResponse, render

def IndexEasy(request):
    return render(request, 'base/index.html')