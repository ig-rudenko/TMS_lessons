from django.core.cache import cache


def get_or_cache(cache_key, queryset, timeout: int = 30) -> list:
    cached = cache.get(cache_key)
    if not cached:
        cached = list(queryset)
        cache.set(cache_key, cached, timeout=timeout)
    return cached
