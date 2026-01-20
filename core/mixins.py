from cloudinary.exceptions import Error as CloudinaryError
from cloudinary.models import CloudinaryField
from cloudinary.uploader import destroy, upload
from django import forms
from django.db import models
from django.urls import reverse
from django.utils.html import format_html

from utils.save_image import convert_image_to_webp, generate_unique_filename


class HomeImageProcessingMixin(models.Model):
    image = models.ImageField(upload_to="default/", null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.image:
            try:
                old_instance = self.__class__.objects.get(pk=self.pk)
                image_changed = old_instance.image != self.image
                if image_changed and old_instance.image:
                    old_instance.image.delete(save=False)

            except self.__class__.DoesNotExist:
                image_changed = True

            if image_changed:
                if not self.image.name.lower().endswith(".webp"):
                    unique_filename = generate_unique_filename(".webp")
                    converted_file = convert_image_to_webp(self.image)
                    self.image.save(unique_filename, converted_file, save=False)
                else:
                    self.image.name = generate_unique_filename(".webp")

        super().save(*args, **kwargs)


class HomeIconProcessingMixin(models.Model):
    icon = models.ImageField(upload_to="default/", null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        if self.icon:
            self.icon.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.icon:
            try:
                old_instance = self.__class__.objects.get(pk=self.pk)
                icon_changed = old_instance.icon != self.icon
                if icon_changed and old_instance.icon:
                    old_instance.icon.delete(save=False)
            except self.__class__.DoesNotExist:
                icon_changed = True

            if icon_changed:
                if not self.icon.name.lower().endswith(".webp"):
                    unique_filename = generate_unique_filename(".webp")
                    converted_file = convert_image_to_webp(self.icon)
                    self.icon.save(unique_filename, converted_file, save=False)
                else:
                    self.icon.name = generate_unique_filename(".webp")

        super().save(*args, **kwargs)


class CloudinaryIconProcessingMixin(models.Model):

    icon = CloudinaryField("icon")

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.pk:
            old = self.__class__.objects.get(pk=self.pk)
            if old.icon and self.icon != old.icon:
                try:
                    destroy(old.image.public_id)
                except CloudinaryError as e:
                    print(f"Cloudinary destroy error: {e}")
                    pass

        if hasattr(self.icon, "file"):
            model_name = self.__class__.__name__.lower()
            uploaded = upload(
                self.icon,
                format="webp",
                folder=f"{model_name}/",
                transformation=[{"quality": "auto"}],
            )
            self.icon = uploaded["public_id"]

        super().save(*args, **kwargs)


class CloudinaryImageProcessingMixin(models.Model):
    image = CloudinaryField("image")

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.pk:
            old = self.__class__.objects.get(pk=self.pk)
            if old.image and self.image != old.image:
                try:
                    destroy(old.image.public_id)
                except CloudinaryError as e:
                    print(f"Cloudinary destroy error: {e}")
                    pass

        if hasattr(self.image, "file"):
            model_name = self.__class__.__name__.lower()
            uploaded = upload(
                self.image,
                format="webp",
                folder=f"{model_name}/",
                transformation=[{"quality": "auto"}],
            )
            self.image = uploaded["public_id"]

        super().save(*args, **kwargs)


class ImageSizeValidationMixin:
    MAX_IMAGE_SIZE = 9 * 1024 * 1024  # 9MB

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image and hasattr(image, "size") and image.size > self.MAX_IMAGE_SIZE:
            raise forms.ValidationError(
                "Image file size exceeds the maximum allowed size of 9 MB."
            )
        return image


class IconSizeValidationMixin:
    MAX_ICON_SIZE = 9 * 1024 * 1024  # 9MB

    def clean_icon(self):
        icon = self.cleaned_data.get("icon")
        if icon and hasattr(icon, "size") and icon.size > self.MAX_ICON_SIZE:
            raise forms.ValidationError(
                "Icon file size exceeds the maximum allowed size of 9 MB."
            )
        return icon


class DeleteLinkMixin:
    def delete_link(self, obj):
        url = reverse(
            f"admin:{obj._meta.app_label}_{obj._meta.model_name}_delete", args=[obj.pk]
        )
        return format_html(
            '<a class="button" href="{}" style="color:white; font-size:14px">Delete</a>',
            url,
        )

    delete_link.short_description = "Delete"
    delete_link.allow_tags = True
