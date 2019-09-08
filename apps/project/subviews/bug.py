# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..submodels.bug import PyBug

""" BEGIN BUG """
BUG_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Estado', 'field': 'state'},
            {'string': 'Usuario', 'field': 'user_id'},
            {'string': 'Notas', 'field': 'note'},
        ]

BUG_FIELDS_SHORT = ['name','state','user_id','note']


class BugListView(LoginRequiredMixin, ListView):
    model = PyBug
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(BugListView, self).get_context_data(**kwargs)
        context['title'] = 'Errores'
        context['detail_url'] = 'base:bug-detail'
        context['add_url'] = 'base:bug-add'
        context['fields'] = BUG_FIELDS
        return context

class BugDetailView(LoginRequiredMixin, DetailView):
    model = PyBug
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(BugDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:bug', 'name': 'Error'}]
        context['update_url'] = 'base:bug-update'
        context['delete_url'] = 'base:bug-delete'
        context['fields'] = BUG_FIELDS
        return context

class BugCreateView(LoginRequiredMixin, CreateView):
    model = PyBug
    fields = BUG_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(BugCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Error'
        context['breadcrumbs'] = [{'url': 'base:bug', 'name': 'Error'}]
        context['back_url'] = reverse('base:bug')
        return context

class BugUpdateView(LoginRequiredMixin, UpdateView):
    model = PyBug
    fields = BUG_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(BugUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:bug', 'name': 'Error'}]
        context['back_url'] = reverse('base:bug-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteBug(self, pk):
    bug = PyBug.objects.get(id=pk)
    bug.delete()
    return redirect(reverse('bug'))
