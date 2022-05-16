from django.contrib import admin
from .models import OrderItem


@admin.register(OrderItem)
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['item']
