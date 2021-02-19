from .models import Blog
from django.forms import ModelForm
from django import forms


class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title', 'author_firstname', 'author_lastname', 'topic_category', 'post']