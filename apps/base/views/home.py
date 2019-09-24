# Librerias Django
from django.apps import apps
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.management import call_command
from django.shortcuts import redirect, render
from django.urls import clear_url_caches, reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _

# Librerias de terceros
from pyerp.settings import BASE_DIR

from .wparameter import PyWParameter
from .bi import PyBi

def _web_parameter():
    web_parameter = {}
    for parametro in PyWParameter.objects.all():
        web_parameter[parametro.name] = parametro.value
    return web_parameter

@login_required(login_url="base:login")
def erp_home(request):
    """Vista para renderizar el dasboard del erp
    """

    bi_list = PyBi.objects.filter(dashboard='home', type='indicator')
    if bi_list:
        for bi in bi_list:
            if bi.model:
                from ..models import PyPartner
                print(bi.model)
    value = {
        'bi':bi_list,
        'web_parameter': _web_parameter()
    }
    """
    for val in value['bi']:
        print val"""

    print(value)
    return render(request, "home.html", value)