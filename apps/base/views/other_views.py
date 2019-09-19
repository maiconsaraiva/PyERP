# Librerias Future
from __future__ import unicode_literals

# Librerias Django
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Librerias en carpetas locales
from ..models.base_config import BaseConfig
from ..forms import InitForm
from ..models.company import PyCompany


def IndexEasy(request):
    if BaseConfig.objects.all().exists():
        template = 'base/index.html'
    else:
        template = 'base/install.html'
    context = {}
    if request.method == 'POST':
        context['form'] = InitForm(request.POST)
        if context['form'].is_valid():
            name = context['form'].cleaned_data.get('name')
            country = context['form'].cleaned_data.get('country')
            currency = context['form'].cleaned_data.get('currency_id')
            BaseConfig.crear(PyCompany.crear(name, country, currency))

            return HttpResponseRedirect(reverse_lazy('home:home_easy'))
    else:
        context['form'] = InitForm()

    return render(request, template, context)
