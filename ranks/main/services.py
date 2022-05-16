import stripe
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from stripe.api_resources.order import Order

from main.models import Item

HOST = settings.ALLOWED_HOSTS[0]


def get_sessions(item):
    try:
        stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                    },
                    'price': item.price,
                    'quantity': 1,
                }
            }],
            mode='payment',
            success_url=f'{HOST}/success',
            cancel_url=f'{HOST}/cancel',
        )
        order_create(item)
    except Exception as e:
        return JsonResponse({'Ошибка': str(e)})


def get_item(id: int):
    try:
        item = get_object_or_404(Item, id=id)
        return item
    except ObjectDoesNotExist as e:
        raise e


def order_create(item):
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
