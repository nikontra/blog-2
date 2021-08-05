from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш Email'})
    )
    username = forms.CharField(
        label='Введите Логин',
        required=True,
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш Логин'})
    )
    password1 = forms.CharField(
        label='Введите Пароль',
        required=True,
        help_text='Не менее 8 символов',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ваш Пароль'})
    )
    password2 = forms.CharField(
        label='Подтвердите Пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ваш Пароль'})
    )
    # some = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш Email'})
    )
    username = forms.CharField(
        label='Введите Логин',
        required=True,
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш Логин'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузите фото',
        required=False,
        widget = forms.FileInput
    )

    class Meta:
        model = Profile
        fields = ['img']
