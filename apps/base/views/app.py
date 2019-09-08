# Librerias Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# Librerias en carpetas locales
from ...base.models import PyApp

APP_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Author', 'field': 'author'},
    {'string': 'Description', 'field': 'description'},
    {'string': 'Installed', 'field': 'installed'},
]


class AppView(LoginRequiredMixin, ListView):
    model = PyApp
    template_name = 'base/apps.html'
    fields = APP_FIELDS
    paginate_by = 80
