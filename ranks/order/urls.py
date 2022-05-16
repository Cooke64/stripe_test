from django.urls import path

from . import views


urlpatterns = [
    path('/buy/<order_id>', views.get_order, name='buy_order'),
    ]
