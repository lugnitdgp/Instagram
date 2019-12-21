from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email',)


class CreatePostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('caption','image','location',)

class UpdatePostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('caption','location')

