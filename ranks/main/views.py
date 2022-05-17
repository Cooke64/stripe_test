import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from main.services import get_item, create_checkout_session

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    """При успешной оплате рендерим эту вьюху"""
    template_name = 'main/success.html'


class CanselVies(TemplateView):
    """При отказе рендерим эту вьюху"""
    template_name = 'main/cancel.html'


def buy_item(request, item_id: int):
    """Получаем информацию о товаре по его id."""
    item = get_item(item_id=item_id)
    try:
        session = create_checkout_session(item=item)
        return JsonResponse({'session': session.id})
    except Exception as e:
        return JsonResponse({'Ошибка': str(e)})


def get_item_detail(request, item_id: int):
    """Получаем информацию о товаре по его id."""
    context = {
        'item': get_item(item_id=item_id),
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'main/item_detail.html', context)
