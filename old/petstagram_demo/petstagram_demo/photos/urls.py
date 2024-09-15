from django.urls import path, include

from petstagram_demo.photos.views import create_photo, details_photo, edit_photo

urlpatterns = (
    path('add/', create_photo, name='create photo'),
    path('<int:pk>/', include([
        path('', details_photo, name='details photo'),
        path('edit/', edit_photo, name='edit photo')
    ]))
)