from django.contrib import admin

from .models import Basket


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['user', 'added']
    readonly_fields = ['user', 'item', 'added']
    list_filter = ['added']
