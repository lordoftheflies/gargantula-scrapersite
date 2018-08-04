from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class CubesviewerConfig(ModuleMixin, AppConfig):
    name = 'cubesviewer'
    icon = '<i class="material-icons">settings_applications</i>'
    verbose_name = 'Olap'
    order = 5