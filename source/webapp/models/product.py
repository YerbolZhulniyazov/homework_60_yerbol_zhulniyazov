from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Наименование товара'
    )
    description = models.CharField(
        max_length=2000,
        null=True,
        verbose_name='Описание товара'
    )
    image = models.TextField(
        null=False,
        verbose_name='Фото товара'
    )
    category = models.CharField(
        max_length=50,
        null=False,
        default='other',
        verbose_name='Категория'
    )
    remaining = models.IntegerField(
        null=False,
        default=1,
        verbose_name='Остаток',
        validators=[MinValueValidator(0)]
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
         null=False,
         default=False
    )
    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True,
        default=None
    )

    def __str__(self):
        return f'{self.name} - {self.category}'

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
