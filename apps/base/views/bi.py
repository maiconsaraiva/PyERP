# Librerias Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyBi, PyLog
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

BI_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Type"), 'field': 'type'},
    {'string': _("Model"), 'field': 'model'},
    {'string': _("Parameter"), 'field': 'parameter'},
    {'string': _("Color"), 'field': 'color'},
    {'string': _("Font Color"), 'field': 'font_color'},
    {'string': _("Icon"), 'field': 'icon'},
    {'string': _("Dashboard"), 'field': 'dashboard'},
    {'string': _("Url"), 'field': 'url'},
]

BI_SHORT = ['name', 'type', 'model', 'parameter', 'color', 'font_color', 'icon', 'dashboard','url']


class BiListView(LoginRequiredMixin, FatherListView):
    model = PyBi
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(BiListView, self).get_context_data(**kwargs)
        context['title'] = 'BI'
        context['detail_url'] = 'base:bi-detail'
        context['add_url'] = 'base:bi-add'
        context['fields'] = BI_FIELDS
        return context


class BiDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyBi
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(BiDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:bi', 'name': 'Bi'}]
        context['update_url'] = 'base:bi-update'
        context['delete_url'] = 'base:bi-delete'
        context['fields'] = BI_FIELDS
        return context


class BiCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyBi
    fields = BI_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(BiCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Bi'
        context['breadcrumbs'] = [{'url': 'base:bi', 'name': 'BI'}]
        context['back_url'] = reverse('base:bi')
        return context


class BiUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyBi
    fields = BI_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(BiUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:bi', 'name': 'Bi'}]
        context['back_url'] = reverse('base:bi-detail', kwargs={'pk': context['object'].pk})
        return context



class BiDeleteView(FatherDeleteView):
    model = PyBi
    success_url = 'base:bi'
