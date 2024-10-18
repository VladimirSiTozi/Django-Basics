from datetime import datetime

from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import classonlymethod
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView, FormView, CreateView, DeleteView, UpdateView

from forumApp.posts.forms import PersonForm, PostForm, PostDeleteForm, SearchForm, PostEditForm, CommentFormSet, \
    PostCreateForm
from forumApp.posts.models import Post, Comment


# Create your views here.

class BaseView:
    @classonlymethod
    def as_view(cls):

        def view(request, *args, **kwargs):
            view_instance = cls()
            return view_instance.dispatch(request, *args, **kwargs)

        return view

    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            return self.get(request, *args, **kwargs)
        elif request.method == "POST":
            return self.post(request, *args, **kwargs)


# Built in Django View
class IndexView(TemplateView):
    template_name = 'common/index.html'  # static way
    extra_context = {
        'static_time': datetime.now()
    }  # static way

    def get_context_data(self, **kwargs):  # dynamic way
        context = super().get_context_data(**kwargs)

        context['dynamic_time'] = datetime.now()

        return context

    def get_template_names(self):  # dynamic way
        if self.request.user.is_authenticated:
            return ['common/index_logged_in.html']
        else:
            return ['common/index.html']


# Class base view
class Index(View):
    def get(self, request, *args, **kwargs):
        context = {
            "dynamic_time": datetime.now(),
        }

        return render(request, 'common/index.html', context)


# Function base view
# def index(request):
#     post_form = modelform_factory(
#         Post,
#         fields=('title', 'content', 'author', 'languages')
#     )
#
#     context = {
#         "my_form": post_form,
#     }
#
#     return render(request, 'common/index.html', context)


class RedirectHomeView(RedirectView):
    url = reverse_lazy()  # static way

    # def get_redirect_url(self, *args, **kwargs):  # dynamic way
    #     # my logic, return redirect url
    #     pass


class DashboardView(ListView, FormView):
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'  # or by default - objects_list or post_list
    form_class = SearchForm
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        queryset = Post.objects.all()

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')
            queryset = queryset.filter(title__icontains=query)

        return queryset


# def dashboard(request):
#     form = SearchForm(request.GET)
#     posts = Post.objects.all()
#
#     if request.method == 'GET':
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             posts = posts.filter(title__icontains=query)
#
#     context = {
#         'posts': posts,
#         'form': form,
#     }
#
#     return render(request, 'posts/dashboard.html', context)


class AddPostView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/add-post.html'
    success_url = reverse_lazy('dashboard')


# def add_post(request):
#     form = PostForm(request.POST or None, request.FILES or None)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'posts/add-post.html', context)


class DeleteFormView(DeleteView, FormView, ):
    model = Post
    template_name = 'posts/delete-post.html'
    form_class = PostDeleteForm
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = Post.objects.get(pk=pk)
        return post.__dict__


# def delete_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#
#     form = PostDeleteForm(instance=post)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('dashboard')
#
#     context = {
#         'form': form,
#         'post': post
#     }
#
#     return render(request, 'posts/delete-post.html', context)


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


class EditPostView(UpdateView):
    model = Post
    template_name = 'posts/edit-post.html'
    # form_class = PostEditForm
    success_url = reverse_lazy('dashboard')

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Post, fields=('title', 'content', 'author', 'languages'))
        else:
            return modelform_factory(Post, fields=('content',))

# def edit_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#
#     if request.method == 'POST':
#         form = PostEditForm(request.POST, instance=post)
#
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#
#     else:
#         form = PostEditForm(instance=post)
#
#     context = {
#         'form': form,
#         'post': post
#     }
#
#     return render(request, 'posts/edit-post.html', context)


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