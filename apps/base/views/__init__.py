# Librerias Django
from django.apps import apps
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.management import call_command
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import clear_url_caches, reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Librerias de terceros
from pyerp.settings import BASE_DIR

# Librerias en carpetas locales
from ..forms import AvatarForm
from ..models import (
    BaseConfig, PyCompany, PyPartner, PyPlugin, PyProduct, PyProductCategory,
    PyUser, PyWebsiteConfig)
from .activatelanguage import ActivateLanguageView
from .base_config import UpdateBaseConfigView
from .company import (
    CompanyCreateView, CompanyDetailView, CompanyListView, CompanyUpdateView,
    DeleteCompany, change_active_company)
from .partner import (
    CustomerListView, ProviderListView)
from .usercustom import (
    ActivateUserView, AvatarUpdateView, LogOutModalView, PasswordRecoveryView,
    ProfileView, SignUpView, cambio_clave)
from .web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView)
from .wparameter import PyWParameter


def _web_parameter():
    web_parameter = {}
    for parametro in PyWParameter.objects.all():
        web_parameter[parametro.name] = parametro.value
    return web_parameter

def Install(request):
    return render(request, 'base/install.html')


class UserListView(FatherListView):
    model = PyUser
    template_name = 'base/list.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Usuarios'
        context['detail_url'] = 'base:user-detail'
        context['add_url'] = 'base:user-add'
        context['fields'] = [
            {'string': _('Name'), 'field': 'first_name'},
            {'string': _('Last name'), 'field': 'last_name'},
            {'string': _('Email'), 'field': 'email'},
        ]
        return context


class UserDetailView(FatherDetailView):
    model = PyUser
    template_name = 'base/detail.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].email
        context['breadcrumbs'] = [{'url': 'base:users', 'name': 'Usuarios'}]
        context['update_url'] = 'base:user-update'
        context['delete_url'] = 'base:user-delete'
        context['fields'] = [
            {'string': _('Name'), 'field': 'first_name'},
            {'string': _('Last name'), 'field': 'last_name'},
            {'string': _('Email'), 'field': 'email'},
        ]
        context['buttons'] = [
            {
                'act': reverse('base:password-change', kwargs={'pk': context['object'].pk}),
                'name': 'Cambiar contraseña',
                'class': 'success'
            }
        ]
        return context


class UserCreateView(FatherCreateView):
    model = PyUser
    fields = ['email', 'first_name', 'last_name', 'password']
    template_name = 'base/form.html'
    success_url = 'base:user-detail'

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Usuario'
        context['breadcrumbs'] = [{'url': 'base:users', 'name': 'Usuarios'}]
        context['back_url'] = reverse('base:users')
        return context

    def form_valid(self, form):
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        company = self.request.user.active_company
        self.object = PyUser.create(first_name, last_name, email, password, 0, 0, 1, company)
        url = reverse_lazy(self.get_success_url(), kwargs={'pk': self.object.pk})

        return HttpResponseRedirect(url)


class UserUpdateView(FatherUpdateView):
    model = PyUser
    fields = ['email', 'first_name', 'last_name', 'partner_id']
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].email
        context['breadcrumbs'] = [{'url': 'base:users', 'name': 'Usuarios'}]
        context['back_url'] = reverse('base:user-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteUser(self, pk):
    user = PyUser.objects.get(id=pk)
    user.delete()
    return redirect(reverse('base:users'))


def ChangePasswordForm(self, pk):
    return render(self, 'base/change_password.html', {'pk': pk})


def DoChangePassword(self, pk, **kwargs):
    user = PyUser.objects.get(id=pk)
    if user and self.POST['new_password1'] == self.POST['new_password2']:
        user.set_password(self.POST['new_password1'])
    else:
        return render(self, 'base/change_password.html', {'pk': pk, 'error': 'Las contraseñas no coinciden.'})
    return redirect(reverse('base:user-detail', kwargs={'pk': pk}))
