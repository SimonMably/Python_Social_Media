from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "surname",
            "username",
            "email",
            "password1",
            "password2",
        ]

    first_name = forms.CharField(
        label="First Name",
        strip=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    surname = forms.CharField(
        label="Surname",
        strip=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    username = forms.CharField(
        label="Username",
        strip=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.CharField(
        label="Email",
        strip=False,
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        min_length=12,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        min_length=12,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )


class UserForm(ModelForm):
    class Meta:
        Model: User
        fields = ["avatar", "name", "username", "email", "bio"]
