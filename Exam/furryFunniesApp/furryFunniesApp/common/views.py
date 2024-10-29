from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from furryFunniesApp.posts.models import Post


class HomePageView(TemplateView):
    template_name = 'index.html'


class DashboardView(ListView):
    model = Post
    template_name = 'dashboard.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
