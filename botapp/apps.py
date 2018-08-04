from django.apps import AppConfig
from material.frontend.apps import ModuleMixin

class BotappConfig(ModuleMixin, AppConfig):
    name = 'botapp'
    icon = '<i class="material-icons">settings_applications</i>'
    verbose_name = 'Data collection'
    order = 2
