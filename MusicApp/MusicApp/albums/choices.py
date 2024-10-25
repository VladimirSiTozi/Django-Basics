from django.db import models


class GenreChoice(models.TextChoices):
    POP = 'Pop', 'Pop'
    JAZZ = 'Jazz', 'Jazz'
    R_AND_B_ = 'R&B', 'R&B'
    ROCK = 'Rock', 'Rock'
    METAL = 'Metal', 'Metal'
    COUNTRY = 'Country', 'Country'
    DANCE_MUSIC = 'Dance Music', 'Dance Music'
    HIP_HOP = 'Hip Hop', 'Hip Hop'
    OTHER = 'Other', 'Other'
