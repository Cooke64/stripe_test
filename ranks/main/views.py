import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from ranks.main.services import get_sessions, get_item

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'main/success.html'


class CanselVies(TemplateView):
    template_name = 'main/cancel.html'


def buy_item(id: int) -> JsonResponse:
    """Получаем информацию о товаре по его id."""
    item = get_item(id)
    session = get_sessions(item)
    return JsonResponse({'session_id': session.id})


def get_item_detail(request, id: int):
    """Получаем информацию о товаре по его id."""
    context = {'items': get_item(id)}
    return render(request, 'main/item_detail.html', context)
