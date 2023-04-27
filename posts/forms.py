from .models import BlogPost, Tags, Task
from django import forms
from django.forms import widgets


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image', 'category']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']

    widgets = {
        'degree': forms.Select(choices=Task.STATUS_OPTION)
    }


class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['title']
