# Librerias Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyLog
from ..models import PyTag
from .web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView)

TAG_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
]

TAG_SHORT = ['name']


class TagListView(LoginRequiredMixin, FatherListView):
    model = PyTag
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context['title'] = 'Tags'
        context['detail_url'] = 'base:tag-detail'
        context['add_url'] = 'base:tag-add'
        context['fields'] = TAG_FIELDS
        return context


class TagDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyTag
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:tags', 'name': 'Tags'}]
        context['update_url'] = 'base:tag-update'
        context['delete_url'] = 'base:tag-delete'
        context['fields'] = TAG_FIELDS
        return context


class TagCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyTag
    fields = TAG_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(TagCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Tag'
        context['breadcrumbs'] = [{'url': 'base:tags', 'name': 'Tags'}]
        context['back_url'] = reverse('base:tags')
        return context


class TagUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyTag
    fields = TAG_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(TagUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:tags', 'name': 'Tags'}]
        context['back_url'] = reverse('base:tag-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteTag(self, pk):
    tag = PyTag.objects.get(id=pk)
    tag.delete()
    return redirect(reverse('base:tags'))
