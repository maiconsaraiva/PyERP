# Librerias Django
from django.contrib import messages
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import connections, router, transaction

# Librerias en carpetas locales
from ..models import PySequence
from .web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView, FatherDeleteView)

SEQ_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Prefix"), 'field': 'prefix'},
    {'string': _("Padding"), 'field': 'padding'},
    {'string': _("Initial"), 'field': 'initial'},
    {'string': _("Increment"), 'field': 'increment'},
    {'string': _("Reset"), 'field': 'reset'},
    {'string': _("Last"), 'field': 'last'},
]

SEQ_SHORT = ['name', 'prefix', 'padding', 'initial', 'increment', 'reset', 'last']


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
        DO UPDATE SET last = sequences_sequence.last + %s
            RETURNING last;
"""

MYSQL_UPSERT = """
    INSERT INTO sequences_sequence (name, prefix, padding, initial, increment, reset, last)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY
        UPDATE last = sequences_sequence.last + %s
"""


def get_last_value(name='default', *, using=None,):
    """
    Return the last value for a given sequence.
    """
    # Inner import because models cannot be imported before their application.
    from ..models import PySequence

    if using is None:
        using = router.db_for_read(PySequence)

    connection = connections[using]

    with connection.cursor() as cursor:
        cursor.execute(SELECT, [name])
        result = cursor.fetchone()

    return None if result is None else result[0]


def get_next_value(name='default', prefix='default', padding=4, initial=1, increment=1, reset=None, *, nowait=False, using=None):
    """
    Return the next value for a given sequence.
    """
    # Inner import because models cannot be imported before their application.
    from ..models import PySequence

    try:
        sequence = PySequence.objects.get(name=name)
        prefix = sequence.prefix
        initial = sequence.initial
        increment = sequence.increment
        reset = sequence.reset
        padding = sequence.padding
    except PySequence.DoesNotExist:
        sequence = None

    if reset is not None:
        assert initial < reset

    if using is None:
        using = router.db_for_write(PySequence)

    connection = connections[using]

    if (connection.vendor == 'postgresql' and getattr(connection, 'pg_version', 0) >= 90500 and reset is None and not nowait):

        # PostgreSQL ≥ 9.5 supports "upsert".
        # This is about 3x faster as the naive implementation.

        with connection.cursor() as cursor:
            cursor.execute(
                POSTGRESQL_UPSERT,
                [name, prefix, padding, initial, increment, reset, initial]
            )
            result = cursor.fetchone()

        return '{}{}'.format(prefix, str(result[0]).zfill(padding))

    elif (connection.vendor == 'mysql' and reset is None and not nowait):

        # MySQL supports "upsert" but not "returning".
        # This is about 2x faster as the naive implementation.

        with transaction.atomic(using=using, savepoint=False):
            with connection.cursor() as cursor:
                cursor.execute(
                    MYSQL_UPSERT,
                    [name, prefix, padding, initial, increment, reset, initial]
                )
                cursor.execute(SELECT, [name])
                result = cursor.fetchone()

        return '{}{}'.format(prefix, str(result[0]).zfill(padding))

    else:

        # Default, ORM-based implementation for all other cases.
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
                        'last': initial
                    }
                )
            )
            if not created:
                sequence.last += increment
                if reset is not None and sequence.last >= reset:
                    sequence.last = initial
                sequence.save()

            return '{}{}'.format(prefix, str(sequence.last).zfill(padding))


# class PySequence:
#     """
#     Generate a gapless sequence of integer values.
#     """
#     def __init__(self, name='default', initial=1, reset=None, *, using=None):
#         if reset is not None:
#             assert initial < reset
#         self.name = name
#         self.initial = initial
#         self.reset = reset
#         self.using = using

#     def get_last_value(self):
#         """
#         Return the last value of the sequence.
#         """
#         return get_last_value(
#             self.name,
#             using=self.using,
#         )

#     def get_next_value(self, *, nowait=False):
#         """
#         Return the next value of the sequence.
#         """
#         return get_next_value(
#             self.name,
#             self.initial,
#             self.reset,
#             nowait=nowait,
#             using=self.using,
#         )

#     def __iter__(self):
#         return self

#     def __next__(self):
#         return self.get_next_value()