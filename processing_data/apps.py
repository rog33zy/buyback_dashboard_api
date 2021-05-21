import processing_data
from django.apps import AppConfig


class ProcessingDataConfig(AppConfig):
    name = "processing_data"

    def ready(self):
        import processing_data.signals
