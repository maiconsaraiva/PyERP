# Librerias Django
from django.shortcuts import render
from django.views.generic.edit import UpdateView

# Librerias en carpetas locales
from ..submodels.website_config import WebsiteConfig


class UpdateWebsiteConfigView(UpdateView):
    model = WebsiteConfig
    template_name = 'base/form.html'
    fields = ['show_blog', 'show_shop', 'under_construction', 'show_chat','show_price']
