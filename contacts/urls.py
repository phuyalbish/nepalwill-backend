from django.urls import path

from contacts.views import (ContactCreateView)

urlpatterns = [
    path("contact/create/", ContactCreateView.as_view(), name="contact-create"),
]
