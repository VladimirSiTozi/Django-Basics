from django.shortcuts import render
from django.views.generic import TemplateView

from SpeedApp.cars.models import Car


class HomePageView(TemplateView):
    template_name = 'index.html'




