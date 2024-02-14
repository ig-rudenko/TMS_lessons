
from django.core.cache import cache
from django.db.models import QuerySet


def get_or_cache(cache_key: str, queryset: QuerySet, timeout: int = 30) -> list:
    cached = cache.get(cache_key)
    if not cached:
        cached = list(queryset)
        cache.set(cache_key, cached, timeout=timeout)
    return cached
