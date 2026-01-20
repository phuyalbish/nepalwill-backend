from django.db import models
class AllManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()


class HiddenManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_hidden=True)


class NonHiddenManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_hidden=False)
