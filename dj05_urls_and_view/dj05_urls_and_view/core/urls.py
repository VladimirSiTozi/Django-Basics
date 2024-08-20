from django.urls import path, include

from dj05_urls_and_view.core.views import index, index_json, index_with_template, redirect_to_google, redirect_to_index

urlpatterns = [
    path('', include([
        path('', index, name='index_no_params'),
        path('<int:pk>', index),
        path('<slug:slug>', index),
        path('to-index-with-params/', index, name='redirect_to_index_with_params'),
        # path('<int:pk>/<slug:slug>', index, name='index_with_pk_and_slug'),
    ]))
    ,

    path('json/', include([
        path('', index_json),
        path('<int:pk>', index_json),
        path('<slug:slug>', index_json),
        path('<int:pk>/<slug:slug>', index_json),
        ])
    ),

    path('template/', include([
        path('', index_with_template),
        path('<int:pk>', index_with_template),
        path('<slug:slug>', index_with_template),
        path('<int:pk>/<slug:slug>', index_with_template),
    ])),

    path('to-google/', redirect_to_google),

    path('to-index/', redirect_to_index, name='redirect_to_index')

]
