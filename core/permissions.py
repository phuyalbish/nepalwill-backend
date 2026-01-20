from rest_framework import generics
from rest_framework.permissions import (AllowAny, BasePermission,
                                        IsAuthenticated)
from rest_framework.views import APIView

from core.pagination import StandardPagination


class UserRolePermission(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.is_superuser:
            return True

        if user.is_admin:
            if obj.is_superuser:
                return False
            return True

        if user.is_staff:
            if obj.is_superuser or obj.is_admin:
                return False
            return obj.id == user.id

        return False


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, _):
        return request.user.is_superuser


class IsStaff(BasePermission):
    def has_permission(self, request, _):
        return request.user.is_staff


class AdminAPIView(APIView):
    permission_classes = [IsAdmin, IsAuthenticated]


class SuperAPIView(APIView):
    permission_classes = [IsSuperAdmin, IsAuthenticated]


class SuperAdminAPIView(APIView):
    permission_classes = [IsSuperAdmin | IsAdmin, IsAuthenticated]


class AllowAnyAPIView(APIView):
    permission_classes = [AllowAny]


class AuthenticatedAPIView(APIView):
    permission_classes = [IsAuthenticated]


class GenericsAuthenticatedAPIView(generics.ListAPIView):
    pagination_class = StandardPagination
    permission_classes = [IsAuthenticated]


class GenericsAdminAPIView(generics.ListAPIView):
    pagination_class = StandardPagination
    permission_classes = [IsAdmin, IsAuthenticated]


class GenericsSuperAdminAPIView(generics.ListAPIView):
    pagination_class = StandardPagination
    permission_classes = [IsSuperAdmin | IsAdmin, IsAuthenticated]


class GenericsSuperAPIView(generics.ListAPIView):
    pagination_class = StandardPagination
    permission_classes = [IsSuperAdmin, IsAuthenticated]


class GenericsAllowAnyAPIView(generics.ListAPIView):
    pagination_class = StandardPagination
    permission_classes = [AllowAny]
