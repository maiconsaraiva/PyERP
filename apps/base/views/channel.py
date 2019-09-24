# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyChannel
from .web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView)

CHANNEL_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Code"), 'field': 'code'},
]

CHANNEL_SHORT = ['name','code']


class ChannelListView(LoginRequiredMixin, FatherListView):
    model = PyChannel
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ChannelListView, self).get_context_data(**kwargs)
        context['title'] = 'Channels'
        context['detail_url'] = 'base:channel-detail'
        context['add_url'] = 'base:channel-add'
        context['fields'] = CHANNEL_FIELDS
        return context


class ChannelDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyChannel
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ChannelDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:channels', 'name': 'Channels'}]
        context['update_url'] = 'base:channel-update'
        context['delete_url'] = 'base:channel-delete'
        context['fields'] = CHANNEL_FIELDS
        return context


class ChannelCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyChannel
    fields = CHANNEL_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ChannelCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Channel'
        context['breadcrumbs'] = [{'url': 'base:channels', 'name': 'Channels'}]
        context['back_url'] = reverse('base:channels')
        return context


class ChannelUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyChannel
    fields = CHANNEL_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ChannelUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:channels', 'name': 'Channels'}]
        context['back_url'] = reverse('base:channel-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteChannel(self, pk):
    channel = PyChannel.objects.get(id=pk)
    channel.delete()
    return redirect(reverse('base:channels'))
