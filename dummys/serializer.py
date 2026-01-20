from rest_framework import serializers
from dummys.models import (
    Dummy
)

class DummySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dummy
        fields = "__all__"
