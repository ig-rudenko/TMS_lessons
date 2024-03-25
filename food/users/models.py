from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    tg_id = models.IntegerField(null=True, blank=True, unique=True, db_index=True)
