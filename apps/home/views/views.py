# Librerias Future
from __future__ import unicode_literals

# Librerias Django
from django.core import serializers
from django.core.mail import EmailMessage
from django.shortcuts import HttpResponse, render
from django.template.loader import render_to_string
from django.views.generic import DetailView, ListView, TemplateView

# Librerias de terceros
from apps.base.models import PyWParameter, PyPartner, PyProduct

# from apps.crm.submodels.lead import PyLead


class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        web_parameter = {}
        for parametro in PyWParameter.objects.all():
            web_parameter[parametro.name] = parametro.value

        context['web_parameter'] = web_parameter

        return context



def index(request):
    web_parameter = {}
    for parametro in PyWParameter.objects.all():
        web_parameter[parametro.name] = parametro.value

    request.session['web_parameter'] = web_parameter
    # context['web_parameter'] = web_parameter

    return render(request, 'home/index.html', web_parameter)

def post(request):
    return render(request, 'home/post.html')

def license(request):
    return render(request, 'home/license.html')

def UnderConstruction(request):
    return render(request, 'home/under_construction.html')


def contact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    message = request.POST.get('message')
    partners = PyPartner.objects.filter(email=email)
    send = True
    if partners:
        partner = partners[0]
        if partner.not_email:
            send = False
    else:
        partner = PyPartner(name=name, email=email, phone=phone)
        partner.save()

    if send:
        title = name
        # lead = PyLead(name=title, content=message, partner_id=partner)
        # lead.save()
        body = render_to_string('home/contact_mail_template.html', {'name': name, 'phone': phone, 'message': message})
        email_message = EmailMessage(subject='Mensaje de usuario', body=body, from_email=email, to=['mfalcon@ynext.cl'])
        email_message.content_subtype = 'html'
        email_message.send()
        return HttpResponse(content='OK')
