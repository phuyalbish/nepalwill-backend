from random import shuffle
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView

from core.serializers import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


def custom_404(request, _):
    return render(request, "404.html", status=404)
