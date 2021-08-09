from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserChangePasswordSerializer, UserSerializer, UserUpdateSerializer

UserModel: User = get_user_model()


class UserListCreateView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserRetrieveUpdateSoftDeleteView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserUpdateSerializer
    queryset = UserModel.objects.all()

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data = UserModel.objects.get(pk=pk)
        except Exception:
            return Response('Not Found', status.HTTP_404_NOT_FOUND)
        data.is_active = False
        data.deleted = True
        data.save()
        return Response('deleted', status.HTTP_204_NO_CONTENT)


class UserChangePasswordView(UpdateAPIView):
    serializer_class = UserChangePasswordSerializer
    permission_classes = (IsAuthenticated,)
    queryset = UserModel.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class UserStartChangePasswordView(TokenObtainPairView):
    permission_classes = (AllowAny,)


class UserActivatorView(APIView):
    permission_classes = (AllowAny,)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data = UserModel.objects.get(pk=pk)
        except Exception:
            return Response('Not Found', status.HTTP_404_NOT_FOUND)
        data.is_active = True
        data.save()
        return Response('activated', status.HTTP_202_ACCEPTED)
