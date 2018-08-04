from random import randint

import dateutil
import radar
from django.core.management.base import BaseCommand, CommandError
# from mdm import models as mdm_models
# from botapp import models as bot_models
import mdm
import botapp
from datastore import models as data_models
from mdm import models as mdm_models
import reportsapp
import report_builder
from django.utils.timezone import make_aware, get_current_timezone


class Command(BaseCommand):
    help = 'Generate random best-offer data'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)
        parser.add_argument('min_lowest_price', type=int)
        parser.add_argument('max_lowest_price', type=int)
        parser.add_argument('min_bag_price', type=int)
        parser.add_argument('max_bag_price', type=int)
        parser.add_argument('min_timestamp', type=str)
        parser.add_argument('max_timestamp', type=str)
        parser.add_argument('duration', type=int)
        parser.add_argument('pax', type=int)

    def handle(self, *args, **options):
        count = options['count']
        min_lowest_price = options['min_lowest_price']
        max_lowest_price = options['max_lowest_price']
        min_bag_price = options['min_bag_price']
        max_bag_price = options['max_bag_price']
        min_timestamp = options['min_timestamp']
        max_timestamp = options['max_timestamp']
        pax = options['pax']
        duration = options['duration']

        index = 0
        while (index < count):
            generated_lowest_price = randint(min_lowest_price, max_lowest_price)
            generated_bag_price = randint(min_bag_price, max_bag_price)
            generated_timestamp = radar.random_date(start=min_timestamp, stop=max_timestamp)
            generated_supplier = randint(1, mdm_models.SupplierModel.objects.count())
            generated_market = randint(1, mdm_models.MarketModel.objects.count())
            generated_departure = randint(1, mdm_models.AirportModel.objects.count())
            generated_arrival = randint(1, mdm_models.AirportModel.objects.count())
            # '2008-04-10 11:47:58-05'
            item = data_models.BestOfferModel.objects.create(
                timestamp=generated_timestamp,
                duration=duration,
                supplier=mdm_models.SupplierModel.objects.get(id=generated_supplier),
                market=mdm_models.MarketModel.objects.get(id=generated_market),
                departure=mdm_models.AirportModel.objects.get(id=generated_departure),
                arrival=mdm_models.AirportModel.objects.get(id=generated_arrival),

                lowest_price=generated_lowest_price,
                bag_weight='20',
                bag_price=generated_bag_price
            )
            self.stdout.write(str(item))
            index = index + 1

        self.stdout.write(self.style.SUCCESS('Successfully generated %s best-offer model' % (count)))
