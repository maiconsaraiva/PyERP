# Librerias Django
# Librerias Standard
import csv
import os
from os import listdir, path

from django.conf import settings
from django.db import models


class PyFather(models.Model):
    active = models.BooleanField(default=True, blank=True, null=True)
    fc = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fm = models.DateTimeField(auto_now=True, blank=True, null=True)
    uc = models.IntegerField(null=True, blank=True)
    um = models.IntegerField(null=True, blank=True)
    company_id = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['id']

    class Meta:
        abstract = True

    @classmethod
    def setSequence(cls):
        # return PySequence.objects.get(pk=1).show_chat
        print("Adelantando Sequencia")

    @classmethod
    def LoadData(cls,type,company_id):
        ToModel = cls
        toModelName =  cls.__name__
        app_name = cls._meta.app_label
        folder_apps = format(settings.BASE_DIR) + '/apps/' + format(app_name) + '/' + type
        route_csv = folder_apps + '/'+toModelName+'.csv'
        if os.path.isfile(route_csv):
            with open(route_csv) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    mydic = row
                    lines = ""
                    cont = 0
                    for key, value in mydic.items():
                        cont += 1
                        lines += key + "=" + "'" + value + "'"
                        if cont < len(mydic):
                            lines += ","
                    lines = "ToModel(" + lines
                    lines = lines + ",company_id='" + str(company_id) + "')"
                    # ToModel(title='description',id='2',content='Web')
                    print(lines)
                    lines.replace('"', '')
                    _Model = eval(lines)
                    _Model.save()
        else:
            print('No Existe')
            print(route_csv)
