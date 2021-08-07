from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

UserModel:User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user
