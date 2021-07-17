from django.contrib import admin

from .models import *

admin.register(User)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price',
                    'in_stock', 'created', 'promotion']
    list_filter = ['in_stock', 'created', 'price']
    list_editable = ['price', 'in_stock', 'promotion']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email', 'device']
