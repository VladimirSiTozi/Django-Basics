from django.urls import path

from petstagram_demo.common.views import index

urlpatterns = (
    path('', index, name='index'),
)