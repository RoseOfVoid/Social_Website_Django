from django import forms
from django.forms import CharField


class LoginForm(forms.Form):
    username = CharField()
    password = CharField(widget=forms.PasswordInput)