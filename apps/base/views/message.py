# Librerias Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyLog, PyMessage
from .web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView, FatherDeleteView)

MESSAGE_FIELDS = [
    {'string': _("Message"), 'field': 'message'},
]

MESSAGE_SHORT = ['message', 'user_id']


class MessageListView(LoginRequiredMixin, FatherListView):
    model = PyMessage
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(MessageListView, self).get_context_data(**kwargs)
        context['title'] = 'message'
        context['detail_url'] = 'base:message-detail'
        context['add_url'] = 'base:message-add'
        context['fields'] = MESSAGE_FIELDS
        return context


class MessageDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyMessage
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(MessageDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].message
        context['breadcrumbs'] = [{'url': 'base:messages', 'name': 'Messages'}]
        context['update_url'] = 'base:message-update'
        context['delete_url'] = 'base:message-delete'
        context['fields'] = MESSAGE_FIELDS
        return context


class MessageCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyMessage
    fields = MESSAGE_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(MessageCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Message'
        context['breadcrumbs'] = [{'url': 'base:messages', 'name': 'Messages'}]
        context['back_url'] = reverse('base:messages')
        return context


class MessageUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyMessage
    fields = MESSAGE_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(MessageUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].title
        context['breadcrumbs'] = [{'url': 'base:messages', 'name': 'Messages'}]
        context['back_url'] = reverse('base:message-detail', kwargs={'pk': context['object'].pk})
        return context



class MessageDeleteView(FatherDeleteView):
    model = PyMessage
    success_url = 'base:messages'
