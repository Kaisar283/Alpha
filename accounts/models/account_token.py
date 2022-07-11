import os
import binascii
from django.db import models
from .account import CustomUserAccount
from django.utils.translation import gettext_lazy as _


class AccountToken(models.Model):
    key = models.CharField(max_length=120, unique=True, verbose_name=_("Account Token"))
    account = models.ForeignKey(CustomUserAccount, on_delete=models.CASCADE, verbose_name=_('Account'))

    class Meta:
        abstract = False
        verbose_name = _('Token')
        verbose_name_plural = _('Tokens')

    def save(self, *args, **kwargs):
        if self.key is None or not self.key:
            self.key = self.generate_token()
        return super(AccountToken, self).save(*args, **kwargs)

    def generate_token(self):
        return binascii.hexlify(os.urandom(50)).decode()

    def __str__(self):
<<<<<<< HEAD
        return f"{self.account.email} - {self.key}"
=======
        return f"{self.account.email} - {self.key}"
>>>>>>> main
