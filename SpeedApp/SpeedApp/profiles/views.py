from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from SpeedApp.profiles.forms import ProfileCreateForm, ProfileEditForm
from SpeedApp.profiles.models import Profile
from SpeedApp.utils import get_user_obj


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/profile-create.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        return super().form_valid(form)


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile/profile-edit.html'
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDetailView(DetailView):
    template_name = 'profile/profile-details.html'

    def get_object(self, queryset=None):
        return get_user_obj()
