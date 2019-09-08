# Librerias Django
from django.db import models

# Librerias en carpetas locales
from ...crm.submodels.lead import PyLead
from .campaign import PyCampaign
from .channel import PyChannel


class MarketingLead(PyLead):
    class Meta:
        app_label = 'crm'

    channel_id = models.ForeignKey(PyChannel, null=True, blank=True, on_delete=models.CASCADE)
    campaign_id = models.ForeignKey(PyCampaign, null=True, blank=True, on_delete=models.CASCADE)
