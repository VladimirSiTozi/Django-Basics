from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.

def index(request, *args, **kwargs):
    content = (f'<h1>If it works</h1><br/> '
               f'args={args}and kwargs={kwargs}<br/> '
               f'from path {request.path}<br/> '
               f'method={request.method}<br/> '
               f'user={request.user}')

    return HttpResponse(
        content,
        # content_type="application/json"
        # status=201
    )


def index_json(request, *args, **kwargs):
    content = {
        'args': args,
        'kwargs': kwargs,
        'path': request.path,
        'method': request.method,
        'user': str(request.user)
    }

    return JsonResponse(
        content,
        # content_type="application/json",
        safe=False
        # status=201
    )


def index_with_template(request, *args, **kwargs):
    content = {
        'title': "Requested data",
        'args': args,
        'kwargs': kwargs,
        'path': request.path,
        'method': request.method,
        'user': request.user
    }
    return render(request, 'core/index.html', content)


def redirect_to_google(request, *args, **kwargs):
    return redirect('https://www.google.co.uk/')


def redirect_to_index(request):
    return redirect('index_no_params')


def redirect_to_index_with_params(request):
    return redirect('index_with_pk_and_slug', pk=19, slug='Gosha')