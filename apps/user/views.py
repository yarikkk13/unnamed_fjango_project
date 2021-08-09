from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, UserUpdateSerializer

UserModel: User = get_user_model()


class UserListCreateView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserRetrUpdView(RetrieveUpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserUpdateSerializer
    queryset = UserModel.objects.all()


class DeleteView(APIView):
    # def get(self, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     try:
    #         data = CarModel.objects.get(pk=pk)
    #     except Exception as e:
    #         return Response('Not Found')
    #     serializer = CarSerializer(data)
    #     return Response(serializer.data)

    permission_classes = (AllowAny,)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data = UserModel.objects.get(pk=pk)
        except Exception as e:
            return Response('Not Found', status.HTTP_404_NOT_FOUND)
        data.is_active = False
        data.deleted = True
        data.save()
        return Response('deleted', status.HTTP_204_NO_CONTENT)
