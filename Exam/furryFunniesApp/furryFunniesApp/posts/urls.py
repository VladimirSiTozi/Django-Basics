from django.urls import path, include

from furryFunniesApp.posts import views

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('<int:id>/', include([
        path('details/', views.PostDetailsView.as_view(), name='post-details'),
        path('edit/', views.PostEditView.as_view(), name='post-edit'),
        path('delete/', views.PostDeleteView.as_view(), name='post-delete')
    ]))
]
