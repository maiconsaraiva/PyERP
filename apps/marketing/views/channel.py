# Librerias Django
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Librerias en carpetas locales
from ..models import PyChannel

CHANNEL_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Código', 'field': 'code'},
        ]

CHANNEL_FIELDS_SHORT = ['name','code']


class ChannelListView(LoginRequiredMixin, ListView):
    model = PyChannel
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ChannelListView, self).get_context_data(**kwargs)
        context['title'] = 'Canales'
        context['detail_url'] = 'channel-detail'
        context['add_url'] = 'base:channel-add'
        context['fields'] = CHANNEL_FIELDS
        return context

class ChannelDetailView(LoginRequiredMixin, DetailView):
    model = PyChannel
    template_name = 'base/detail.html'
    def get_context_data(self, **kwargs):
        context = super(ChannelDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'channel', 'name': 'Canal'}]
        context['update_url'] = 'channel-update'
        context['delete_url'] = 'channel-delete'
        context['fields'] = CHANNEL_FIELDS
        return context

class ChannelCreateView(LoginRequiredMixin, CreateView):
    model = PyChannel
    fields = CHANNEL_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ChannelCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Canal'
        context['breadcrumbs'] = [{'url': 'channel', 'name': 'Canal'}]
        context['back_url'] = reverse('channel')
        return context

class ChannelUpdateView(LoginRequiredMixin, UpdateView):
    model = PyChannel
    fields = CHANNEL_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ChannelUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'channel', 'name': 'Canal'}]
        context['back_url'] = reverse('channel-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteChannel(self, pk):
    channel = PyChannel.objects.get(id=pk)
    channel.delete()
    return redirect(reverse('channel'))
