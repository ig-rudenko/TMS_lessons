from django.test import TestCase
from django.core.cache import cache

from ..cache import get_or_cache
from ..models import Ingredient


class TestCache(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.cache_key = "test_get_or_cache"

    def setUp(self):
        Ingredient.objects.create(name="name")

    def tearDown(self):
        cache.clear()

    def test_get_or_cache_1(self):
        valid_data = list(Ingredient.objects.all())  # Обращение к базе.

        with self.assertNumQueries(1):  # Кол-во запросов к базе - 1.
            self.assertListEqual(
                valid_data,
                get_or_cache(self.cache_key, Ingredient.objects.all())  # Обращение к базе.
            )

        with self.assertNumQueries(0):  # Обращения к базе НЕТ.
            self.assertListEqual(
                valid_data,
                get_or_cache(self.cache_key, Ingredient.objects.all()),
            )

        self.assertListEqual(
            valid_data,
            cache.get(self.cache_key),
        )
