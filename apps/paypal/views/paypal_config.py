# Librerias Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.edit import UpdateView

# Librerias en carpetas locales
from ..models import PaypalConfig


class UpdatePaypalConfigView(LoginRequiredMixin, UpdateView):
    login_url = "login"
    model = PaypalConfig
    template_name = 'base/form.html'
    fields = ['mode', 'paypal_client_id', 'paypal_client_secret', 'online']
