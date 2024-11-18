from django import forms


class RegistrationForm(forms.Form):
    login = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(
                               min_length=8, label='Введите пароль')
    password_rep = forms.CharField(
                               min_length=8, label='Повторите пароль')
    age = forms.CharField(max_length=3, label='Введите возраст')