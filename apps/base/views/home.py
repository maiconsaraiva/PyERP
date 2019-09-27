# Librerias Django
from django.contrib import messages
from django.shortcuts import render

# Librerias en carpetas locales
from ..models import PyCompany
from .bi import PyBi
from .wparameter import PyWParameter


def _web_parameter():
    web_parameter = {}
    for parametro in PyWParameter.objects.all():
        web_parameter[parametro.name] = parametro.value
    return web_parameter


def erp_home(request):
    """Vista para renderizar el dasboard del erp
    """

    bi_list = PyBi.objects.filter(dashboard='home', type='indicator')
    if bi_list:
        for bi in bi_list:
            if bi.model:
                from ..models import PyPartner
                # print(bi.model)
    value = {
        'bi': bi_list,
        'web_parameter': _web_parameter(),
        'company': PyCompany.objects.filter(active=True)
    }
    # for val in value['bi']:
    #     print val"""

    # print(value)
    return render(request, "home.html", value)
