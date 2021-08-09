from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework import serializers

from core.services.mail_service import MailService

UserModel: User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password', 'name')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        MailService.register_mail_sender(user.id, user.email)
        return user


class UserUpdateSerializer(UserSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'name')


class UserChangePasswordSerializer(UserSerializer):
    class Meta:
        model = UserModel
        fields = ('password', 'id')
        extra_kwargs = {
            'password': {'write_only': True}
        }