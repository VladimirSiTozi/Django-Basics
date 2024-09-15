from django.shortcuts import render


# Create your views here.

def create_photo(request):
    context = {}
    return render(request, 'photos/create-photo.html', context)


def details_photo(request, pk):
    context = {}
    return render(request, 'photos/details-photo.html', context)


def edit_photo(request, pk):
    context = {}
    return render(request, 'photos/edit-photo.html', context)
