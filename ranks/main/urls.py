from django.urls import path

from . import views


urlpatterns = [
    path('buy/<int:item_id>/', views.buy_item, name='buy_item'),
    path('item/<int:item_id>/', views.get_item_detail, name='get_item'),
    path('success/', views.SuccessView.as_view, name='success'),
    path('cansel/', views.CanselVies.as_view, name='cansel'),
]
