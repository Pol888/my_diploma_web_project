from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'city', 'address', 'postal_code']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Электронная почта',
                  'city': 'Город', 'address': 'Адрес', 'postal_code': 'Индекс'}

        help_texts = {'first_name': ''}
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control", 'placeholder': "Как в паспорте"}),
            'last_name': forms.TextInput(attrs={"class": "form-control", 'placeholder': "Как в паспорте"}),
            'email': forms.EmailInput(attrs={"class": "form-control", 'placeholder': "login@server.extension"}),
            'city': forms.TextInput(attrs={"class": "form-control", 'placeholder': "поселок Мирный"}),
            'address': forms.TextInput(attrs={"class": "form-control", 'placeholder': "Мирная 101/a кв 2"}),
            'postal_code': forms.TextInput(attrs={"class": "form-control", 'placeholder': "123456"}),
        }

