from django import forms

from furryFunniesApp.authors.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorCreateForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        fields = ('first_name', 'last_name', 'passcode', 'pets_number')

        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Enter your first name...'}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Enter your last name...'}
            ),
            'passcode': forms.PasswordInput(
                attrs={'placeholder': 'Enter 6 digits...'}
            ),
            'pets_number': forms.TextInput(
                attrs={'placeholder': 'Enter the number of your pets...'}
            ),
        }

        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'passcode': 'Passcode',
            'pets_number': 'Pets Number',
        }

        help_texts = {
            'passcode': 'Your passcode must be a combination of 6 digits'
        }


class AuthorEditForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        exclude = ('passcode', )

        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'pets_number': 'Pets Number',
            'info': 'Info',
            'image_url': 'Profile Image URL'
        }


class AuthorDeleteForm(AuthorBaseForm):
    pass


class AuthorDetailForm(AuthorBaseForm):
    pass

