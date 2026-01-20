from rest_framework import serializers

from .models import Users


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password", "placeholder": "Password"},
    )

    class Meta:
        model = Users
        fields = [
            "id",
            "username",
            "fullname",
            "password",
            "is_active",
            "is_admin",
            "is_staff",
            "is_superuser",
        ]
        read_only_fields = ["is_active", "is_staff", "is_superuser"]

    def create(self, validated_data):
        user = Users(
            username=validated_data["username"],
            fullname=validated_data.get("fullname", ""),
            is_admin=validated_data.get("is_admin", False),
            is_superuser=False,
            is_staff=True,
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        validated_data.pop("is_superuser", None)
        validated_data.pop("is_staff", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)
        instance.save()
        return instance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["fullname"]
