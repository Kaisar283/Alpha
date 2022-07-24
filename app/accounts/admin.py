from django.contrib import admin
from .models import AccountToken
from accounts.models import CustomUserAccount, AccountToken

admin.site.register(CustomUserAccount)
admin.site.register(AccountToken)
