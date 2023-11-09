from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.core.exceptions import ValidationError


class NewPasswordAfterReset(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(NewPasswordAfterReset, self).__init__(*args, **kwargs)

    error_messages = {
        "password_mismatch": "Пароли не совпадают.",
    }
    new_password1 = forms.CharField(
        label="Новый пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control", "autocomplete": "new-password"}),
        strip=False,
        help_text='<ul>'
                  '<li>Пусть он будет хорош.</li>'
                  '<li>Символов не менее 8 будет.</li>'
                  '<li>Не только цифры.</li></ul>',
    )
    new_password2 = forms.CharField(
        label="Подтверждение  нового пароля",
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control", "autocomplete": "new-password"}),
    )

    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2: str = self.cleaned_data.get("new_password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        if len(password2) < 8 and password2.isdigit():
            raise ValidationError(
                'Длинна пароля менее 8 символов.\n'
                'Пароль состоит из одних цифр.'
            )
        if len(password2) < 8:
            raise ValidationError(
                'Длинна пароля менее 8 символов.'
            )
        if password2.isdigit():
            raise ValidationError(
                'Пароль состоит из одних цифр.'
            )
        return password2


class EnterYourPasswordResetEmailForm(PasswordResetForm):  # переопределение стандартной формы сброса пароля
    def __init__(self, *args, **kwargs):
        super(EnterYourPasswordResetEmailForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='Электронная почта',
                             widget=forms.EmailInput(attrs={"class": "form-control",
                                                            'placeholder': "login@server.extension"}))


class LoginForm(forms.Form):  # Форма для входа в систему

    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "login123"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs):  # переопределение <label>text</l...>
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Логин"
        self.fields['password'].label = "Пароль"


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
