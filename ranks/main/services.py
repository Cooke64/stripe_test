import stripe
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from stripe.api_resources.order import Order

from main.models import Item

HOST = settings.ALLOWED_HOSTS[0]


def create_checkout_session(item):
    """Создаем объект сессии Stripe."""
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'quantity': 1,
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
            }
        }],
        mode='payment',
        success_url=f'http://{HOST}/success',
        cancel_url=f'http://{HOST}/cancel',
    )
    order_create(item)
    return session


def get_item(item_id: int):
    """Получаем товар по его id."""
    try:
        item = get_object_or_404(Item, id=item_id)
        return item
    except ObjectDoesNotExist as e:
        raise e


def order_create(item):
    """Создание заказа."""
    try:
        Order.objects.create(
            item=item.pk,
            # В тренировочных целях
            user=1,
            price=item.price,
            quantity=1
        )
    except:
        raise 'Проверить заказ'
