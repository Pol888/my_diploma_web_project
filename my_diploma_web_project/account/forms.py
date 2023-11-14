from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class NewPasswordAfterReset(SetPasswordForm): # переопределение формы для сброса пароля
    def __init__(self, *args, **kwargs):
        super(NewPasswordAfterReset, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(
        label="Новый пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control", "autocomplete": "new-password"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label="Подтверждение  нового пароля",
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control", "autocomplete": "new-password"}),
    )

class EnterYourPasswordResetEmailForm(PasswordResetForm):  # переопределение стандартной формы ввода
                                                           # почты для сброса пароля
    def __init__(self, *args, **kwargs):
        super(EnterYourPasswordResetEmailForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='Электронная почта',
                             widget=forms.EmailInput(attrs={"class": "form-control",
                                                            'placeholder': "login@server.extension"}))







class LoginForm(forms.Form):  # Форма для входа в систему

    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "form-control",
                                                                            'placeholder': "login123"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control"}))














#class UserRegistrationForm(forms.Form):  # форма регистрации
#
#    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={"class": "form-control",
#                                                                            'placeholder': "login123"}))
#    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={"class": "form-control",
#                                                                            'placeholder': "name"}))
#    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={"class": "form-control",
#                                                                           'placeholder': "login@server.extension"}))
#    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
#    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={"class": "form-control"}))
#
#
#
#    def clean_password2(self):
#        cd = self.cleaned_data
#        if cd['password'] != cd['password2']:
#            raise forms.ValidationError('Пароли не совпадают')
#        if len(cd['password2']) < 8:
#            raise forms.ValidationError('Количество символов меньше 8')
#        if cd['password2'].isdigit():
#            raise forms.ValidationError('Не должны быть одни цифры')
#
#        return cd['password2']



class UserRegistrationForm(forms.ModelForm):  # форма регистрации (на основе модели)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email',]
        labels = {'username': 'Логин', 'first_name': 'Имя', 'email': 'Электронная почта'}
        help_texts = {'username': ''}
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control", 'placeholder': "login123"}),
            'first_name': forms.TextInput(attrs={"class": "form-control", 'placeholder': "name"}),
            'email': forms.EmailInput(attrs={"class": "form-control", 'placeholder': "login@server.extension"}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        if len(cd['password2']) < 8:
            raise forms.ValidationError('Количество символов меньше 8')
        if cd['password2'].isdigit():
            raise forms.ValidationError('Не должны быть одни цифры')
        return cd['password2']
