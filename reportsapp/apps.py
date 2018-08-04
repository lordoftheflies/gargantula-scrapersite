from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class ReportsappConfig(ModuleMixin, AppConfig):
    name = 'reportsapp'
    icon = '<i class="material-icons">settings_applications</i>'
    verbose_name = 'Reporting'
    order = 4