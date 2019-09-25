# Librerias Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyLog
from ..models.meta import PyMeta
from .web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView, FatherDeleteView)

META_FIELDS = [
            {'string': _("Title"), 'field': 'title'},
            {'string': _("Content"), 'field': 'content'},
        ]

META_FIELDS_SHORT = ['title','content']

class MetaListView(LoginRequiredMixin, FatherListView):
    model = PyMeta
    template_name = 'base/list.html'

    def get_context_data(self, **kwargs):
        context = super(MetaListView, self).get_context_data(**kwargs)
        context['title'] = 'Metas'
        context['detail_url'] = 'base:meta-detail'
        context['add_url'] = 'base:meta-add'
        context['fields'] = META_FIELDS
        return context

class MetaDetailView(FatherDetailView):
    model = PyMeta
    template_name = 'base/detail.html'
    def get_context_data(self, **kwargs):
        context = super(MetaDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].title
        context['breadcrumbs'] = [{'url': 'base:metas', 'name': 'Metas'}]
        context['update_url'] = 'base:meta-update'
        context['delete_url'] = 'base:meta-delete'
        context['fields'] = META_FIELDS
        return context


class MetaCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyMeta
    fields = META_FIELDS_SHORT
    template_name = 'base/form.html'
    success_url = reverse_lazy('base:metas')

    def get_context_data(self, **kwargs):
        context = super(MetaCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Meta'
        context['breadcrumbs'] = [{'url': 'base:metas', 'name': 'Metas'}]
        context['back_url'] = reverse('base:metas')
        return context


class MetaUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyMeta
    fields = META_FIELDS_SHORT
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(MetaUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].title
        context['breadcrumbs'] = [{'url': 'base:metas', 'name': 'Metas'}]
        context['back_url'] = reverse('base:meta-detail', kwargs={'pk': context['object'].pk})
        return context



class MetaDeleteView(FatherDeleteView):
    model = PyMeta
    success_url = 'base:metas'
