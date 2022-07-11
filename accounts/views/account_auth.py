from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.contrib.auth import login, logout
from accounts.serializers import AccountSerializer, AccountSignUpSerializer, Login_serializer
from utils.services import auth_custom_user_account, delete_tokens


class AccountAuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = AccountSerializer

    def get_serializer_class(self):
        serializer_class = AccountSerializer
        if self.action == "sign_up":
            serializer_class = AccountSignUpSerializer
        elif self.action == "login":
            serializer_class = Login_serializer
        return serializer_class

    def get_permissions(self):
        permissions_classes = self.permission_classes
        if self.action == "logout":
            permissions_classes = [IsAuthenticated, ]
<<<<<<< HEAD
        elif self.action == "login":
            permissions_classes = [AllowAny, ]
=======
>>>>>>> main
        return [permission() for permission in permissions_classes]

    @action(methods=['post'], detail=False, url_path='sign_up')
    def sign_up(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=False, url_path='login')
    def login(self, request, *args, **kwargs):
        seializer = self.get_serializer(data=request.data)
        seializer.is_valid(raise_exception=True)
<<<<<<< HEAD
=======

>>>>>>> main
        account, token = auth_custom_user_account(
            seializer.validated_data.get('email'),
            seializer.validated_data.get('password')
        )
        responce = {}
        responce['account_data'] = AccountSerializer(instance=account).data
        responce['token'] = token
        return Response(data=responce, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='logout')
    def logout(self, request, *args, **kwargs):
        try:
            token = request.META.get('HTTP_AUTHORIZATION').split()[1]
            delete_tokens(request.user, token, False)
        except:
            raise ValidationError("ERROR: Account not found!")

        return Response(
            data={'details': "The account token has been deleted successfully!"},
            status=status.HTTP_200_OK
        )
<<<<<<< HEAD
=======




>>>>>>> main
