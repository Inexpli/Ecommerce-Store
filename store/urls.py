from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/all/', views.all, name='all'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('item/<slug:slug>/', views.item, name='item'),
]
