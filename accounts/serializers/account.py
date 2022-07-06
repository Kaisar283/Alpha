from rest_framework import serializers
from accounts.models import CustomUserAccount


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserAccount
        fields = "__all__"


class AccountSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserAccount
        fields = "email", "user_name", "date_of_birth"
