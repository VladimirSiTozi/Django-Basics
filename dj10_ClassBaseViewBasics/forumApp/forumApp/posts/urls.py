from django.urls import path, include

from forumApp.posts import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('add-post/', views.AddPostView.as_view(), name='add-post'),
    path('<int:pk>/', include([
        path('delete-post/', views.DeleteFormView.as_view(), name='delete-post'),
        path('details-post/', views.details_page, name='details-post'),
        path('edit-post/', views.EditPostView.as_view(), name='edit-post'),
    ])),
    path('old-examples/', views.old_examples, name='old-examples'),
    path('redirect-home/', views.RedirectHomeView.as_view(), name='redirect-home'),
]
