# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from dal import autocomplete

# Localfolder Library
from ..models import PyPartner
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Street"), 'field': 'street'},
    {'string': _("Country"), 'field': 'country_id'},
    {'string': _("Phone"), 'field': 'phone'},
    {'string': _("Email"), 'field': 'email'},
    {'string': _("For Invoice"), 'field': 'for_invoice'},
    {'string': _("Note"), 'field': 'note'},
    {'string': _("No Email"), 'field': 'not_email'},
    {'string': _("Parent"), 'field': 'parent_id'},
    {'string': _("Type"), 'field': 'type'},
]

OBJECT_FORM_FIELDS = [
    'name',
    'img',
    'street',
    'country_id',
    'email',
    'phone',
    'note',
    'customer',
    'provider',
    'for_invoice',
    'not_email',
    'parent_id',
    'type',
    'active'
]


# ========================================================================== #
class CustomerListView(LoginRequiredMixin, FatherListView):
    model = PyPartner
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


# ========================================================================== #
class ProviderListView(LoginRequiredMixin, FatherListView):
    model = PyPartner
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}
    queryset = PyPartner.objects.filter(provider=True, active=True).all()


# ========================================================================== #
class PartnerCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyPartner
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


# ========================================================================== #
class PartnerDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyPartner
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


# ========================================================================== #
class PartnerUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyPartner
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


# ========================================================================== #
class PartnerDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyPartner


# ========================================================================== #
class PartnerAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo PyPartner
    """
    def get_queryset(self):
        queryset = PyPartner.objects.all()
        if self.q:
            queryset = queryset.filter(name__icontains=self.q, active=True)
        return queryset
