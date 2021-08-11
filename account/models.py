from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email=self.normalize_email(email), username=username, password=password, **other_fields)

    def create_user(self, email, username, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        if not username:
            raise ValueError(_('You must provide a username'))

        email = self.normalize_email(email)
        user = self.model(email=self.normalize_email(email),
                          username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserBase(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    country = CountryField(blank=True)
    phone_number = models.CharField(max_length=9, blank=True)
    postcode = models.CharField(max_length=12, blank=True)
    address_line1 = models.CharField(max_length=50, blank=True)
    address_line2 = models.CharField(max_length=50, blank=True)
    town = models.CharField(max_length=50, blank=True)
    # User_status
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Accounts'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.username
