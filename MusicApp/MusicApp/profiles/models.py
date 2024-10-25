from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from MusicApp.profiles.validators import ProfileNameValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            ProfileNameValidator(),
        ]
    )

    email = models.EmailField()

    age = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.username
