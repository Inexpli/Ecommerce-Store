from django.conf import settings
from django.db import models

from store.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=2)
    quantity = models.PositiveIntegerField(default=1)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-added',)

    def price(self):
        return float(self.item.price * self.quantity)

    def __str__(self):
        return str(self.user)
