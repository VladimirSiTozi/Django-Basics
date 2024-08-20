import time

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse(f"Response from {time.time()}")


def department_details(request, pk):
    return HttpResponse(f"<h1>Department with id #{pk}</h1>")


def department_details_by_name(request, name):
    return HttpResponse(f"<h1>Department with name: {name}</h1>")