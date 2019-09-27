# Librerias Django
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyMenu
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

MENU_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Parent"), 'field': 'parent_id'},
    {'string': _("Link"), 'field': 'link'},
    {'string': _("Sequence"), 'field': 'sequence'},
]

MENU_SHORT = ['name', 'parent_id', 'link', 'sequence']


class MenuListView(LoginRequiredMixin, FatherListView):
    model = PyMenu
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(MenuListView, self).get_context_data(**kwargs)
        context['title'] = 'Menus'
        context['detail_url'] = 'base:menu-detail'
        context['add_url'] = 'base:menu-add'
        context['fields'] = MENU_FIELDS
        return context


class MenuDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyMenu
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(MenuDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:menus', 'name': 'Menus'}]
        context['update_url'] = 'base:menu-update'
        context['delete_url'] = 'base:menu-delete'
        context['fields'] = MENU_FIELDS
        return context


class MenuCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyMenu
    fields = MENU_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(MenuCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Menu'
        context['breadcrumbs'] = [{'url': 'base:menus', 'name': 'Menus'}]
        context['back_url'] = reverse('base:menus')
        return context


class MenuUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyMenu
    fields = MENU_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(MenuUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].title
        context['breadcrumbs'] = [{'url': 'base:menus', 'name': 'Menus'}]
        context['back_url'] = reverse('base:menu-detail', kwargs={'pk': context['object'].pk})
        return context



class MenuDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyMenu
    success_url = 'base:menus'
