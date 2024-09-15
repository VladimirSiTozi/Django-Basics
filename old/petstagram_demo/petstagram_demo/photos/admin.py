from django.contrib import admin

from petstagram_demo.photos.models import PetPhoto


# Register your models here.

@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ('photo', 'description', 'created_at', 'modified_at')
