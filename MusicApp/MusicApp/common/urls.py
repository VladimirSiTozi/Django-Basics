from django.urls import path

from MusicApp.common.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
