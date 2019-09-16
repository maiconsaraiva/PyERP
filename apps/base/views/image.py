# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..models import PyImage

IMAGE_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Content"), 'field': 'content'},
]

IMAGE_SHORT = ['name', 'content']


class ImageListView(LoginRequiredMixin, ListView):
    model = PyImage
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ImageListView, self).get_context_data(**kwargs)
        context['title'] = 'Images'
        context['detail_url'] = 'base:image-detail'
        context['add_url'] = 'base:image-add'
        context['fields'] = IMAGE_FIELDS
        return context


class ImageDetailView(LoginRequiredMixin, DetailView):
    model = PyImage
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ImageDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:images', 'name': 'Images'}]
        context['update_url'] = 'base:image-update'
        context['delete_url'] = 'base:image-delete'
        context['fields'] = IMAGE_FIELDS
        return context


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = PyImage
    fields = IMAGE_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ImageCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Image'
        context['breadcrumbs'] = [{'url': 'base:images', 'name': 'Images'}]
        context['back_url'] = reverse('base:images')
        return context


class ImageUpdateView(LoginRequiredMixin, UpdateView):
    model = PyImage
    fields = IMAGE_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ImagesUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:images', 'name': 'Images'}]
        context['back_url'] = reverse('base:image-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteImage(self, pk):
    image = PyImage.objects.get(id=pk)
    image.delete()
    return redirect(reverse('base:images'))
