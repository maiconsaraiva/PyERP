# Librerias Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _
from .web_father import FatherDetailView, FatherListView, FatherUpdateView, FatherCreateView

# Librerias en carpetas locales
from ..models.page import PyPage

PAGE_FIELDS = [
            {'string': _("Title"), 'field': 'title'},
            {'string': _("Created on"), 'field': 'created_on'},
            {'string': _("Keywords"), 'field': 'keywords'},

        ]

PAGE_FIELDS_SHORT = ['title','content','keywords']

class PageListView(FatherListView):
    model = PyPage
    template_name = 'base/list.html'

    def get_context_data(self, **kwargs):
        context = super(PageListView, self).get_context_data(**kwargs)
        context['title'] = 'Pages'
        context['detail_url'] = 'base:page-detail'
        context['add_url'] = 'base:page-add'
        context['fields'] = PAGE_FIELDS
        return context

class PageDetailView(FatherDetailView):
    model = PyPage
    template_name = 'base/detail.html'
    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].title
        context['breadcrumbs'] = [{'url': 'base:page-backend', 'name': 'Pages'}]
        context['update_url'] = 'base:page-update'
        context['delete_url'] = 'base:page-delete'
        context['fields'] = PAGE_FIELDS
        return context


class PageCreateView(FatherCreateView):
    model = PyPage
    fields = PAGE_FIELDS_SHORT
    template_name = 'base/form.html'
    success_url = reverse_lazy('base:page-backend')

    def get_context_data(self, **kwargs):
        context = super(PageCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Page'
        context['breadcrumbs'] = [{'url': 'base:page-backend', 'name': 'Page'}]
        context['back_url'] = reverse('base:page-backend')
        return context


class PageUpdateView(FatherUpdateView):
    model = PyPage
    fields = PAGE_FIELDS_SHORT
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(PageUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].title
        context['breadcrumbs'] = [{'url': 'base:page-backend', 'name': 'Page'}]
        context['back_url'] = reverse('base:page-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeletePage(self, pk):
    page = PyPage.objects.get(id=pk)
    page.delete()
    return redirect(reverse('base:page-backend'))
