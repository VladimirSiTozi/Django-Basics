from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from furryFunniesApp.posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from furryFunniesApp.posts.models import Post
from furryFunniesApp.utils import get_user_obj


class PostCreateView(CreateView):
    model = Post,
    form_class = PostCreateForm
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)


class PostDetailsView(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'posts/details-post.html'


class PostEditView(UpdateView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'posts/edit-post.html'
    form_class = PostEditForm
    success_url = reverse_lazy('dashboard')


class PostDeleteView(DeleteView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'posts/delete-post.html'
    form_class = PostDeleteForm
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.get_object().__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
