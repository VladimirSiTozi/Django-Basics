from django.urls import path

from furryFunniesApp.common.views import HomePageView, DashboardView

urlpatterns = [
    path('', HomePageView.as_view(), name='home-index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
