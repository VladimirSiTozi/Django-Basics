import http.client
from django import http
from django.db.models import Q
from django.http import HttpResponse

from django.shortcuts import render

from django101.tasks.models import Tasks


# Create your views here.

# def index(request):
#     name = request.GET.get('name', 'NONAME')
#
#     content = "<h1>It works</h1>" + \
#               f"<p>Welcome the to my project, {name}</p>" + \
#               "<ul><li>1</li><li>2</li></ul>"
#
#     return http.HttpResponse(content)


# def index(request):
#     query_filter = request.GET.get('filter', '')
#
#     tasks = Tasks.objects.all()
#
#     if filter:
#         tasks = tasks.filter(Q(description__icontains=query_filter) | Q(title__icontains=query_filter))
#
#     if not tasks:
#         return HttpResponse("<h1>No Tasks!!!</h1>")
#
#     result = []
#     for task in tasks:
#         result.append(f"""
#         <li>
#             <h2>{task.title}</h2>
#             <p>{task.description}</p>
#         </li>
#         """)
#
#         ul = f"<ul>{''.join(result)}</ul>"
#
#         content = f"""
#         <h1>{len(tasks)} Tasks</h1>
#         {ul}
#         """
#         return HttpResponse(content)


def index(request):
    print('In the view')
    title_filter = request.GET.get('title_filter', '')

    tasks = Tasks.objects.all()

    if title_filter:
        tasks = tasks.filter(Q(description__icontains=title_filter) | Q(title__icontains=title_filter))

    context = {
        'title': 'The tasks app!',
        'task_list': tasks,
        'task_list_count': tasks.count(),
        'title_filter': title_filter,
    }
    return render(request, 'tasks/index.html', context)
