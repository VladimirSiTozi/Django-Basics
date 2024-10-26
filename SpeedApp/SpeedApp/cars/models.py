from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from SpeedApp.cars.choices import CarTypeChoices


class Car(models.Model):
    type = models.CharField(
        max_length=10,
        choices=CarTypeChoices.choices
    )

    model = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(1)
        ]
    )

    year = models.IntegerField()

    image_url = models.URLField(
        unique=True
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(1.0)
        ]
    )

    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
    )
