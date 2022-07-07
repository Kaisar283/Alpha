from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import TokenAuthentication
from accounts.models import AccountToken
from django.utils.translation import gettext_lazy as _


class CustomAuthToken(TokenAuthentication):
    def __init__(self):
        super().__init__()

    model = AccountToken

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('account').get(key=key)
        except model.DoesNotExist:
            raise AuthenticationFailed(_('Invalid token.'))

        if not token.account.is_active:
            raise AuthenticationFailed(_('User inactive or deleted.'))

        return (token.account, token)