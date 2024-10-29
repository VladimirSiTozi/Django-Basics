from django.core.validators import MinLengthValidator
from django.db import models

from furryFunniesApp.authors.validators import ProfileNameValidator, PasscodeDigitsValidator


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            ProfileNameValidator(),
        ]
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            ProfileNameValidator(),
        ]
    )

    passcode = models.CharField(
        validators=[
            PasscodeDigitsValidator()
        ]
    )

    pets_number = models.SmallIntegerField()

    info = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )
