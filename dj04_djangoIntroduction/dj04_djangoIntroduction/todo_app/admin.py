from django.contrib import admin

from dj04_djangoIntroduction.todo_app.models import Task


# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
