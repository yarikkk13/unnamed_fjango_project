from django.urls import path

from .views import UserActivatorView, UserChangePasswordView, UserListCreateView, UserRetrieveUpdateSoftDeleteView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/<int:pk>', UserRetrieveUpdateSoftDeleteView.as_view(), name='user_byId_retrieve_update_softDelete'),
    path('/<int:pk>/change_password', UserChangePasswordView.as_view(), name='user_change_password'),
    path('/<int:pk>/activate', UserActivatorView.as_view(), name='user_activate_account_by_patch_method'),
]
