from django import forms

from MusicApp.mixins import ReadOnlyMixin
from MusicApp.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    pass

