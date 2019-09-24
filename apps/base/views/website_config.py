# Librerias Django
from django.shortcuts import render
from .web_father import FatherUpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Librerias en carpetas locales
from ..models.website_config import PyWebsiteConfig


class UpdateWebsiteConfigView(LoginRequiredMixin, FatherUpdateView):
    model = PyWebsiteConfig
    template_name = 'base/form.html'
    fields = ['show_blog', 'show_shop', 'under_construction', 'show_chat','show_price','user_register']
