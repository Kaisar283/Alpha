from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class AccountManager(BaseUserManager):
    def create_account(self, email, password, **extra_fields):
        """
                Creates and saves a User with the given email, name,  date of
                birth and password.
        """
        if not email:
            raise ValueError(_("You must provide an email address"))
        email = self.normalize_email(email)
        account = self.model(email=email, **extra_fields)
        if password is None:
            raise ValueError(_("ERROR: The username must have a password"))
        else:
            account.set_password(password)
        account.save()
        return account

    def _create_superuser(self, email, password, **extra_field):
        account = self.model(email=email, **extra_field)
        account.is_active = True
        account.set_password(password)
        return account.save()

    def create_superuser(self, email, password, **extra_field):
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_active', True)

        if extra_field.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if extra_field.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        return self.create_account(email, password, **extra_field)