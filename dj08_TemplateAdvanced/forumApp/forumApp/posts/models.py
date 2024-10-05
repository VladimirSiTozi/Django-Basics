from django.db import models

from forumApp.posts.choises import LanguageChoice
from forumApp.posts.validators import BadLanguageValidator


class Post(models.Model):
    title = models.CharField(
        max_length=100,
    )

    content = models.TextField(
        validators=[
            BadLanguageValidator(),
        ]
    )

    author = models.CharField(
        max_length=30,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    languages = models.CharField(
        choices=LanguageChoice.choices,
        default=LanguageChoice.PYTHON,
        max_length=20
    )
