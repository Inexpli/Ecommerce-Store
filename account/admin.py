from django.contrib import admin

from .models import UserBase


@admin.register(UserBase)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'country', 'is_active', 'created']
    list_filter = ['is_staff', 'created']
