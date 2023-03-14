from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator

from webapp.models import Product, Order


def min_len_validator(string):
    if len(string) < 2:
        raise ValidationError('Заголовок должен быть длинее 2-ух символов')
    return string


def letters_capital_validator(string):
    if string != string.capitalize():
        raise ValidationError('Строка должна начинаться с большой буквы')


class ProductForm(forms.ModelForm):
    name = forms.CharField(validators=(MaxLengthValidator(
        limit_value=50,
    ), min_len_validator, letters_capital_validator), label='Наименование продукта')
    description = forms.CharField(widget=forms.Textarea, validators=(MinLengthValidator(
        limit_value=2,
    ), letters_capital_validator), label='Описание продукта')

    CHOICES = (
        ('Alcohol', 'Алкоголь'),
        ('Smartphone', 'Смартфон'),
        ('Cars', 'Машины'),
        ('Other', 'Разное')
    )
    category = forms.ChoiceField(choices=CHOICES, initial='Other', label='Категория')

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'remaining', 'price')
        labels = {
            'name': 'Наименование продукта',
            'description': 'Описание',
            'image': 'Фото продукта',
            'category': 'Категория',
            'remaining': 'Остаток',
            'price': 'Цена'
        }
        widgets = {
            'remaining': forms.NumberInput(attrs={'class': 'int_input', 'min': 0}),
            'price': forms.NumberInput(attrs={'class': 'int_input', 'min': 0})
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label='Search')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('username', 'address', 'phone_number')
        labels = {
            'username': 'Пользователь',
            'address': 'Адрес',
            'phone_number': 'Телефон'
        }
