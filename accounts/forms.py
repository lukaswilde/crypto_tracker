from django import forms
from django.contrib.auth.forms import AuthenticationForm


class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        label="Username",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
