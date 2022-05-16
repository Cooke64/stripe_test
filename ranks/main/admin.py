from django.contrib import admin

from .models import Item


@admin.register(Item)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    search_fields = ('name',)
    empty_value_display = 'не указано'
    ordering = ['-id']
