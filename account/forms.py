from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

from .models import UserBase


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(min_length=4, max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': 'form-control', 'type': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control'}))


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(min_length=4, max_length=50,
                               help_text='Required', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}), max_length=100, help_text='Required', error_messages={
                             'required': 'Enter email address'})
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Repeat password', 'class': 'form-control'}))

    class Meta:
        model = UserBase
        fields = ('username', 'email')

    def clean_username(self):
        username = self.cleaned_data['username']
        ur = UserBase.objects.filter(username=username)
        if ur.count():
            raise forms.ValidationError('Username already exists')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match')
        return password2

    def clean_email(self):
        email = (self.cleaned_data['email']).lower()
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Account with this email already exists')
        return email


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = UserBase
        fields = ['username', 'email']
