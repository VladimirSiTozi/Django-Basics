from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.db.models import Sum
from django.shortcuts import render

from SpeedApp.profiles.validators import ProfileNameValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(limit_value=3, message='Username must be at least 3 chars long!'),
            ProfileNameValidator(),
        ]
    )

    email = models.EmailField()

    age = models.IntegerField(
        validators=[
            MinValueValidator(21),
        ]
    )

    password = models.CharField(
        max_length=20,
    )

    first_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )
