from django.core.validators import MinValueValidator
from django.db import models

from MusicApp.albums.choices import GenreChoice


class Album(models.Model):
    album_name = models.CharField(
        unique=True,
        max_length=30,
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=GenreChoice.choices
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    img_url = models.URLField()

    price = models.FloatField(
        validators=[
            MinValueValidator(0.0)
        ]
    )

    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='albums',
    )

    def __str__(self):
        return self.album_name
