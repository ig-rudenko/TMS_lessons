from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


def get_fake_image() -> SimpleUploadedFile:
    img = Image.new('RGB', (20, 20), 'black')
    image_data = BytesIO()
    img.save(image_data, 'PNG')
    return SimpleUploadedFile("image.png", image_data.getvalue(), "image/png")
