from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.exceptions import ValidationError
from accounts.models import CustomUserAccount, AccountToken


def auth_custom_user_account(email: str, password: str):
    data = {
        'username': email,
        'password': password
    }
    serializer = AuthTokenSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    account = serializer.validated_data.get('user')
    account_token = AccountToken.objects.create(account=account)
    return account, account_token.key


def delete_tokens(account: CustomUserAccount, token: str, all:bool):
    try:
        if all:
            AccountToken.objects.filter(account=account).delete()
        else:
            AccountToken.objects.filter(account=account, key=token).delete()
    except:
        raise ValidationError("ERROR: Token not found!")