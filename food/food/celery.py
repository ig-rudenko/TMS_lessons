import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food.settings')

app = Celery('food')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()  # Celery сам найдет задачи (в приложениях).
