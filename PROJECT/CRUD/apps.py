from django.apps import AppConfig


class CrudConfig(AppConfig):
    name = 'CRUD'

    def ready(self):
        import CRUD.signals