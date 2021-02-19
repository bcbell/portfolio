from .models import Blog
from django.forms import ModelForm
from django import forms


class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title', 'topic_category','author_firstname', 'author_lastname', 'post']