from django import forms
from diary_app.models import Post

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2', )


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('date', 'weather', 'mood', 'title', 'text',)