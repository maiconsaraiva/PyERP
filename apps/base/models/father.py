# Librerias Django
from django.db import models
from os import listdir, path
from django.conf import settings
import csv

class PyFather(models.Model):
    active = models.BooleanField(default=True, blank=True, null=True)
    fc = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fm = models.DateTimeField(auto_now=True, blank=True, null=True)
    uc = models.IntegerField(null=True, blank=True)
    um = models.IntegerField(null=True, blank=True)
    company_id = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True

    def LoadData(app_name, ToModel):
        folder_apps = format(settings.BASE_DIR) + '/apps/' + format(app_name) + '/data'
        for file_csv in listdir(folder_apps):
            route_csv = folder_apps + "/" +file_csv
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
                    lines = "ToModel(" + lines + ")"
                    lines.replace('"','')
                    _Model = eval(lines)
                    _Model.save()
