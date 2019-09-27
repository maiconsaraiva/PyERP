# Librerias Django
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyComment
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

COMMENT_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Comment"), 'field': 'comment'},
]

COMMENT_SHORT = ['name', 'comment']


class CommentListView(LoginRequiredMixin, FatherListView):
    model = PyComment
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CommentListView, self).get_context_data(**kwargs)
        context['title'] = 'Comments'
        context['detail_url'] = 'base:comment-detail'
        context['add_url'] = 'base:comment-add'
        context['fields'] = COMMENT_FIELDS
        return context


class CommentDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyComment
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CommentDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:comments', 'name': 'Comments'}]
        context['update_url'] = 'base:comment-update'
        context['delete_url'] = 'base:comment-delete'
        context['fields'] = COMMENT_FIELDS
        return context


class CommentCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyComment
    fields = COMMENT_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Comment'
        context['breadcrumbs'] = [{'url': 'base:comments', 'name': 'Comments'}]
        context['back_url'] = reverse('base:comments')
        return context


class CommentUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyComment
    fields = COMMENT_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CommentUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:comments', 'name': 'Comments'}]
        context['back_url'] = reverse('base:comment-detail', kwargs={'pk': context['object'].pk})
        return context



class CommentDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyComment
    success_url = 'base:comments'
