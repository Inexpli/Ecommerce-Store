from django.urls import path

import basket

from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket, name='basket'),
    path('add/', views.basket_add, name='basket_add'),
    # path('remove/', views.basket_remove, name='basket_remove'),
]
