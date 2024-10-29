from django.core.validators import MinLengthValidator
from django.db import models

from furryFunniesApp.authors.models import Author


class Post(models.Model):
    title = models.CharField(
        unique=True,
        max_length=50,
        validators=[
            MinLengthValidator(5),

        ]
    )

    image_url = models.URLField()

    content = models.TextField()

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    class Meta:
        ordering = ['-updated_at']
        get_latest_by = 'updated_at'
