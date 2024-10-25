from django.contrib import admin

from MusicApp.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'age',)
