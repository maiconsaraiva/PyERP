# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyVariant

VARIANT_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
]

VARIANT_SHORT = ['name']


class VariantListView(LoginRequiredMixin, ListView):
    model = PyVariant
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(VariantListView, self).get_context_data(**kwargs)
        context['title'] = 'Variants'
        context['detail_url'] = 'base:variant-detail'
        context['add_url'] = 'base:variant-add'
        context['fields'] = VARIANT_FIELDS
        return context


class VariantDetailView(LoginRequiredMixin, DetailView):
    model = PyVariant
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(VariantDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:variants', 'name': 'Variants'}]
        context['update_url'] = 'base:variant-update'
        context['delete_url'] = 'base:variant-delete'
        context['fields'] = VARIANT_FIELDS
        return context


class VariantCreateView(LoginRequiredMixin, CreateView):
    model = PyVariant
    fields = VARIANT_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(VariantCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Variant'
        context['breadcrumbs'] = [{'url': 'base:variants', 'name': 'Variants'}]
        context['back_url'] = reverse('base:variants')
        return context


class VariantUpdateView(LoginRequiredMixin, UpdateView):
    model = PyVariant
    fields = VARIANT_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(VariantUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:variants', 'name': 'Variants'}]
        context['back_url'] = reverse('base:variant-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteVariant(self, pk):
    variant = PyVariant.objects.get(id=pk)
    variant.delete()
    return redirect(reverse('base:variants'))
