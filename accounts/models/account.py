from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from utils.consts import CustomUserRolesChoices
<<<<<<< HEAD
from accounts.managers import AccountManager
=======
from accounts.account_meneger import AccountManager
>>>>>>> main


class CustomUserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email address"), unique=True, blank=False)
    user_name = models.CharField(max_length=100, unique=True, blank=True)
<<<<<<< HEAD
    date_of_birth = models.DateField(verbose_name=_('Date of birth'), blank=True, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
=======
    date_of_birth = models.DateField(verbose_name=_('Date of birth'), blank=True, null=False)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
>>>>>>> main
    user_role = models.CharField(
        verbose_name=_('User roles'),
        max_length=20,
        choices=CustomUserRolesChoices.choices,
        default=CustomUserRolesChoices.USER.value
    )
<<<<<<< HEAD
    objects = AccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']
=======

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']
    objects = AccountManager()
>>>>>>> main

    class Meta:
        verbose_name = _('User account')
        verbose_name_plural = _('Users accounts')

    def __str__(self):
        return f"{self.id} - {self.email} - {self.date_of_birth} - {self.user_name}"