from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from furryFunniesApp.authors.forms import AuthorCreateForm, AuthorEditForm
from furryFunniesApp.authors.models import Author
from furryFunniesApp.utils import get_user_obj


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'authors/create-author.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        return super().form_valid(form)


class AuthorDetailsView(DetailView):
    template_name = 'authors/details-author.html'

    def get_object(self, queryset=None):
        return get_user_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_post'] = self.object.posts.order_by('-updated_at').first()
        return context


class AuthorEditView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'authors/edit-author.html'
    success_url = reverse_lazy('author-details')

    def get_object(self, queryset=None):
        return get_user_obj()


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('home-index')

    def get_object(self, queryset=None):
        return get_user_obj()
