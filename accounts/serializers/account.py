from django.contrib.auth.hashers import make_password
from django.contrib.auth import password_validation
from rest_framework import serializers
from accounts.models import CustomUserAccount


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserAccount
        fields = "__all__"


class AccountSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserAccount
        fields = "email", "user_name", "date_of_birth", "password"

        def validate_password(self, value):
            password_validation.validate_password(value, self.instance)
            return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)
        fields = "email", "user_name", "date_of_birth"
