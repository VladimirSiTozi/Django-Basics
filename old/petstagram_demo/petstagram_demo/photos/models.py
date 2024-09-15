from django.core.validators import MinLengthValidator
from django.db import models

from petstagram_demo.pets.models import Pet


# Create your models here.

class PetPhoto(models.Model):
    photo = models.ImageField(
        upload_to='pet_photos/',
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=300,
        validators=[
            MinLengthValidator(10)
        ]
    )

    location = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    pets = models.ManyToManyField(
        Pet
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
    )
