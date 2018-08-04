from mdm import models as mdm_models
from django.contrib import admin


# Register your models here.


@admin.register(mdm_models.SupplierModel)
class SupplierAdmin(admin.ModelAdmin):
    fields = ('portal', 'display_name', 'description')
    icon = '<i class="material-icons">attachment</i>'
    list_display = ['display_name', 'portal']


@admin.register(mdm_models.BagTypeModel)
class BagTypeAdmin(admin.ModelAdmin):
    fields = ('display_name', 'weight', 'description')
    icon = '<i class="material-icons">attachment</i>'


@admin.register(mdm_models.MarketModel)
class MarketAdmin(admin.ModelAdmin):
    fields = ('display_name', 'code', 'description')
    icon = '<i class="material-icons">attachment</i>'


@admin.register(mdm_models.AirportModel)
class AirportAdmin(admin.ModelAdmin):
    fields = ('display_name', 'code', 'description')
    icon = '<i class="material-icons">attachment</i>'


@admin.register(mdm_models.FlightProviderModel)
class FlightProviderAdmin(admin.ModelAdmin):
    fields = ('display_name', 'code', 'description')
    icon = '<i class="material-icons">attachment</i>'
    list_display = ['code', 'display_name']


@admin.register(mdm_models.HotelModel)
class HotelAdmin(admin.ModelAdmin):
    fields = ('display_name', 'stars', 'description', 'market')
    icon = '<i class="material-icons">attachment</i>'


@admin.register(mdm_models.BoardModel)
class BoardAdmin(admin.ModelAdmin):
    fields = ('display_name', 'code', 'description')
    icon = '<i class="material-icons">attachment</i>'


@admin.register(mdm_models.RoomTypeModel)
class RoomTypeAdmin(admin.ModelAdmin):
    fields = ('display_name', 'code', 'description')
    icon = '<i class="material-icons">attachment</i>'
