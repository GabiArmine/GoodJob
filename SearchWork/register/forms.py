from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'place\
    holder': 'Email'}), )
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'p\
    laceholder': 'First Name'}), )
    last_name = forms.CharField( max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'p\
    laceholder': 'Last Name'}), )
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'pla\
    ceholder': 'Username'}), )
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control',\
    'placeholder': 'Password'}), )
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control',\
    'placeholder': 'Password Again'}), )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', ]
