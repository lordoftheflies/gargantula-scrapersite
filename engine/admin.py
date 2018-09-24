from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.translation import gettext as _

from . import models
# Register your models here.


class ArgumentInline(admin.TabularInline):
    model = models.ArgumentModel
    verbose_name_plural = _('Parameters')
    fk_name = 'process'
    fields = ['slug', 'friendly_name', 'description', 'data_type', 'default_value', 'tag']
    extra = 0


class PropertyInline(admin.TabularInline):
    model = models.ArgumentModel
    verbose_name_plural = _('Properties')
    fk_name = 'process'
    fields = ['slug', 'friendly_name', 'description', 'data_type', 'default_value', 'tag']
    extra = 0


@admin.register(models.ProcessModel)
class ProcessAdmin(ModelAdmin):
    fields = ['friendly_name', 'description', 'notebook']
    list_display = ['id', 'friendly_name', 'notebook_basename', 'description']
    icon = '<i class="material-icons">attachment</i>'
    inlines = [
        ArgumentInline,
        PropertyInline
    ]
