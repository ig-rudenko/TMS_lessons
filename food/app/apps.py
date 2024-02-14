from django.apps import AppConfig as AppConfigClass


class AppConfig(AppConfigClass):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
