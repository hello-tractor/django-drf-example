from django.apps import AppConfig
from django.contrib import admin


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self) -> None:
        from .models import Farmer
        admin.register(Farmer)
        return super().ready()
