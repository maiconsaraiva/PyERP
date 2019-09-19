# Librerias Standard
import json
import os
import subprocess
import sys
from collections import OrderedDict
from importlib import reload
from os import listdir

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
    BaseConfig, PyApp, PyCompany, PyPartner, PyProduct, PyProductCategory,
    PyUser, PyWebsiteConfig)
from .activate import ActivateView
from .activatelanguage import ActivateLanguageView
from .avatar import AvatarUpdateView
from .base_config import UpdateBaseConfigView
from .company import (
    CompanyCreateView, CompanyDetailView, CompanyListView, CompanyUpdateView,
    DeleteCompany)
from .logoutmodal import LogOutModalView
from .partner import (
    CustomerListView, DeletePartner, PartnerAutoComplete, PartnerCreateView,
    PartnerDetailView, PartnerUpdateView, ProviderListView)
from .passwordchange import cambio_clave
from .passwordreset import PasswordRecoveryView
from .profile import ProfileView
from .signup import SignUpView

ChangePasswordView = cambio_clave


def Apps(request):
    return render(request, 'base/apps.html')

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
def UpdateApps(self):
    FILE_NAME = 'info.json'
    folder_apps = '{}/apps'.format(settings.BASE_DIR)
    list_app = listdir(folder_apps)
    PyApp.objects.all().delete()
    for folder in list_app:
        try:
            for file in listdir(folder_apps + "/" + folder):
                if file == FILE_NAME:
                    with open(folder_apps + "/" + folder + "/" + FILE_NAME) as json_file:
                        data = json.load(json_file)
                        p = PyApp(name=data['name'], description=data['description'], author=data['author'],
                                  fa=data['fa'], version=data['version'],
                                  website=data['website'], color=data['color'])
                        p.save()
        except Exception:
            continue

    return redirect(reverse('base:apps'))


# def InstallPyERP(self):
#     count_pw = BaseConfig.objects.all().count()
#     if count_pw > 0:
#         print("=== Ya Instalado ====")
#     else:
#         print("=== Se Instalo ====")
#         PyWebsiteConfig().save()
#         BaseConfig().save()
#         PyCompany().save()

#     return redirect(reverse('base:login'))



@login_required(login_url="base:login")
def InstallApps(self, pk):
    plugin = PyApp.objects.get(id=pk)
    plugin.installed = True
    with open('installed_apps.py', 'a+') as installed_apps_file:
        if installed_apps_file.write('apps.{}\n'.format(plugin.name.lower())):
            print('yes')
        else:
            print("no")

    # Como no se cargar una sola app, se leen todas las app que estan
    # como plugins en tiempo de ejecución al instalar cualquier app
    with open('%s/installed_apps.py' % BASE_DIR, 'r') as ins_apps_file:
        for line in ins_apps_file.readlines():
            settings.INSTALLED_APPS += (line.strip().rstrip('\n'), )

    apps.app_configs = OrderedDict()
    apps.apps_ready = apps.models_ready = apps.loading = apps.ready = False
    apps.clear_cache()

    try:
        # Se recargan todas las aplicaciones ¿como cargar solo una?
        apps.populate(settings.INSTALLED_APPS)
    except:
        # plugin.installed = False
        print('Fallo el proceso de poblado de la app')

    try:
        # Se contruyen las migraciones del plugin
        call_command('makemigrations', plugin.name.lower(), interactive=False)
    except:
        # plugin.installed = False
        print('No hay migración de la app')

    try:
        # Se ejecutan las migraciones de la app
        call_command('migrate', plugin.name.lower(), interactive=False)
    except:
        # plugin.installed = False
        print('No se migro la app')

    try:
        # Se ejecutan las migraciones de la app
        call_command('loaddata', '{}.json'.format(plugin.name.lower()), interactive=False)
    except:
        # plugin.installed = False
        print('No se cargaron datos de la app')

    plugin.save()


    # subprocess.run[PROJECT_RELOAD]
    # Recargo en memoria la rutas del proyecto
    urlconf = settings.ROOT_URLCONF
    if urlconf in sys.modules:
        clear_url_caches()
        reload(sys.modules[urlconf])

    return redirect(reverse('base:apps'))


@login_required(login_url="base:login")
def UninstallApps(self, pk):
    app = PyApp.objects.get(id=pk)
    app.installed = False
    app.save()
    app_lists = []
    with open('installed_apps.py', 'r') as installed_apps_file:
        app_lists = installed_apps_file.readlines()
    with open('installed_apps.py', 'w+') as installed_apps_file:
        for line in app_lists:
            if 'apps.%s' % app.name.lower() == line.strip():
                continue
            installed_apps_file.write(line)
    return redirect(reverse('base:apps'))


@login_required(login_url="base:login")
def erp_home(request):
    """Vista para renderizar el dasboard del erp
    """
    count_app = PyApp.objects.all().count()

    apps = PyApp.objects.all().filter(installed=True).order_by('sequence')
    app_list = []
    if apps:
        for app in apps:
            st = app.name + "/menu.html"
            app_list.append(st.lower())

    partners = PyPartner.objects.all()
    return render(request, "home.html", {
        'customers': partners.filter(customer=True),
        'providers': partners.filter(provider=True),
        'users': PyUser.objects.all(),
        'products': PyProduct.objects.all(),
        'app_list': app_list,
        'count_app': count_app
    })
