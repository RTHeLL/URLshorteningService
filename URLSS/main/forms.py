from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import URL, User


class URLGenerateForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['full_url']
        widgets = {
            'full_url': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Полная ссылка'})
        }


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Имя пользователя'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повторить пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Повторить пароль'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Пароль'}))
