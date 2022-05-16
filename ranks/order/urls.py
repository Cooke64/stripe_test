from django.urls import path

from . import views


urlpatterns = [
    path('buy/<order_id>', views, name='buy_order'),
    ]
