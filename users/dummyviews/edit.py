from rest_framework import status
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.response import Response

from core.permissions import AdminAPIView, SuperAdminAPIView
from users.models import Users
from users.serializers import UserSerializer


class StaffUpdateView(AdminAPIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def patch(self, request, user_id):
        try:
            user = Users.staff.get(id=user_id)
        except Users.DoesNotExist:
            return Response({"msg": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)

        try:
            Users.objects.exclude(username=request.data["username"]).get(
                username=request.data["username"]
            )
            return Response("Username already used", status=status.HTTP_400_BAD_REQUEST)
        except Users.DoesNotExist:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminUpdateView(SuperAdminAPIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def patch(self, request, user_id):
        try:
            user = Users.admin.get(id=user_id)
        except Users.DoesNotExist:
            return Response({"msg": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)

        try:
            Users.objects.exclude(username=request.data["username"]).get(
                username=request.data["username"]
            )
            return Response("Username already used", status=status.HTTP_400_BAD_REQUEST)
        except Users.DoesNotExist:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
