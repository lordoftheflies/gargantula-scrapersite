from django.apps import AppConfig
from material.frontend.apps import ModuleMixin
from django.template import Template

class MdmConfig(AppConfig):
    name = 'mdm'
    icon = '<i class="material-icons">settings_applications</i>'
    verbose_name = 'Master data'
    order = 1
    #
    # def menu(self):
    #     """Load module menu template.
    #
    #     Template should be located in `<app_label>/menu.html`
    #
    #     If no template exists, no exception raised.
    #
    #     Intended to use with {% include %} template tag::
    #
    #         {% include module.menu %}
    #     """
    #     return Template('')