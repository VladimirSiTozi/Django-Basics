from django.contrib.sitemaps.views import index
from django.urls import path

from dj05_urls_and_view.department.views import department_details, department_details_by_name

urlpatterns = [
    path('departments/<int:pk>/', department_details),
    path('departments/<str:name>/', department_details_by_name),

]