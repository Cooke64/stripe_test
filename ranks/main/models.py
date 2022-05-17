from django.db import models


class Item (models.Model):
    CURRENCY = (
        ('eur', 'EUR'),
        ('usd', 'USD'),
    )
    name = models.CharField('Название', max_length=250)
    description = models.TextField('Описание', blank=True)
    price = models.IntegerField('Цена')
    currency = models.CharField(
        'Валюта',
        choices=CURRENCY,
        default='eur',
        max_length=3
    )

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name
