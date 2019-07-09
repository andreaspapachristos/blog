from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'text email',
                                                           'type': 'email',
                                                           'name': 'email',
                                                           'placeholder': 'email',
                                                           'required': ''}))

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'text ',
                                                             'type': 'text',
                                                             'name': 'username',
                                                             'placeholder': 'username',
                                                             'required': ''}))
    password1 = forms.PasswordInput(widget=forms.TextInput(attrs={'class': 'text ',
                                                                  'type': 'password',
                                                                  'name': 'password',
                                                                  'placeholder': 'password',
                                                                  'required': ''}))

    password2 = forms.PasswordInput(widget=forms.TextInput(attrs={'class': 'text w3lpass',
                                                                  'type': 'password',
                                                                  'name': 'password',
                                                                  'placeholder': 'confirm password',
                                                                  'required': ''}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']