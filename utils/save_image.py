import secrets
from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image


def generate_unique_filename(extension=".webp"):
    random_string = secrets.token_hex(8)
    return f"{random_string}{extension}"


def convert_image_to_webp(image_field):
    img = Image.open(image_field)
    img = img.convert("RGBA")
    buffer = BytesIO()
    img.save(buffer, format="WEBP", quality=85)
    return ContentFile(buffer.getvalue())
