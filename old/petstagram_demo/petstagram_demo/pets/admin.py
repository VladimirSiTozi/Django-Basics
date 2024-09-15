from django.contrib import admin

from petstagram_demo.pets.models import Pet


# Register your models here.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'slug')