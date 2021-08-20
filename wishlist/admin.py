from django.contrib import admin

from .models import List


@admin.register(List)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'item', 'added']
    list_filter = ['added']
