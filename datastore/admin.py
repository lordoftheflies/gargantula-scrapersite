from datastore import models as datastore_models
# Register your models here.
from django.contrib import admin

@admin.register(datastore_models.BestOfferModel)
class BestOfferAdmin(admin.ModelAdmin):
    fields = ['timestamp', 'duration', 'supplier', 'market', 'departure', 'arrival', 'lowest_price', 'bag_weight', 'bag_price']
    icon = '<i class="material-icons">attachment</i>'
    list_display = ['timestamp', 'duration', 'supplier', 'market', 'departure', 'arrival', 'lowest_price', 'bag_weight', 'bag_price']

# @admin.register(datastore_models.ReservationModel)
# class ReservationAdmin(admin.ModelAdmin):
#     fields = ['hotel', 'room_type', 'board']
#     # inlines = [PricePerPersonInline]
#
# @admin.register(datastore_models.RouteModel)
# class RouteAdmin( admin.ModelAdmin):
#     fields = ['flight_provider', 'departure', 'arrival', 'cheapest_out', 'cheapest_return', 'bag_type']
#     # inlines = [PricePerPersonInline]
#
#
# @admin.register(datastore_models.JourneyModel)
# class JourneyAdmin( admin.ModelAdmin):
#     fields = ['date', 'number_of_nights', 'number_of_passengers', 'stay', 'inbound_carrier', 'outbound_carrier']
#     inlines = [PricePerPersonInline]
