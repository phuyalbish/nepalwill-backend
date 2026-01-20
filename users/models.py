from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from users.manager import AdminManager, StaffManager, UserManager


class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, null=False, unique=True)
    fullname = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()
    admin = AdminManager()
    staff = StaffManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return f"{self.username}"

    class Meta:
        db_table = "users"
