from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory

from forumApp.posts.choises import LanguageChoice
from forumApp.posts.mixins import DisableFieldsMixin
from forumApp.posts.models import Post, Comment


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

    def clean_author(self):
        author = self.cleaned_data.get('author')

        if author[0] != author[0].upper():
            raise ValidationError('Author name should start with upper letter!')

        return author

    def clean(self):
        cleaned_date = super().clean()

        title = cleaned_date.get('title')
        content = cleaned_date.get('content')

        if title and content and title in content:
            raise ValidationError('The post title cannot be included in the post content')

        return cleaned_date

    def save(self, commit=True):
        post = super().save(commit=False)

        post.title = post.title.capitalize()

        if commit:
            post.save()

        return post


class PostCreateForm(PostForm):
    pass


class PostEditForm(PostForm, DisableFieldsMixin):
    disabled_fields = ('author',)


class PostDeleteForm(PostForm, DisableFieldsMixin):
    disabled_fields = ('title', 'content', 'author', 'languages', 'image')


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        # error_messages={
        #     'required': 'Sorry, this field is required',
        #     'max_length': 'Sorry max length is 10',
        #     },
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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content')

        labels = {
            'author': '',
            'content': '',
        }

        error_messages = {
            'author': {
                'required': 'Author name is required!!!'
            },
            'content': {
                'required': 'Content is required!!!'
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your name...'
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your comment here...'
        })


CommentFormSet = formset_factory(CommentForm, extra=1)
