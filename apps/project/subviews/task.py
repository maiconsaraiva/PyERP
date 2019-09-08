# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..submodels.task import PyTask

""" BEGIN TASK """
TASK_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Estado', 'field': 'state'},
            {'string': 'Usuario', 'field': 'user_id'},
            {'string': 'Proyecto', 'field': 'project_id'},
            {'string': 'Notas', 'field': 'note'},
        ]

TASK_FIELDS_SHORT = ['name','state','user_id','project_id','note']


class TaskListView(LoginRequiredMixin, ListView):
    model = PyTask
    template_name = 'base/list.html'
    login_url = "/base/login"

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context['title'] = 'Tareas'
        context['detail_url'] = 'task-detail'
        context['add_url'] = 'task-add'
        context['fields'] = TASK_FIELDS
        return context

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = PyTask
    template_name = 'base/detail.html'
    login_url = "/base/login"

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'task', 'name': 'Tarea'}]
        context['update_url'] = 'task-update'
        context['delete_url'] = 'task-delete'
        context['fields'] = TASK_FIELDS
        return context

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = PyTask
    fields = TASK_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "/base/login"

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Tarea'
        context['breadcrumbs'] = [{'url': 'task', 'name': 'Tarea'}]
        context['back_url'] = reverse('task')
        return context

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = PyTask
    fields = TASK_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "/base/login"

    def get_context_data(self, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'task', 'name': 'Tarea'}]
        context['back_url'] = reverse('task-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="login")
def DeleteTask(self, pk):
    task = PyTask.objects.get(id=pk)
    task.delete()
    return redirect(reverse('task'))
""" END TASK """
