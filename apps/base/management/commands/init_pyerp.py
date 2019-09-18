"""Inicialización de PyERP
"""

import subprocess

import sys

from django.utils import timezone

from django.core.management import call_command

from django.core.management.base import BaseCommand, CommandError


from django.utils.translation import ugettext_lazy as _

from apps.base.models import PyCountry, PyCurrency


# ======================= Generating base migrations ======================= #

class Command(BaseCommand):
    """Clase para inicialización de PyERP
    """
    help = (
        _("Command to initialize PyErp")
    )

    def handle(self, *args, **options):
        self.stdout.write(_('*** Generating base migrations...'))
        call_command('makemigrations', 'base', interactive=False)

        self.stdout.write(_('*** Migrating the base databases...'))
        call_command('migrate', interactive=False)

        self.stdout.write(_('*** Loading PypErp country objects ...'))
        if not PyCountry.objects.all().exists():
            call_command('loaddata', 'PyCountry')

        self.stdout.write(_('*** Loading PypErp currency objects ...'))
        if not PyCurrency.objects.all().exists():
            call_command('loaddata', 'PyCurrency')
