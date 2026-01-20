from rest_framework import status
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.response import Response

from core.permissions import AdminAPIView, SuperAdminAPIView
from users.models import Users
from users.serializers import UserSerializer


class StaffCreateView(AdminAPIView):
    def post(self, request):
        try:
            Users.objects.get(username=request.data["username"])
            return Response("Username already used", status=status.HTTP_400_BAD_REQUEST)
        except Users.DoesNotExist:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response = Response(serializer.data)
            else:
                response = Response(serializer.errors, status=422)
            return response


class AdminCreateView(SuperAdminAPIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def post(self, request):
        try:
            Users.objects.get(username=request.data["username"])
            return Response("Username already used", status=status.HTTP_400_BAD_REQUEST)
        except Users.DoesNotExist:
            request.data["is_admin"] = True
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                return Response(serializer.data)
            return Response(serializer.errors, status=422)
