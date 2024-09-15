from django.shortcuts import render

from dj04_djangoIntroduction.todo_app.models import Task


# Create your views here.

def index(request):
    # if no match ''
    title_filter = request.GET.get('title_filter', '')

    tasks = Task.objects.filter(name__icontains=title_filter)

    context = {
        'title_filter': title_filter,
        'tasks': tasks,
    }

    # result = '\n'.join([
    #     '<h1>TASKS</h1>',
    #     '<ul>',
    #     *[f'<li>{task.name} - {task.description} - {task.created_at}</li>'for task in tasks],
    #     '</ul>',
    # ])

    return render(request, 'tasks/index.html', context)

