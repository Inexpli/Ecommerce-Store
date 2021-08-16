from django.db import models
from decimal import Decimal
from django.conf import settings
from django_countries.fields import CountryField

from store.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='order_user')
    product = models.ForeignKey(
        Product, related_name='order_items', on_delete=models.CASCADE)
    size = models.CharField(max_length=2)
    quantity = models.PositiveIntegerField(default=1)
    full_name = models.CharField(max_length=60)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    postcode = models.CharField(max_length=12)
    town = models.CharField(max_length=50)
    country = CountryField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2)
    order_key = models.CharField(max_length=200)
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.user)
