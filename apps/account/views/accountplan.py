# Librerias Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..models.accountplan import PyAccountPlan

ACCOUNTPLAN_FIELDS = [
            {'string': 'Código', 'field': 'code'},
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Tipo', 'field': 'type'},
            {'string': 'Conciliación', 'field': 'reconcile'},
        ]

ACCOUNTPLAN_FIELDS_SHORT = ['code','name','type', 'reconcile']


class AccountPlanListView(ListView):
    model = PyAccountPlan
    template_name = 'base/list.html'

    def get_context_data(self, **kwargs):
        context = super(AccountPlanListView, self).get_context_data(**kwargs)
        context['title'] = 'Plan de Cuenta'
        context['detail_url'] = 'base:accountplan-detail'
        context['add_url'] = 'base:accountplan-add'
        context['fields'] = ACCOUNTPLAN_FIELDS
        return context

class AccountPlanDetailView(DetailView):
    model = PyAccountPlan
    template_name = 'base/detail.html'
    def get_context_data(self, **kwargs):
        context = super(AccountPlanDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:accountplan', 'name': 'Cuenta Contable'}]
        context['update_url'] = 'base:accountplan-update'
        context['delete_url'] = 'base:accountplan-delete'
        context['fields'] = ACCOUNTPLAN_FIELDS
        return context

class AccountPlanCreateView(CreateView):
    model = PyAccountPlan
    fields = ACCOUNTPLAN_FIELDS_SHORT
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(AccountPlanCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Cuenta'
        context['breadcrumbs'] = [{'url': 'base:accountplan', 'name': 'Crear Cuenta'}]
        context['back_url'] = reverse('base:accountplan')
        return context

class AccountPlanUpdateView(UpdateView):
    model = PyAccountPlan
    fields = ACCOUNTPLAN_FIELDS_SHORT
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(AccountPlanUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:accountplan', 'name': 'Cuenta Contable'}]
        context['back_url'] = reverse('base:accountplan-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteAccountPlan(self, pk):
    accountplan = PyAccountPlan.objects.get(id=pk)
    accountplan.delete()
    return redirect(reverse('base:accountplan'))
