from django.contrib import admin
from accounts.models import CustomUserAccount, AccountToken

admin.site.register(CustomUserAccount)
admin.site.register(AccountToken)
