from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('order-done/', views.order_done, name='order_done'),
    path('add/', views.add, name='add'),
]
