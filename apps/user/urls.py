from django.urls import path

from .views import DeleteView, UserListCreateView, UserRetrUpdView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    # path('/<int:pk>', DeleteView.as_view(), name='soft_delete'),
    path('/<int:pk>', UserRetrUpdView.as_view(), name='retr_upd'),
]
