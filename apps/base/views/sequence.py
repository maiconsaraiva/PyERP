# Librerias Django
from django.contrib import messages
from django.db import connections, router, transaction
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PySequence
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

SEQ_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Prefix"), 'field': 'prefix'},
    {'string': _("Padding"), 'field': 'padding'},
    {'string': _("Initial"), 'field': 'initial'},
    {'string': _("Increment"), 'field': 'increment'},
    {'string': _("Reset"), 'field': 'reset'},
    {'string': _("Next"), 'field': 'next_val'},
]

SEQ_SHORT = ['name', 'prefix', 'padding', 'initial', 'increment', 'reset', 'next_val']


class SequenceListView(FatherListView):
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


class SequenceDetailView(FatherDetailView):
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


class SequenceCreateView(FatherCreateView):
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


class SequenceUpdateView(FatherUpdateView):
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


# ========================================================================== #
class SequenceDeleteView(FatherDeleteView):
    model = PySequence
    success_url = 'base:sequences'


# ========================================================================== #
SELECT = """
    SELECT last
    FROM sequences_sequence
    WHERE name = %s
"""

POSTGRESQL_UPSERT = """
    INSERT INTO sequences_sequence (name, prefix, padding, initial, increment, reset, last)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (name)
    DO UPDATE SET (last = sequences_sequence.last + %s, nex_val = sequences_sequence.last + 1 + %s)
    RETURNING last;
"""

MYSQL_UPSERT = """
    INSERT INTO sequences_sequence (name, prefix, padding, initial, increment, reset, last)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY
    UPDATE (last = sequences_sequence.last + %s, next_val = sequences_sequence.last + 1 + %s)
"""

def get_next_value(name='default', prefix='default', padding=4, initial=1, increment=1, reset=None, *, nowait=False, using=None):
    """
    Return the next value for a given sequence.
    """
    if reset is not None:
        assert initial < reset

    if using is None:
        using = router.db_for_write(PySequence)

    with transaction.atomic(using=using, savepoint=False):
        sequence, created = (
            PySequence.objects.select_for_update(
                nowait=nowait
            ).get_or_create(
                name=name,
                defaults={
                    'prefix': prefix,
                    'padding': padding,
                    'initial': initial,
                    'increment': increment,
                    'reset': reset,
                    'last': initial,
                    'next_val': initial + 1
                }
            )
        )
        if not created:
            if (sequence.last + 1) != sequence.next_val:
                sequence.last = sequence.next_val
            else:
                sequence.last += increment

            sequence.next_val = sequence.last + 1

            if reset is not None and sequence.last >= reset:
                sequence.last = initial

            sequence.save()
        return '{}{}'.format(prefix, str(sequence.last).zfill(padding))
