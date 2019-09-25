# Librerias Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyLog
from ..models import PyFaq
from .web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView)

FAQ_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Content"), 'field': 'content'},
]

FAQ_SHORT = ['name', 'content']


class FaqListView(LoginRequiredMixin, FatherListView):
    model = PyFaq
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(FaqListView, self).get_context_data(**kwargs)
        context['title'] = 'Faqs'
        context['detail_url'] = 'base:faq-detail'
        context['add_url'] = 'base:faq-add'
        context['fields'] = FAQ_FIELDS
        return context


class FaqDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyFaq
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(FaqDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:faqs', 'name': 'Faqs'}]
        context['update_url'] = 'base:faq-update'
        context['delete_url'] = 'base:faq-delete'
        context['fields'] = FAQ_FIELDS
        return context


class FaqCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyFaq
    fields = FAQ_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(FaqCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Faq'
        context['breadcrumbs'] = [{'url': 'base:faqs', 'name': 'Faqs'}]
        context['back_url'] = reverse('base:faqs')
        return context


class FaqUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyFaq
    fields = FAQ_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(FaqUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:faqs', 'name': 'Faqs'}]
        context['back_url'] = reverse('base:faq-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteFaq(self, pk):
    faq = PyFaq.objects.get(id=pk)
    faq.delete()
    return redirect(reverse('base:faqs'))
