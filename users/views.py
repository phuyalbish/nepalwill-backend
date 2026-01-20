from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core.permissions import IsAdmin, IsSuperAdmin, UserRolePermission
from users.models import Users
from users.serializers import UserSerializer


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class CredentialView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        password = request.data.get("password")
        if not password:
            return Response(
                "Password field is required", status=status.HTTP_400_BAD_REQUEST
            )
        try:
            user = Users.objects.get(id=request.user.id)
        except Users.DoesNotExist:
            return Response("User doesn't exist", status=status.HTTP_401_UNAUTHORIZED)
        if not user.check_password(password):
            return Response("Wrong Password", status=status.HTTP_401_UNAUTHORIZED)
        return Response("Valid User", status=status.HTTP_200_OK)


class AdminListView(generics.ListAPIView):
    permission_classes = [IsSuperAdmin, IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return Users.admin.all()


class StaffListView(generics.ListAPIView):
    permission_classes = [IsAdmin, IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return Users.staff.all()


class UserViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserRolePermission]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Users.objects.all()
        elif user.is_admin:
            return Users.objects.exclude(is_superuser=True)
        elif user.is_staff:
            return Users.objects.filter(id=user.id)
        return Users.objects.none()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "User created successfully!", "data": response.data},
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {"message": "User updated successfully!", "data": response.data},
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response(
            {"message": "User deleted successfully!"}, status=status.HTTP_204_NO_CONTENT
        )
