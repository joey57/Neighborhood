from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Business, Profile, NeighbourHood, Post

class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

class UpdateProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ('user', 'neighbourhood')

class NeighbourHoodForm(forms.ModelForm):
  class Meta:
    model = NeighbourHood
    exclude = ('admin',)

class BusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    exclude =('user', 'neighbourhood')

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ('user', 'hood')    
    