import json

from django.db import models
from django.utils import timezone
from mdm import models as mdm_models


class BestOfferModel(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    timestamp = models.DateField(default=timezone.now)
    duration = models.IntegerField(null=True, blank=True, default=0)
    supplier = models.ForeignKey(mdm_models.SupplierModel, null=True, blank=True, default=None, on_delete=models.CASCADE)
    market = models.ForeignKey(mdm_models.MarketModel, null=True, blank=True, default=None, on_delete=models.CASCADE)
    departure = models.ForeignKey(mdm_models.AirportModel, related_name='departures', null=True, blank=True, default=None, on_delete=models.CASCADE)
    arrival = models.ForeignKey(mdm_models.AirportModel, related_name='arrivals', null=True, blank=True, default=None, on_delete=models.CASCADE)

    lowest_price = models.CharField(max_length=200, null=True, blank=True, default=None)
    bag_weight = models.CharField(max_length=200, null=True, blank=True, default=None)
    bag_price = models.CharField(max_length=200, null=True, blank=True, default=None)

    @property
    def arrival_name(self):
        return self.arrival.display_name

    @property
    def departure_name(self):
        return self.departure.display_name

    @property
    def supplier_name(self):
        return self.supplier.display_name

    @property
    def market_name(self):
        return self.market.display_name

    @property
    def bag_price_per_person(self):
        return self.bag_price if self.bag_price is not None else 0

    @property
    def hotel_only_price(self):
        return self.bag_price if self.bag_price is not None else 0

    @property
    def flight_only_price(self):
        return self.lowest_price if self.lowest_price is not None else 0

    @property
    def flight_price_with_bag(self):
        return self.flight_only_price + self.bag_price_per_person

    @property
    def package_price(self):
        return self.flight_only_price + self.hotel_only_price

    @property
    def full_package_price(self):
        return self.flight_only_price + self.hotel_only_price + self.bag_price_per_person

    def to_dict(self):
        map = self.input_parameters()
        map['lowest_price'] = self.lowest_price
        map['bag_weight'] = self.bag_weight
        map['bag_price'] = self.bag_price
        return map

    def input_parameters(self):
        return {
            'timestamp': self.timestamp,
            'duration': self.duration,
            'supplier': None if self.supplier is None else self.supplier.id,
            'market': None if self.market is None else self.market.id,
            'departure': None if self.departure is None else self.departure.id,
            'arrival': None if self.arrival is None else self.arrival.id
        }

    def __str__(self):
        return json.dumps(self.to_dict())
