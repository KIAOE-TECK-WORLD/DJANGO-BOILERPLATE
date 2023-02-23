from django.contrib.auth.models import BaseUserManager
from django.db import models

from .enums import UserType


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have a username number.')

        user = self.model(
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user


# class HostManager(models.Manager):
#     def get_queryset(self, *args, **kwargs):
#         return super() \
#             .get_queryset(*args, **kwargs) \
#             .filter(category=UserType.host())


# class ClientManager(models.Manager):
#     def get_queryset(self, *args, **kwargs):
#         return super() \
#             .get_queryset(*args, **kwargs) \
#             .filter(category=UserType.client())
