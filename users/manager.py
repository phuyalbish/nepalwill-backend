from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Username is Required")
        if not password:
            raise ValueError("Password is Required")
        username = username.strip().lower()
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        return self.create_user(username, password, **extra_fields)

    def create_admin(self, username, password, **kwargs):
        if not username:
            raise ValueError("Username is required")
        if not password:
            raise ValueError("Password is Required")
        kwargs.setdefault("is_admin", True)
        kwargs.setdefault("is_superuser", False)
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def get_admin(self):
        try:
            res = (
                super()
                .get_queryset()
                .filter(is_staff=True)
                .filter(is_deleted=False, is_disabled=False)
            )
        except AttributeError:
            return "No Data Found"
        return res


# class SuperUserManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_superuser=True, )


class AdminManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True, is_superuser=False)


class StaffManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_superuser=False, is_admin=False)
