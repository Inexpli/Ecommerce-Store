from django import forms
from django.contrib.auth.models import User
from .models import UserBase


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(min_length=4, max_length=50,
                                help_text='Required', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}), max_length=100, help_text='Required', error_messages={
                             'required': 'Enter email address'})
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Repeat password', 'class': 'form-control'}))

    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)

    def clean_username(self):
        user_name = self.cleaned_data('user_name').lower()
        ur = UserBase.objects.filter(user_name=user_name)
        if ur.count():
            raise forms.ValidationError(
                {'Username': 'Username already exists'})
        return user_name

    def clean_password(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Account with this email already exists')
        return email
