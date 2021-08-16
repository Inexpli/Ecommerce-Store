from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'country',
                    'town', 'total_paid', 'created', 'billing_status']
    list_filter = ['created', 'product', 'country']
