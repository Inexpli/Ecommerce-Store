from django.urls import path

from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add/', views.wishlist_add, name='wishlist_add'),
    path('remove/', views.wishlist_remove, name='wishlist_remove'),
    path('not-auth-add/', views.not_auth_wishlist_add,
         name='not_auth_wishlist_add'),
    path('not-auth-remove/', views.not_auth_wishlist_delete,
         name='not_auth_wishlist_remove'),
]
