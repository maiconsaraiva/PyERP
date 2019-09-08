# Librerias Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..models.accountmove import PyAccountMove

ACCOUNTMOVE_FIELDS = [
            {'string': 'Código', 'field': 'code'},
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Estado', 'field': 'state'},
        ]

ACCOUNTMOVE_FIELDS_SHORT = ['code','name','state']


class AccountMoveListView(ListView):
    model = PyAccountMove
    template_name = 'base/list.html'

    def get_context_data(self, **kwargs):
        context = super(AccountMoveListView, self).get_context_data(**kwargs)
        context['title'] = 'Asiento Contable'
        context['detail_url'] = 'base:account-move-detail'
        context['add_url'] = 'base:account-move-add'
        context['fields'] = ACCOUNTMOVE_FIELDS
        return context

class AccountMoveDetailView(DetailView):
    model = PyAccountMove
    template_name = 'base/detail.html'
    def get_context_data(self, **kwargs):
        context = super(AccountMoveDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:account-move', 'name': 'Asiento Contable'}]
        context['update_url'] = 'base:account-move-update'
        context['delete_url'] = 'base:account-move-delete'
        context['fields'] = ACCOUNTMOVE_FIELDS
        return context

class AccountMoveCreateView(CreateView):
    model = PyAccountMove
    fields = ACCOUNTMOVE_FIELDS_SHORT
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(AccountMoveCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Asiento'
        context['breadcrumbs'] = [{'url': 'base:account-move', 'name': 'Crear Asiento'}]
        context['back_url'] = reverse('base:account-move')
        return context

class AccountMoveUpdateView(UpdateView):
    model = PyAccountMove
    fields = ACCOUNTMOVE_FIELDS_SHORT
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(AccountMoveUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:account-move', 'name': 'Asiento Contable'}]
        context['back_url'] = reverse('base:account-move-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteAccountMove(self, pk):
    accountmove = PyAccountMove.objects.get(id=pk)
    accountmove.delete()
    return redirect(reverse('base:account-move'))
