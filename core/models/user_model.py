from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from core.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'
        app_label = 'core'

    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
