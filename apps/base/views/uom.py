# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..models import PyUom

UOM_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Ratio"), 'field': 'ratio'},
    {'string': _("Rouding"), 'field': 'rouding'},
    {'string': _("Type"), 'field': 'type'},
    {'string': _("Category"), 'field': 'category_id'},
]

UOM_SHORT = ['name','ratio','rouding','type','category_id']


class UomListView(LoginRequiredMixin, ListView):
    model = PyUom
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(UomListView, self).get_context_data(**kwargs)
        context['title'] = 'Uoms'
        context['detail_url'] = 'base:uom-detail'
        context['add_url'] = 'base:uom-add'
        context['fields'] = UOM_FIELDS
        return context


class UomDetailView(LoginRequiredMixin, DetailView):
    model = PyUom
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(UomDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:Uoms', 'name': 'Uoms'}]
        context['update_url'] = 'base:uom-update'
        context['delete_url'] = 'base:uom-delete'
        context['fields'] = UOM_FIELDS
        return context


class UomCreateView(LoginRequiredMixin, CreateView):
    model = PyUom
    fields = UOM_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(UomCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create UOM'
        context['breadcrumbs'] = [{'url': 'base:uoms', 'name': 'Uoms'}]
        context['back_url'] = reverse('base:uoms')
        return context


class UomUpdateView(LoginRequiredMixin, UpdateView):
    model = PyUom
    fields = UOM_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(UomUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:uoms', 'name': 'Uoms'}]
        context['back_url'] = reverse('base:uom-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteUom(self, pk):
    uom = PyUom.objects.get(id=pk)
    uom.delete()
    return redirect(reverse('base:uoms'))
