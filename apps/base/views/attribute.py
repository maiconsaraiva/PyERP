# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..models import PyAttribute

ATTRIBUTE_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Variant"), 'field': 'variant_id'},
]

ATTRIBUTE_SHORT = ['name','variant_id']


class AttributeListView(LoginRequiredMixin, ListView):
    model = PyAttribute
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(AttributeListView, self).get_context_data(**kwargs)
        context['title'] = 'Attribute'
        context['detail_url'] = 'base:attribute-detail'
        context['add_url'] = 'base:attribute-add'
        context['fields'] = ATTRIBUTE_FIELDS
        return context


class AttributeDetailView(LoginRequiredMixin, DetailView):
    model = PyAttribute
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(AttributeDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:attributes', 'name': 'Attribute'}]
        context['update_url'] = 'base:attribute-update'
        context['delete_url'] = 'base:attribute-delete'
        context['fields'] = ATTRIBUTE_FIELDS
        return context


class AttributeCreateView(LoginRequiredMixin, CreateView):
    model = PyAttribute
    fields = ATTRIBUTE_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(AttributeCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Attribute'
        context['breadcrumbs'] = [{'url': 'base:attributes', 'name': 'Attributes'}]
        context['back_url'] = reverse('base:attributes')
        return context


class AttributeUpdateView(LoginRequiredMixin, UpdateView):
    model = PyAttribute
    fields = ATTRIBUTE_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(AttributeUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:attributes', 'name': 'Attributes'}]
        context['back_url'] = reverse('base:attribute-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteAttribute(self, pk):
    attribute = PyFaq.objects.get(id=pk)
    attribute.delete()
    return redirect(reverse('base:attributes'))
