# Librerias Django
from django.apps import apps
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.management import call_command
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
    DeleteCompany)
from .partner import (
    CustomerListView, DeletePartner, PartnerAutoComplete, PartnerCreateView,
    PartnerDetailView, PartnerUpdateView, ProviderListView)
from .usercustom import (
    ActivateUserView, AvatarUpdateView, LogOutModalView, PasswordRecoveryView,
    ProfileView, SignUpView, cambio_clave)

from .wparameter import PyWParameter


def _web_parameter():
    web_parameter = {}
    for parametro in PyWParameter.objects.all():
        web_parameter[parametro.name] = parametro.value
    return web_parameter

def Install(request):
    return render(request, 'base/install.html')


class UserListView(ListView):
    model = PyUser
    template_name = 'base/list.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Usuarios'
        context['detail_url'] = 'base:user-detail'
        context['add_url'] = 'base:user-add'
        context['fields'] = [
            {'string': _('User Name'), 'field': 'username'},
            {'string': _('Name'), 'field': 'first_name'},
            {'string': _('Last name'), 'field': 'last_name'},
            {'string': _('Email'), 'field': 'email'},
        ]
        return context


class UserDetailView(DetailView):
    model = PyUser
    template_name = 'base/detail.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].username
        context['breadcrumbs'] = [{'url': 'base:users', 'name': 'Usuarios'}]
        context['update_url'] = 'base:user-update'
        context['delete_url'] = 'base:user-delete'
        context['fields'] = [
            {'string': _('User Name'), 'field': 'username'},
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


class UserCreateView(CreateView):
    model = PyUser
    fields = ['username', 'email', 'first_name', 'last_name', 'password']
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Usuario'
        context['breadcrumbs'] = [{'url': 'base:users', 'name': 'Usuarios'}]
        context['back_url'] = reverse('base:users')
        return context


class UserUpdateView(UpdateView):
    model = PyUser
    fields = ['username', 'email', 'first_name', 'last_name']
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].username
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


@login_required(login_url="base:login")
def erp_home(request):
    """Vista para renderizar el dasboard del erp
    """
    count_plugin = PyPlugin.objects.all().count()
    plugins = PyPlugin.objects.all().filter(installed=True).order_by('sequence')
    plugin_list = []
    if plugins:
        for plugin in plugins:
            st = plugin.name + "/menu.html"
            plugin_list.append(st.lower())

    partners = PyPartner.objects.all()
    return render(request, "home.html", {
        'customers': partners.filter(customer=True),
        'providers': partners.filter(provider=True),
        'users': PyUser.objects.all(),
        'products': PyProduct.objects.all(),
        'plugin_list': plugin_list,
        'count_plugin': count_plugin,
        'web_parameter':_web_parameter()
    })
