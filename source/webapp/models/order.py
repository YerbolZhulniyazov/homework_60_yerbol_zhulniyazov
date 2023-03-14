from django.core.validators import MinValueValidator
from django.db import models


class Order(models.Model):
    products = models.ManyToManyField(
        to='webapp.product',
        through='OrderProducts'
    )
    username = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Пользователь'
    )
    phone_number = models.CharField(
        max_length=12,
        null=False,
        blank=False,
        verbose_name='Номер телефона'
    )
    address = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Адрес'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )

    def __str__(self):
        return f'{self.username},  {self.phone_number}, {self.address}, {self.created_at}'


class OrderProducts(models.Model):
    product = models.ForeignKey(
        to='webapp.product',
        on_delete=models.CASCADE
    )
    order = models.ForeignKey(
        to='webapp.order',
        on_delete=models.CASCADE
    )
    amount = models.IntegerField(
        verbose_name='Количество',
        validators=[MinValueValidator(1)]
    )
