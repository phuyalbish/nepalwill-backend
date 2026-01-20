from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import (AdminListView, CredentialView, StaffListView,
                         UserDetailView, UserViewSet)

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path("admin/", AdminListView.as_view(), name="get_admin"),
    path("staff/", StaffListView.as_view(), name="get_staff"),
    path("credential/", CredentialView.as_view(), name="credential"),
    path("user/", UserDetailView.as_view(), name="logged_in_user"),
    path("", include(router.urls)),
]
