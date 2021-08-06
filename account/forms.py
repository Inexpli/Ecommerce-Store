from django import forms
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
