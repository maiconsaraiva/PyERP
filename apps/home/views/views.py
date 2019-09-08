# Librerias Future
from __future__ import unicode_literals

# Librerias Django
from django.core.mail import EmailMessage
from django.shortcuts import HttpResponse, render
from django.template.loader import render_to_string
from django.views.generic import DetailView, ListView

# Librerias de terceros
from apps.base.models import PyPartner, PyProduct

# Librerias en carpetas locales
# from apps.crm.submodels.lead import PyLead
from ..models.post import PyPost


def index(request):
    return render(request, 'index.html')

def post(request):
    return render(request, 'post.html')

def license(request):
    return render(request, 'license.html')

def UnderConstruction(request):
    return render(request, 'under_construction.html')


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

"""
BLOG
"""

POST_FIELDS = [
            {'string': 'Título', 'field': 'title'},
            {'string': 'Creado en', 'field': 'created_on'},
            {'string': 'Contenido', 'field': 'content'},
        ]

POST_FIELDS_SHORT = ['title','content','created_on']

class BlogView(ListView):
    model = PyPost
    template_name = 'blog.html'
    fields = POST_FIELDS
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostDetailView(DetailView):
    model = PyPost
    template_name = 'post.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



# Tienda de Productos

PRODUCT_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Descripción', 'field': 'description'},
            {'string': 'Precio', 'field': 'price'},
            {'string': 'Activo', 'field': 'web_active'},
            {'string': 'Código', 'field': 'code'},
            {'string': 'Código Barra', 'field': 'code'},
        ]

class WebProductView(ListView):
    model = PyProduct
    template_name = 'shop.html'
    fields = PRODUCT_FIELDS
    paginate_by = 8
    queryset = PyProduct.objects.filter(web_active='True')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class WebProductDetailView(DetailView):
    model = PyProduct
    template_name = 'product.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
