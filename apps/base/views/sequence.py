# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from .web_father import FatherDetailView, FatherListView, FatherUpdateView, FatherCreateView

# Librerias en carpetas locales
from ..models import PySequence

SEQ_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Model"), 'field': 'model'},
    {'string': _("Prefix"), 'field': 'prefix'},
    {'string': _("Padding"), 'field': 'padding'},
    {'string': _("Increment"), 'field': 'increment'},
    {'string': _("Next Number"), 'field': 'next_number'},
]

SEQ_SHORT = ['name', 'model', 'prefix', 'padding', 'increment', 'next_number']


class SequenceListView(LoginRequiredMixin, FatherListView):
    model = PySequence
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(SequenceListView, self).get_context_data(**kwargs)
        context['title'] = 'Sequence'
        context['detail_url'] = 'base:sequence-detail'
        context['add_url'] = 'base:sequence-add'
        context['fields'] = SEQ_FIELDS
        return context


class SequenceDetailView(LoginRequiredMixin, FatherDetailView):
    model = PySequence
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(SequenceDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:sequences', 'name': 'Sequences'}]
        context['update_url'] = 'base:sequence-update'
        context['delete_url'] = 'base:sequence-delete'
        context['fields'] = SEQ_FIELDS
        return context


class SequenceCreateView(LoginRequiredMixin, FatherCreateView):
    model = PySequence
    fields = SEQ_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(SequenceCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Sequence'
        context['breadcrumbs'] = [{'url': 'base:sequences', 'name': 'Sequences'}]
        context['back_url'] = reverse('base:sequences')
        return context


class SequenceUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PySequence
    fields = SEQ_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(SequenceUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:sequences', 'name': 'Sequences'}]
        context['back_url'] = reverse('base:sequence-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteSequence(self, pk):
    sequences = PySequence.objects.get(id=pk)
    sequences.delete()
    return redirect(reverse('base:sequences'))
