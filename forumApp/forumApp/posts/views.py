from datetime import datetime

from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect

from forumApp.posts.forms import PersonForm, PostForm, PostDeleteForm, SearchForm, PostEditForm, CommentFormSet
from forumApp.posts.models import Post, Comment


# Create your views here.

def index(request):
    post_form = modelform_factory(
        Post,
        fields=('title', 'content', 'author', 'languages')
    )

    context = {
        "my_form": post_form,
    }

    return render(request, 'common/index.html', context)


def dashboard(request):
    form = SearchForm(request.GET)
    posts = Post.objects.all()

    if request.method == 'GET':
        if form.is_valid():
            query = form.cleaned_data['query']
            posts = posts.filter(title__icontains=query)

    context = {
        'posts': posts,
        'form': form,
    }

    return render(request, 'posts/dashboard.html', context)


def add_post(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'posts/add-post.html', context)


def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)

    form = PostDeleteForm(instance=post)

    if request.method == 'POST':
        post.delete()
        return redirect('dashboard')

    context = {
        'form': form,
        'post': post
    }

    return render(request, 'posts/delete-post.html', context)


def details_page(request, pk: int):
    post = Post.objects.get(pk=pk)
    formset = CommentFormSet(request.POST or None)
    comments = Comment.objects.filter(post_id=post.id)

    if request.method == 'POST':
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect('details-post', pk=post.id)

    context = {
        'post': post,
        'formset': formset,
        'comments': comments,
    }

    return render(request, 'posts/details-post.html', context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = PostEditForm(instance=post)

    context = {
        'form': form,
        'post': post
    }

    return render(request, 'posts/edit-post.html', context)


def old_examples(request):
    form = PersonForm(request.POST or None)

    if request.method == 'POST':
        print(request.POST['person_name'])

    if form.is_valid():
        print(form.cleaned_data['person_name'])

    context = {
        'current_time': datetime.now(),
        'person': {
            'name': 'Vlado',
            'age': 20,
        },
        'ids': ['2134687124', 'nd9u31das', '23das23'],
        'some_text': """The Danube is the second-longest river in Europe, after the Volga in Russia. It flows through 
                             Central and Southeastern Europe, from the Black Forest south into the Black Sea. A large and 
                             historically important river, it was once a frontier of the Roman Empire. In the 21st century, 
                             it connects ten European countries, running through their territories or marking a border. 
                             Originating in Germany, the Danube flows southeast for 2,850 km (1,770 mi), passing through or 
                             bordering Austria, Slovakia, Hungary, Croatia, Serbia, Romania, Bulgaria, Moldova, and Ukraine. 
                             Among the many cities on the river are four national capitals: Vienna, Bratislava, Budapest, 
                             and Belgrade. Its drainage basin amounts to 817,000 km2 (315,000 sq mi) and extends into 
                             nine more countries.""",
        'some_text2': 'hello i am ali baba',
        'empty_text': '',
        'names_list': ['Antony', 'Rashford', 'Fernandes', 'CR7', 'Messi10'],
        'empty_list': [],
        'posts': [
            {
                'title': 'How to create Django project',
                'author': 'Dido',
                'content': "I **really** <i>don't know</i> how to create django project.... Just kidding :D",
                'created_at': datetime.now()
            },
            {
                'title': 'How to create Django project 1',
                'author': '',
                'content': "I really don't know how to create django project.... Just kidding :D",
                'created_at': datetime.now()
            },
            {
                'title': 'How to create Django project 2',
                'author': 'Ivan Ivanov',
                'content': "",
                'created_at': datetime.now()
            },

        ],

        # Person Form
        "my_form": form,

    }

    return render(request, 'posts/old-examples.html', context)