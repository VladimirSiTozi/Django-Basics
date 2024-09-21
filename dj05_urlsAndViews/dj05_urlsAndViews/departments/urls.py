from django.urls import path, re_path, include
from dj05_urlsAndViews.departments import views

urlpatterns = [
    path('', views.index, name='home'),
    path('redirect-to-home/', views.redirect_to_home, name='redirect-home'),
    path('softuni/', views.redirect_to_softuni),
    path('numbers/', include([
        path('<int:pk>/', views.view_with_int_pk, name='numbers'),
        path('<int:pk>/<slug:slug>/', views.view_with_slug),
    ])),

    re_path(r'^archive/(?P<archive_year>202[0-3])/$', views.show_archive),
    path('<variable>/', views.view_with_name),
    path('<path:variable>/', views.view_with_name),

    # path('<uuid>:id', some_view)
    # path('<param>/', views.view_with_args_and_kwargs),

]






