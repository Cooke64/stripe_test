from django.contrib.auth import get_user_model
from django.db import models

from main.models import Item


User = get_user_model()


class OrderManager(models.Manager):
    def get_orders_by_user(self):
        return super(OrderManager, self).get_queryset().select_related('user')


class OrderItem(models.Model):
    item = models.ForeignKey(Item, related_name='order_items',
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='order_item',
                             on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Количество', default=0)
    has_paid = models.BooleanField('Статус оплаты', default=False, )
    created_on = models.DateTimeField('Дата создания', auto_now_add=True)

    user_orders = OrderManager()

    def __str__(self):
        return f'{self.pk}'

    def get_cost(self):
        return self.price * self.quantity
