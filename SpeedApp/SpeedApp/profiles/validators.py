import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ProfileNameValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Username must contain only letters, digits, and underscores!'
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        pattern = r"^[A-Za-z0-9_]+$"
        match = re.fullmatch(pattern, value)

        if not match:
            raise ValidationError(self.message)