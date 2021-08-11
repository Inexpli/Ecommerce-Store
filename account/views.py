from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from core.settings import EMAIL_HOST_USER

from .forms import RegistrationForm, UserEditForm
from .models import UserBase
from .token import account_activation_token


def account_register(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password1'])
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Active your Account'
            message = render_to_string('account/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            email = EmailMessage(
                subject,
                message,
                EMAIL_HOST_USER,
                [user.email],
            )
            email.send(fail_silently=False)
            return render(request, 'account/activation_sent.html', {'email': user.email})
    else:
        registerForm = RegistrationForm()
    return render(request, 'account/register.html', {'form': registerForm})


def account_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except:
        pass

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('account:complete')
    else:
        return render(request, 'account/activation_invalid.html')


def user_active_check(user):
    return user.is_active == True


@user_passes_test(user_active_check)
def registration_complete(request):
    return render(request, 'account/activation_complete.html')


@login_required
def account_dashboard(request):
    return render(request, 'account/dashboard.html')


@login_required
def account_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.username = request.user.username
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request, 'account/profile.html', {'form': user_form})
