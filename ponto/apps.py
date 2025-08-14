from django.apps import AppConfig

class PontoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ponto'

    def ready(self):
        from .scheduler import iniciar_agendador
        iniciar_agendador()
