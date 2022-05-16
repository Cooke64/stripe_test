from django.db import models


class Item (models.Model):
    CURRENCY = (
        ('ru', 'RUB'),
        ('usd', 'USD'),
    )
    name = models.CharField('Название', max_length=250)
    description = models.TextField('Описание',blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    currency = models.CharField(
        'Валюта',
        choices=CURRENCY,
        default='ru',
    )

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name
