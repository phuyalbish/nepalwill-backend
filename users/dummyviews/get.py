from rest_framework import filters
from rest_framework.response import Response

from core.permissions import (AdminAPIView, AuthenticatedAPIView,
                              GenericsAdminAPIView, GenericsSuperAdminAPIView,
                              SuperAdminAPIView)
from users.models import Users
from users.serializers import UserSerializer


class AdminDetailView(SuperAdminAPIView):
    def get(self, _, user_id):
        try:
            data = Users.admin.get(pk=user_id)
            serializer = UserSerializer(data, many=False)
        except Users.DoesNotExist:
            return Response({"detail": "No Admin Found"}, status=404)
        return Response(serializer.data)


class AdminListView(GenericsSuperAdminAPIView):
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("fullname", "username")

    def get_queryset(self):
        return Users.admin.all()


class StaffListView(GenericsAdminAPIView):
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("fullname", "username")

    def get_queryset(self):
        return Users.staff.all()


class StaffDetailView(AdminAPIView):
    def get(self, _, user_id):
        try:
            data = Users.staff.get(pk=user_id)
            serializer = UserSerializer(data, many=False)
            return Response(serializer.data)
        except Users.DoesNotExist:
            return Response({"detail": "No Staff Found"}, status=404)


class UserDetailView(AuthenticatedAPIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
