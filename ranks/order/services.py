from django.core.exceptions import ObjectDoesNotExist
from stripe.api_resources.order import Order


def get_my_order(request):
    user_id = 1
    try:
        orders = Order.user_orders.filter(user=user_id)
        return orders
    except ObjectDoesNotExist as e:
        raise e
