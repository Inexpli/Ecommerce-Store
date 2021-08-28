from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'country',
                    'town', 'total_paid', 'created', 'billing_status']
    readonly_fields = ['user', 'product', 'country', 'size', 'quantity', 'full_name', 'address1', 'address2', 'order_key', 'postcode',
                       'town', 'total_paid', 'created', 'billing_status']
    list_filter = ['created', 'billing_status', 'product']
