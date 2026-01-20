from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.permissions import AllowAnyAPIView
from dummys.models import  Dummy
from dummys.serializer import ( DummySerializer)

class DummyViewSet(ModelViewSet):
    queryset = Dummy.objects.all()
    serializer_class = DummySerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(modified_at=timezone.now())

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "Dummy created successfully!", "data": response.data},
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {"message": "Dummy updated successfully!", "data": response.data},
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response(
            {"message": "Dummy deleted successfully!"}, status=status.HTTP_204_NO_CONTENT
        )

class DummyDetailView(AllowAnyAPIView):
    def get(self, _, dummy_slug):
        try:
            dummy = Dummy.shown.get(slug=dummy_slug)
        except Dummy.DoesNotExist:
            return Response(
                {"error": "Dummy not found."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = DummySerializer(dummy)
        return Response(serializer.data, status=status.HTTP_200_OK)

