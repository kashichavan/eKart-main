from typing import Any
from django import forms
from django.contrib.auth.models import User
from .models import Account
from django.contrib.auth.hashers import make_password

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=['email','username','first_name','last_name','password']
    

class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())