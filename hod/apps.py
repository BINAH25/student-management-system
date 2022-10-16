from django.apps import AppConfig


class HodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hod'
    def ready(self):
        from .import signals


