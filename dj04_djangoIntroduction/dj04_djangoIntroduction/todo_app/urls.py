from django.urls import path

from dj04_djangoIntroduction.todo_app.views import index

urlpatterns = [
     path('', index),
]