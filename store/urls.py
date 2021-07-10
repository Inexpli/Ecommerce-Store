from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<slug:slug>/', views.item, name='item'),
]
