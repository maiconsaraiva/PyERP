# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..models.department import PyDepartment

DEPARTMENT_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
]

DEPARTMENT_FIELDS_SHORT = ['name']


class DepartmentListView(LoginRequiredMixin, ListView):
    model = PyDepartment
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(DepartmentListView, self).get_context_data(**kwargs)
        context['title'] = 'Departamentos'
        context['detail_url'] = 'department-detail'
        context['add_url'] = 'base:department-add'
        context['fields'] = DEPARTMENT_FIELDS
        return context


class DepartmentDetailView(LoginRequiredMixin, DetailView):
    model = PyDepartment
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(DepartmentDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:department', 'name': 'Departamento'}]
        context['update_url'] = 'base:department-update'
        context['delete_url'] = 'base:department-delete'
        context['fields'] = DEPARTMENT_FIELDS
        return context


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = PyDepartment
    fields = DEPARTMENT_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(DepartmentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Departamento'
        context['breadcrumbs'] = [{'url': 'base:department', 'name': 'Departamento'}]
        context['back_url'] = reverse('base:department')
        return context


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = PyDepartment
    fields = DEPARTMENT_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(DepartmentUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:departmen', 'name': 'Departamento'}]
        context['back_url'] = reverse('base:departmen-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteDepartment(self, pk):
    department = PyDepartment.objects.get(id=pk)
    department.delete()
    return redirect(reverse('department'))
