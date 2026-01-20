from django.urls import include, path
from rest_framework.routers import DefaultRouter
from dummys.views import (DummyViewSet, DummyDetailView) 
router = DefaultRouter()
router.register(r"dummys", DummyViewSet, basename="dummy")

urlpatterns = [
    path("dummys/detail/<slug:dummy_slug>/", DummyDetailView.as_view(), name="get-dummys"),
    path("", include(router.urls)),
]
