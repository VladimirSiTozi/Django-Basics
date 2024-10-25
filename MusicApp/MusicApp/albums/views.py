from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from MusicApp.albums.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from MusicApp.albums.models import Album
from MusicApp.utils import get_user_obj


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class AlbumEditView(UpdateView):
    model = Album
    form_class = AlbumEditForm
    pk_url_kwarg = 'id'
    template_name = 'albums/album-edit.html'
    success_url = reverse_lazy('home')


class AlbumDetailsView(DetailView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'albums/album-details.html'


class AlbumDeleteView(DeleteView):
    model = Album
    form_class = AlbumDeleteForm
    pk_url_kwarg = 'id'
    template_name = 'albums/album-delete.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        return self.get_object().__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


