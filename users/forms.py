from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import Users
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = Users
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите фамилию'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите адрес эл. почты'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Подтвердите пароль'
    }))

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": 'form-control py-4',
        'id': 'inputFirstName'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": 'form-control py-4',
        'id': 'inputLastName'
    }))

    img = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
        'id': 'userAvatar'
    }), required=False)

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": 'form-control py-4',
        'id': 'inputUserName',
        'readonly': True
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": 'form-control py-4',
        'id': 'inputEmailAddress',
        'readonly': True
    }))

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'img', 'username', 'email']

    pass


"""Есть понятие как AAA (Audit, Authentication, Authorization) - это три основных компонента системы управления 
доступом. Audit - контроль, Authentication - аутентификация, Authorization - авторизация."""
