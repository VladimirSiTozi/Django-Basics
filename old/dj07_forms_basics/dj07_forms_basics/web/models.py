from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
