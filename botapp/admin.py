from django.contrib import admin
from botapp import models as bot_models
from django.contrib.admin import ModelAdmin


# Register your models here.
#
# class ParameterInline(admin.TabularInline):
#     fields = ['argument', 'data_value']
#     extra = 0
#
#     def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
#         """enable ordering drop-down alphabetically"""
#         if db_field.name == 'argument':
#             kwargs['queryset'] = self.get_queryset_for_type(**kwargs)
#         return super(ParameterInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
#
#     def get_queryset_for_type(self, **kwargs):
#         raise NotImplementedError('Custom parameter queryset definition is mandatory')
#
#
# class TextParameterInline(ParameterInline):
#     model = bot_models.TextParameterModel
#
#     def get_queryset_for_type(self, **kwargs):
#         return bot_models.TextPropertyModel.objects.all()
#
#
# class NumberParameterInline(ParameterInline):
#     model = bot_models.NumberParameterModel
#
#     def get_queryset_for_type(self, **kwargs):
#         return bot_models.NumberPropertyModel.objects.all()
#
#
# class EnumerationParameterInline(ParameterInline):
#     model = bot_models.EnumerationParameterModel
#
#     def get_queryset_for_type(self, **kwargs):
#         return bot_models.EnumerationPropertyModel.objects.all()
#
#
# class DateParameterInline(ParameterInline):
#     model = bot_models.DateParameterModel
#
#     def get_queryset_for_type(self, **kwargs):
#         return bot_models.DatePropertyModel.objects.all()
#
#
# @admin.register(bot_models.TextPropertyModel)
# class TextPropertyAdmin(ModelAdmin):
#     icon = '<i class="material-icons">attachment</i>'
#
#
# @admin.register(bot_models.NumberPropertyModel)
# class NumberPropertyAdmin(ModelAdmin):
#     icon = '<i class="material-icons">attachment</i>'
#
#
# @admin.register(bot_models.EnumerationPropertyModel)
# class EnumerationPropertyAdmin(ModelAdmin):
#     icon = '<i class="material-icons">attachment</i>'


@admin.register(bot_models.PortalModel)
class PortalAdmin(ModelAdmin):
    fields = ('name', 'version', 'spider', 'supplier', 'lua_source')
    icon = '<i class="material-icons">attachment</i>'
    # inlines = [TextParameterInline, NumberParameterInline, EnumerationParameterInline, DateParameterInline]

@admin.register(bot_models.ComparisonModel)
class ComparisonAdmin(ModelAdmin):
    fields = ('name', 'subject', 'competitors')
    icon = '<i class="material-icons">attachment</i>'

#
# @admin.register(bot_models.PropertyModel)
# class PortalPropertyAdmin(ModelAdmin):
#     fields = ('name', 'display_name', 'argument_type', 'default_value')
#     icon = '<i class="material-icons">attachment</i>'
