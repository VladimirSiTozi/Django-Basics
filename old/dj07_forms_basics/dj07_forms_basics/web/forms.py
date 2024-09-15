from django import forms

from dj07_forms_basics.web.models import Employee


class EmployeeForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label='First Name:',
    )

    last_name = forms.CharField(
        max_length=30,
        required=True,
        label='Last Name:',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your last name'
            }
        )
    )

    age = forms.IntegerField(
        required=True,
        label='Age:'
    )

    INTEREST = (
            (1, 'Gaming'),
            (2, 'Reading'),
            (3, 'Sport'),
            (4, 'Girls'),
        )

    interests = forms.ChoiceField(
        choices=INTEREST,
        label='Interests:'
    )

    interests2 = forms.IntegerField(
        widget=forms.Select(choices=INTEREST),
        label='Interests2:'
    )

    interests3 = forms.IntegerField(
        widget=forms.RadioSelect(choices=INTEREST),
        label='Interests3:'
    )

    interests4 = forms.IntegerField(
        widget=forms.CheckboxSelectMultiple(choices=INTEREST),
        label='Interests5:'
    )


class EmployeeNormalForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label='First Name:',
    )

    last_name = forms.CharField(
        max_length=30,
        required=True,
        label='Last Name:',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your last name'
            }
        )
    )

    age = forms.IntegerField(
        required=True,
        label='Age:'
    )


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ()  # exclude given fields
