from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class Login_serializer(serializers.Serializer):
    email = serializers.CharField(max_length=50, required=True, help_text=_('Email'))
    password = serializers.CharField(max_length=100, required=True, help_text=_('Password'))
