from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class DatastoreConfig(ModuleMixin, AppConfig):
    name = 'datastore'
    icon = '<i class="material-icons">settings_applications</i>'
    verbose_name = 'Datastore'
    order = 2
