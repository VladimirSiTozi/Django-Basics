from django.shortcuts import render, redirect

from dj07_forms_basics.web.forms import EmployeeForm, EmployeeNormalForm, EmployeeModelForm
from dj07_forms_basics.web.models import Employee


# Create your views here.

def index(request):
    return render(request, 'web/index.html')


def type_of_forms(request):
    return render(request, 'web/type-of-forms.html')


def model_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
    else:  # GET
        form = EmployeeForm()

    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data['first_name'])
            return redirect('index')

    context = {
        'employee_form': form
    }

    return render(request, 'web/model-form.html', context)


# def model_form(request):
#     if request.method == 'GET':
#         context = {
#             'employee_form': EmployeeForm()
#         }
#
#         return render(request, 'web/model-form.html', context)
#
#     else:  # Post
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             # data is valid, populate, 'cleaned_data'
#             print(form.cleaned_data['first_name'])
#             # use data
#             # redirect to some URL
#             return redirect('index')
#         else:
#             context = {
#                 'employee_form': form
#             }
#             # data invalid, populate 'errors'
#             pass
#
#         return render(request, 'web/model-form.html', context)


def index_model(request):
    form = EmployeeModelForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    context = {
        # 'normal_employee_form': EmployeeNormalForm(),
        'model_employee_form': EmployeeModelForm(),
        'employee_list': Employee.objects.all()
    }

    return render(request, 'web/modelform-index.html', context)


def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    form = EmployeeModelForm(request.POST or None, instance=employee)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    context = {
        'form': form,
        'employee': employee
    }
    
    return render(request, 'web/employee_details.html', context)

