from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView

from SpeedApp.cars.forms import CarCreateForm, CarDetailForm, CarEditForm, CarDeleteForm
from SpeedApp.cars.models import Car
from SpeedApp.utils import get_user_obj


class CataloguePageView(ListView):
    model = Car
    template_name = 'catalogue.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class CarCreateView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'car/car-create.html'
    success_url = reverse_lazy('catalogue')
    
    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class CarEditView(UpdateView):
    model = Car
    form_class = CarEditForm
    pk_url_kwarg = 'id'
    template_name = 'car/car-edit.html'
    success_url = reverse_lazy('catalogue')


class CarDetailView(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'car/car-details.html'


class CarDeleteView(DeleteView):
    model = Car
    form_class = CarDeleteForm
    pk_url_kwarg = 'id'
    template_name = 'car/car-delete.html'
    success_url = reverse_lazy('catalogue')

    def get_initial(self):
        return self.get_object().__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


