# Librerias Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _
from .web_father import FatherDetailView, FatherListView, FatherUpdateView, FatherCreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Librerias en carpetas locales
from ..models.post import PyPost

POST_FIELDS = [
            {'string': _("Title"), 'field': 'title'},
            {'string': _("Created on"), 'field': 'created_on'},
            {'string': _("Keywords"), 'field': 'keywords'},

        ]

POST_FIELDS_SHORT = ['title', 'keywords', 'content', 'img', ]

class PostListView(LoginRequiredMixin, FatherListView):
    model = PyPost
    template_name = 'base/list.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['title'] = 'Entradas'
        context['detail_url'] = 'base:post-detail'
        context['add_url'] = 'base:post-add'
        context['fields'] = POST_FIELDS
        return context

class PostDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyPost
    template_name = 'base/detail.html'
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].title
        context['breadcrumbs'] = [{'url': 'base:post-backend', 'name': 'Entradas'}]
        context['update_url'] = 'base:post-update'
        context['delete_url'] = 'base:post-delete'
        context['fields'] = POST_FIELDS
        return context


class PostCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyPost
    fields = POST_FIELDS_SHORT
    template_name = 'base/form.html'
    success_url = reverse_lazy('base:post-backend')

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Post'
        context['breadcrumbs'] = [{'url': 'base:post-backend', 'name': 'Entrada'}]
        context['back_url'] = reverse('base:post-backend')
        return context


class PostUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyPost
    fields = POST_FIELDS_SHORT
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].title
        context['breadcrumbs'] = [{'url': 'base:post-backend', 'name': 'Entrada'}]
        context['back_url'] = reverse('base:post-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeletePost(self, pk):
    post = PyPost.objects.get(id=pk)
    post.delete()
    return redirect(reverse('base:post-backend'))
