from django.shortcuts import render

from order.services import get_my_order


def get_order(request):
    orders = get_my_order(request)
    context = {'orders': orders}
    return render(request, 'order/order_list.html', context)
