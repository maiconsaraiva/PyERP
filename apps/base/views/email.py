# Librerias Django
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyEmail, PyLog
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

EMAIL_FIELDS = [
    {'string': _("Title"), 'field': 'title'},
    {'string': _("Creation Date"), 'field': 'fc'},
    {'string': _("Partner"), 'field': 'partner_id'},
    {'string': _("Type"), 'field': 'type'}
]

EMAIL_SHORT = ['title', 'content', 'partner_id', 'type']


class EmailListView(FatherListView):
    model = PyEmail
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(EmailListView, self).get_context_data(**kwargs)
        context['title'] = 'Emails'
        context['detail_url'] = 'base:email-detail'
        context['add_url'] = 'base:email-add'
        context['fields'] = EMAIL_FIELDS
        return context


class EmailDetailView(FatherDetailView):
    model = PyEmail
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(EmailDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].title
        context['breadcrumbs'] = [{'url': 'base:emails', 'name': 'Emails'}]
        context['update_url'] = 'base:email-update'
        context['delete_url'] = 'base:email-delete'
        context['fields'] = EMAIL_FIELDS
        return context


class EmailCreateView(FatherCreateView):
    model = PyEmail
    fields = EMAIL_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(EmailCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Email'
        context['breadcrumbs'] = [{'url': 'base:emails', 'name': 'Emails'}]
        context['back_url'] = reverse('base:emails')
        return context


class EmailUpdateView(FatherUpdateView):
    model = PyEmail
    fields = EMAIL_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(EmailUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].title
        context['breadcrumbs'] = [{'url': 'base:emails', 'name': 'Emails'}]
        context['back_url'] = reverse('base:email-detail', kwargs={'pk': context['object'].pk})
        return context


class EmailDeleteView(FatherDeleteView):
    model = PyEmail
    success_url = 'base:emails'
