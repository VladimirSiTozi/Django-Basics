from django import forms
from django.core.exceptions import ValidationError

from SpeedApp.cars.models import Car
from SpeedApp.mixins import ReadOnlyMixin


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner', )


class CarCreateForm(CarBaseForm):
    image_url = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': '"https://..."',
            'error_messages': {

            }
        })
    )

    def clean_image_url(self):
        image_url = self.cleaned_data.get('image_url')

        # Check if a car with this image_url already exists
        if Car.objects.filter(image_url=image_url).exists():
            raise ValidationError("This image URL is already in use! Provide a new one.")

        return image_url


class CarDetailForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(ReadOnlyMixin, CarBaseForm):
    read_only_fields = ['type', 'model', 'year', 'image_url', 'price']
