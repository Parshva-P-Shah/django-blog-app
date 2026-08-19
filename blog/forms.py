from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Blog_form(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','slug','content','image','status']

class Registerationform(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')