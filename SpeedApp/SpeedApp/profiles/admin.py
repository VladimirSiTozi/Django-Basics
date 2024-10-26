from django.contrib import admin

from SpeedApp.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'age', 'first_name', 'last_name')
