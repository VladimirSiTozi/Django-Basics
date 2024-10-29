from django import forms
from django.template.defaultfilters import title

from furryFunniesApp.posts.mixins import ReadOnlyMixin
from furryFunniesApp.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', )

        labels = {
            'title': 'Title',
            'image_url': 'Post Image URL',
            'content': 'Content',
        }


class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ('title', 'image_url', 'content')

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Put an attractive and unique title...'}
            ),
            'content': forms.Textarea(
                attrs={'placeholder': 'Share some interesting facts about your adorable pets...'}
            )
        }

        help_texts = {
            'image_url': 'Share your funniest furry photo URL!',
        }

        error_messages = {
            'title': {
                'unique': "Oops! That title is already taken. How about something fresh and fun?",
            }
        }


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    read_only_fields = ['title', 'image_url', 'content']


class PostDetailsForm(PostBaseForm):
    pass

