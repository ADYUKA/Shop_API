from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('User already exists')
        return username


class LoginValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class ConfirmValidateSerializer(serializers.Serializer):
    user = serializers.CharField()
    code = serializers.CharField()

    def validate_user(self, value):
        try:
            user = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError('User is not exists')
        return user

    def validate_code(self, code):
        try:
            models.ConfirmCode.objects.get(code=code)
        except models.ConfirmCode.DoesNotExist:
            raise ValidationError('Еhe code is not correct!')
        return code