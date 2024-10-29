from django.urls import path, include

from furryFunniesApp.authors import views

urlpatterns = [
    path('create/', views.AuthorCreateView.as_view(), name='author-create'),
    path('details/', views.AuthorDetailsView.as_view(), name='author-details'),
    path('edit/', views.AuthorEditView.as_view(), name='author-edit'),
    path('delete/', views.AuthorDeleteView.as_view(), name='author-delete'),
]
