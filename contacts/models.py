from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from core.models import BaseModel


def validate_future_date(value):
    if value <= timezone.now().date():
        raise ValidationError("Travel date must be in the future.")


class Contact(BaseModel):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    is_reviewed = models.BooleanField(default=False)
    message = models.TextField()

    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        db_table = "contacts"
