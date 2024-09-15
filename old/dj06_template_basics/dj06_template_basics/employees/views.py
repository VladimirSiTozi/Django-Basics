import datetime

from django.shortcuts import render


# Create your views here.

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


def index(request):
    context = {
        'title': 'Employees list',
        'person': {
            'first_name': 'Valeto',
            'last_name': 'D'
        },
        'person_obj': Person('Vlado', 'S', None),

        'names': ['Maria', 'Ivana', 'Ekaterina'],
        'ages': [10, 20, 30, 40, 50, 60],
        'names_empty': [],

        'date': datetime.date.today(),
        'get_params': request.GET,

    }

    return render(request, 'employees/index.html', context)


def employee_details(request, pk):
    context = {
        'pk': pk
    }
    return render(request, 'employees/details.html', context)
