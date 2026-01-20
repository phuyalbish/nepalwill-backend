from django.db import models

from core.mixins import HomeImageProcessingMixin
from core.models import  BaseSlugModel
from core.manager import AllManager, NonHiddenManager, HiddenManager


class Dummy(BaseSlugModel, HomeImageProcessingMixin):
    
    name = models.CharField(
        max_length=50, 
    )
    image = models.ImageField(
        upload_to="dummys/images/", 
        null=True, 
        blank=True,
    )
    is_hidden = models.BooleanField(
        default=False, 
    )

    objects = AllManager()
    shown = NonHiddenManager()
    hidden = HiddenManager()

    class Meta:
        db_table = "dummys"

    def __str__(self):
        return f"{self.name} ({self.dummy_type})"
    

    # def delete(self, *args, **kwargs):
    #     if self.image:
    #         try:
    #             destroy(self.image.public_id)
    #         except:
    #             pass 
    #     super().delete(*args, **kwargs)