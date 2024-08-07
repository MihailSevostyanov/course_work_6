from django.forms import ModelForm

from blog.models import Blog
from mailing.forms import StyleFormMixin


class BlogForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'image', 'slug', 'is_published', 'number_views']
