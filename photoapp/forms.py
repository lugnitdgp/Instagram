from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post, Comment
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email','password1','password2',)


class CreatePostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('caption','image','location',)

class UpdatePostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('caption','location')

class CreateCommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=('text',)

