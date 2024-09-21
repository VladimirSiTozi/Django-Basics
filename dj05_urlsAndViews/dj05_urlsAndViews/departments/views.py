from django.http import HttpResponse, JsonResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from dj05_urlsAndViews.departments.models import Department


# Create your views here.

def index(request):
    url = reverse('redirect-home')
    url_lazy = reverse_lazy('redirect-home')
    return HttpResponse(f'<h1>{url_lazy}</h1>')


def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f'<h1>Args: {args}, Kwargs: {kwargs}</h1>')


def view_with_name(request, variable):
    # return HttpResponse(f'<h1>Variable: {variable}</h1>')

    context = {
        'variable': variable
    }
    return render(request, 'departments/name_template.html', context)


def view_with_int_pk(request, pk):
    # return HttpResponse(f'<h1>Int pk with pk: {pk}</h1>', content_type="application/json")  # May return different types
    return JsonResponse({"pk": pk})  # option 2 make same thing abstract


def view_with_slug(request, pk, slug):
    # OPTION 1
    # department = Department.objects.filter(pk=pk, slug=slug)
    #
    # if not department:
    #     raise Http404

    # OPTION 2
    department = get_object_or_404(Department, pk=pk, slug=slug)

    # OPTION 3
    return HttpResponseNotFound()

    # OPTION 4
    # return HttpResponse(status=404)

    # OPTION 2
    # return HttpResponse(f'<h1>Department: {department}, with Slug: {slug}</h1>')


def show_archive(request, archive_year):
    return HttpResponse(f'<h1>The year is: {archive_year}</h1>')


def redirect_to_softuni(request):
    return redirect('https://softuni.bg/')


def redirect_to_home(request):
    # OPTION 1, breaks abstraction
    # return redirect('http://127.0.0.1:8000')

    # OPTION 2, not optimal as well, breaks single responsibility if view is from another app
    # return redirect(index)

    # OPTION 3 - "NAMING" - The best way
    return redirect('home')


def redirect_to_numbers(request, pk):
    return redirect('numbers', pk=pk)

