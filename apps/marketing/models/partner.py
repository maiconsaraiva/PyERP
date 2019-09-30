# Librerias Django
# Django Library
from django.db import models

# Thirdparty Library
# Librerias de terceros
from apps.base.models import PyPartner

# Localfolder Library
# Librerias en carpetas locales
from .campaign import PyCampaign
from .channel import PyChannel


class MarketingPartner(PyPartner):
    class Meta:
        app_label = 'base'

    channel_id = models.ForeignKey(PyChannel, null=True, blank=True, on_delete=models.PROTECT)
    campaign_id = models.ForeignKey(PyCampaign, null=True, blank=True, on_delete=models.PROTECT)
