import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from main.services import get_sessions, get_item

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'main/success.html'


class CanselVies(TemplateView):
    template_name = 'main/cancel.html'


def buy_item(item_id: int) -> JsonResponse:
    """Получаем информацию о товаре по его id."""
    item = get_item(item_id)
    session = get_sessions(item)
    return JsonResponse({'session': session.id})


def get_item_detail(request, item_id: int):
    """Получаем информацию о товаре по его id."""
    context = {
        'item': get_item(item_id),
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'main/item_detail.html', context)
