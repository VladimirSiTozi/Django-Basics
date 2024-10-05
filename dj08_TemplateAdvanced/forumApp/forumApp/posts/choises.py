from django.db import models


class LanguageChoice(models.TextChoices):
    PYTHON = 'py', 'Python'
    JAVASCRIPT = 'js', 'JavaScript'
    C_PLUS_PLUS = 'cpp', 'C++'
    C = 'c', 'C'
    JAVA = 'j', 'Java'
