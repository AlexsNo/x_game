from django.apps import AppConfig
from django.core.signals import request_finished


class GameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'game'
    verbose_name = 'Main'

    def ready(self):
        from . import signals
