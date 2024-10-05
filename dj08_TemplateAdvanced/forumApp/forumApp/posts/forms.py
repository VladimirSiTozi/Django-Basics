from django import forms

from forumApp.posts.choises import LanguageChoice
from forumApp.posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Enter the title'}
            )
        }

        labels = {
            'title': 'That the title label'
        }

        # help_texts = {
        #     'title': 'This is help text',
        # }
        #
        # error_messages = {
        #     'title': {
        #         'required': 'This box is required'
        #     }
        # }


class PostCreateForm(PostForm):
    pass


class PostEditForm(PostForm):
    pass


class PostDeleteForm(PostForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search...'
            }
        )
    )


# class PostForm(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#     )
#
#     content = forms.CharField(
#         widget=forms.Textarea,
#     )
#
#     author = forms.CharField(
#         max_length=30
#     )
#
#     created_at = forms.DateTimeField()
#
#     languages = forms.ChoiceField(
#         choices=LanguageChoice.choices
#     )


class PersonForm(forms.Form):
    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Published'),
        (3, 'Archived')
    )

    person_name = forms.CharField(
        label='First name pls',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name here'}),  # Placeholder
        # initial='Ivan be',  # initial value
        # help_text='Add you first name',
        max_length=20,
    )

    description = forms.CharField(
        max_length=300,
        widget=forms.Textarea(attrs={'placeholder': 'Write sth about you'}),
    )

    email = forms.CharField(
        max_length=50,
        widget=forms.EmailInput(attrs={'class': 'my-email-class'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    age = forms.IntegerField()

    is_lecture = forms.BooleanField()

    status_radio = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=STATUS_CHOICES
    )

    status_checkbox_multiple = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=STATUS_CHOICES
    )

    # Keep the status as an int
    status_dropdown = forms.IntegerField(
        widget=forms.Select(choices=STATUS_CHOICES)
    )

    # Keep the status as a str - '2'
    # status = forms.ChoiceField(
    #     choices=STATUS_CHOICES
    # )

