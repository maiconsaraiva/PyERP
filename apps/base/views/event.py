# Librerias Django
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyEvent
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

EVENT_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Note"), 'field': 'note'},
    {'string': _("Begin Date"), 'field': 'begin_date'},
]

EVENT_SHORT = ['name', 'note', 'begin_date']


class EventListView(LoginRequiredMixin, FatherListView):
    model = PyEvent
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        context['title'] = 'Events'
        context['detail_url'] = 'base:event-detail'
        context['add_url'] = 'base:event-add'
        context['fields'] = EVENT_FIELDS
        return context


class EventDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyEvent
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:events', 'name': 'Events'}]
        context['update_url'] = 'base:event-update'
        context['delete_url'] = 'base:event-delete'
        context['fields'] = EVENT_FIELDS
        return context


class EventCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyEvent
    fields = EVENT_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(EventCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Event'
        context['breadcrumbs'] = [{'url': 'base:events', 'name': 'Events'}]
        context['back_url'] = reverse('base:events')
        return context


class EventUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyEvent
    fields = EVENT_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(EventUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:events', 'name': 'Events'}]
        context['back_url'] = reverse('base:event-detail', kwargs={'pk': context['object'].pk})
        return context



class EventDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyEvent
    success_url = 'base:events'
