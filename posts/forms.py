from django.contrib.auth.forms import forms
from posts.models import Post


class PostImageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image']


class PostTextForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
