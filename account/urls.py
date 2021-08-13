from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from . import views
from .forms import UserLoginForm

app_name = 'account'

urlpatterns = [
    path('register/', views.account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.account_activate, name='activate'),
    path('registration-complete/', views.registration_complete, name='complete'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='account/login.html',
                                                form_class=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.account_dashboard, name='dashboard'),
    path('profile/', views.account_profile, name='profile'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='account/password_reset/password_reset_request.html',
             email_template_name='account/password_reset/email.html',
             success_url=reverse_lazy('account:password_reset_done')
         ),
         name='password_reset_request'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='account/password_reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/password_reset/password_reset_confirm.html',
             success_url=reverse_lazy('account:password_reset_complete')
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/password_reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
