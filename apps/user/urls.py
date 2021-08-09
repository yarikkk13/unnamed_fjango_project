from django.urls import path

from .views import DeleteView, UserActivatorView, UserChangePasswordView, UserListCreateView, UserRetrUpdView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    # path('/<int:pk>', DeleteView.as_view(), name='soft_delete'),
    path('/<int:pk>', UserRetrUpdView.as_view(), name='retr_upd'),
    path('/<int:pk>/change_password', UserChangePasswordView.as_view(), name='change_password'),
    path('/<int:pk>/activate', UserActivatorView.as_view(), name='change_password'),
]
