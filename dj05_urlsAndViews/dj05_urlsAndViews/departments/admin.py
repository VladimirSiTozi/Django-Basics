from django.contrib import admin

from dj05_urlsAndViews.departments.models import Department


# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
