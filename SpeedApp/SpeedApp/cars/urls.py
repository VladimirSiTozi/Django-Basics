from django.urls import path, include

from SpeedApp.cars import views

urlpatterns = [
    path('catalogue/', views.CataloguePageView.as_view(), name='catalogue'),
    path('create/', views.CarCreateView.as_view(), name='create-car'),
    path('<int:id>/', include([
        path('edit/', views.CarEditView.as_view(), name='edit-car'),
        path('detail/', views.CarDetailView.as_view(), name='detail-car'),
        path('delete/', views.CarDeleteView.as_view(), name='delete-car'),
    ]))
]