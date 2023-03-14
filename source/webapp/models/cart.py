from django.core.validators import MinValueValidator
from django.db import models


class ProductInCart(models.Model):
    product = models.ForeignKey(
        to='webapp.product',
        on_delete=models.PROTECT,
        related_name='product',
        verbose_name='Продукт'
    )
    amount = models.IntegerField(
        null=False,
        default=0,
        verbose_name='Количество товара в корзине',
        validators=[MinValueValidator(0)]
    )

