import os

from django import template
from django.core.files.storage import default_storage

register = template.Library()


@register.filter
def get_storage_url(file) -> str:
    url = default_storage.url(file)
    minio_custom_url = os.environ.get("MINIO_CUSTOM_URL", "")
    if minio_custom_url:
        url = url.replace(os.environ.get('MINIO_ENDPOINT_URL'), minio_custom_url)
    return url
