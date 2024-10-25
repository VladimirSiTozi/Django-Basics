from django.contrib import admin

from MusicApp.albums.models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'artist', 'genre', 'price', 'owner')
