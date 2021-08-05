from django.db import models
from django.db.models.fields import CharField, SlugField
from django.urls import reverse


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(in_stock=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('store:category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    in_stock = models.BooleanField(default=False)
    promotion = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:item', args=[self.slug])

    def __str__(self):
        return self.title
