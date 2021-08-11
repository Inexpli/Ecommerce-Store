from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.http import request
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from .models import UserBase


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(min_length=4, max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': 'form-control', 'type': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control'}))


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(min_length=4, max_length=20,
                               help_text='Required', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}), max_length=30, help_text='Required', error_messages={
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


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'placeholder': 'First name', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'placeholder': 'Last name', 'class': 'form-control'}))
    country = CountryField()
    phone_number = forms.CharField(max_length=9, widget=forms.TextInput(
        attrs={'placeholder': 'Phone number', 'class': 'form-control'}))
    postcode = forms.CharField(max_length=12, widget=forms.TextInput(
        attrs={'placeholder': 'Post code', 'class': 'form-control'}))
    town = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Town', 'class': 'form-control'}))
    address_line1 = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Address line 1', 'class': 'form-control'}))
    address_line2 = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Address line 2', 'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        ur = UserBase.objects.filter(username=username)
        if ur.count():
            raise forms.ValidationError('Username already exists')
        return username

    class Meta:
        model = UserBase
        fields = ['first_name', 'last_name',
                  'country', 'phone_number', 'postcode', 'town', 'address_line1', 'address_line2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['country'].required = False
        self.fields['phone_number'].required = False
        self.fields['postcode'].required = False
        self.fields['town'].required = False
        self.fields['address_line1'].required = False
        self.fields['address_line2'].required = False
