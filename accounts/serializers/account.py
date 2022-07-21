from django.contrib.auth.hashers import make_password
from django.contrib.auth import password_validation
from rest_framework import serializers
from accounts.models import CustomUserAccount
from accounts.tasks import custom_send_mail

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

    def verify_email(self):
        if self.validated_data.get("email"):
            custom_send_mail.delay(
                self.validated_data.get("email"),
                "Here subject",
                "Here will be our message."
            )