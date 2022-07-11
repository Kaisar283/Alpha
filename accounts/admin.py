from django.contrib import admin
<<<<<<< HEAD
from .models import AccountToken

=======
from accounts.models import CustomUserAccount, AccountToken

admin.site.register(CustomUserAccount)
>>>>>>> main
admin.site.register(AccountToken)
