from django.db import models
from django.utils.text import slugify


# Create your models here.

class Pet(models.Model):
    name = models.CharField(
        max_length=30
    )
    pet_photo = models.URLField()

    birth_date = models.DateField(
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=False,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:  # slugify("My name") -> "My-name"
            self.slug = slugify(f'{self.name}-{self.id}')
        super().save(*args, **kwargs)

