from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.form import UserAdminForm
from users.models import Users


class UserAdmin(BaseUserAdmin):
    add_form = UserAdminForm
    model = Users
    list_display = (
        "fullname",
        "username",
        "is_admin",
        "is_superuser",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("fullname",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_admin",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "fullname",
                    "password",
                    "is_admin",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("username", "fullname")
    ordering = ("username",)


admin.site.register(Users, UserAdmin)
