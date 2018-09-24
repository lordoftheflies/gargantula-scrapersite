import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class EngineConfig(AppConfig):
    name = 'engine'

    def ready(self):
        logger.info('%s started: OK', (self.name))
