from django.db import models


class DateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModel(DateModel):
    class Meta:
        abstract = True
        ordering = ["-created_at", "-modified_at"]


class BaseSlugModel(BaseModel):
    slug = models.SlugField(unique=True, null=False, blank=False, help_text="The unique URL identifier for this component. Changing this after the profile is public will break existing links.")

    class Meta:
        abstract = True
