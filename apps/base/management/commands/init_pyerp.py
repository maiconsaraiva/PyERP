"""Inicialización de PyERP
"""

# Librerias Standard
import json
from os import listdir

# Librerias Django
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _

# Librerias de terceros
from apps.base.models import (
    PyApp, PyCountry, PyCurrency, PyParameter, PyUser, PyWParameter)


class Command(BaseCommand):
    """Clase para inicialización de PyERP
    """
    help = (
        _("Command to initialize PyErp")
    )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.MIGRATE_HEADING(_('*** Generating base migrations...'))
        )
        call_command('makemigrations', 'base', interactive=False)

        self.stdout.write(
            self.style.MIGRATE_HEADING(_('*** Migrating the base database...'))
        )
        call_command('migrate', interactive=False)

        self.stdout.write(
            self.style.MIGRATE_HEADING(
                _('*** Loading PypErp country object...')
            )
        )
        if not PyCountry.objects.all().exists():
            call_command('loaddata', 'PyCountry')

        self.stdout.write(
            self.style.MIGRATE_HEADING(
                _('*** Loading PypErp currency object...')
            )
        )
        if not PyCurrency.objects.all().exists():
            call_command('loaddata', 'PyCurrency')

        self.stdout.write(
            self.style.MIGRATE_HEADING(
                _('*** Loading PypErp backend parameters object...')
            )
        )
        PyParameter.objects.get_or_create(
            name='mail_catchall_alias',
            value='catchall'
        )
        self.stdout.write('Installed 1 object(s)')

        self.stdout.write(
            self.style.MIGRATE_HEADING(
                _('*** Loading PypErp web parameter object...')
            )
        )
        PyWParameter.objects.get_or_create(
            name='register_user',
            value='True'
        )
        self.stdout.write('Installed 1 object(s)')

        self.stdout.write(
            self.style.SUCCESS('PyErp has been successfully installed. Run ') +
            self.style.MIGRATE_LABEL('python manage.py runserver ') +
            self.style.SUCCESS('to start the development server.')
        )

        self.stdout.write(
            self.style.MIGRATE_HEADING(
                _('*** Loading PypErp plugins library...')
            )
        )
        if not PyApp.objects.all().exists():
            FILE_NAME = 'info.json'
            folder_apps = '{}/apps'.format(settings.BASE_DIR)
            list_app = listdir(folder_apps)
            app_counnter = 0
            for folder in list_app:
                try:
                    for file in listdir(folder_apps + "/" + folder):
                        if file == FILE_NAME:
                            app_counnter += 1
                            with open(folder_apps + "/" + folder + "/" + FILE_NAME) as json_file:
                                data = json.load(json_file)
                                app_obj = PyApp(
                                    name=data['name'],
                                    description=data['description'],
                                    author=data['author'],
                                    fa=data['fa'],
                                    version=data['version'],
                                    website=data['website'], color=data['color']
                                )
                                app_obj.save()
                except Exception:
                    continue
            self.stdout.write('Loaded {} plugin(s)'.format(app_counnter))
