from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import UserLoginForm

app_name = 'account'

urlpatterns = [
    path('register/', views.account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.account_activate, name='activate'),
    path('registration_complete/', views.registration_complete, name='complete'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='account/login.html',
                                                form_class=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.account_dashboard, name='dashboard'),
    path('profile/', views.account_profile, name='profile'),
]
