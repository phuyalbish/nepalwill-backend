from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import Users


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = Users.objects.filter(username=username).first()
        if user and user.check_password(password):
            data = super().validate({"username": user.username, "password": password})
            data["user"] = {
                "id": user.id,
                "username": user.username,
                "fullname": user.fullname,
                "is_admin": user.is_admin,
                "is_superuser": user.is_superuser,
                "is_staff": user.is_staff,
            }
            return data

        raise serializers.ValidationError("Invalid username or password")
