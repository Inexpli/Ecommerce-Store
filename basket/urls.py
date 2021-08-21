from django.urls import path

from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket, name='basket'),
    path('add/', views.basket_add, name='basket_add'),
    path('delete/', views.basket_delete, name='basket_delete'),
    path('update/', views.basket_update, name='basket_update'),
    path('auth-add/', views.auth_basket_add, name='auth_basket_add'),
    path('auth-delete/', views.auth_basket_remove, name='auth_basket_remove'),
]
