from django.contrib import admin

from django101.tasks.models import Tasks


# Register your models here.

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('title', 'description')

