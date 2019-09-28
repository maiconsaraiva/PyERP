# Librerias Django
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Librerias en carpetas locales
from ..models.base_config import BaseConfig
from .web_father import FatherUpdateView


class UpdateBaseConfigView(LoginRequiredMixin, FatherUpdateView):
    model = BaseConfig
    template_name = 'base/form.html'
    fields = ['online', 'open_menu', 'main_company_id', 'type_share']


def LoadData(LoginRequiredMixin, request):
    state = BaseConfig.objects.get(pk=1).load_data
    if state:
        print("Ya existe Data")
    else:
        print("Cargamos")
    return render(request, 'base/ok.html')
