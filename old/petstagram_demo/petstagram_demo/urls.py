from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram_demo.common.urls')),
    path('accounts/', include('petstagram_demo.accounts.urls')),
    path('pets/', include('petstagram_demo.pets.urls')),
    path('photos/', include('petstagram_demo.photos.urls')),
]
