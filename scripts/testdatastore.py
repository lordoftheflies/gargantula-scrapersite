#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones inteact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# ./manage.py dumpscript datastore
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script
import os, sys
from django.db import transaction

class BasicImportHelper(object):

    def pre_import(self):
        pass

    @transaction.atomic
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    # From Python 3.3 we can check e.name - string match is for backward compatibility.
    if 'import_helper' in str(e):
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports
    from mdm.models import FlightProviderModel
    from mdm.models import SupplierModel
    from mdm.models import BagTypeModel
    from mdm.models import MarketModel
    from mdm.models import HotelModel
    from mdm.models import RoomTypeModel
    from mdm.models import BoardModel
    from mdm.models import AirportModel

    # Processing model: datastore.models.FlightPriceModel

    from datastore.models import FlightPriceModel


    # Processing model: datastore.models.ReservationModel

    from datastore.models import ReservationModel

    datastore_reservationmodel_1 = ReservationModel()
    datastore_reservationmodel_1.hotel =  importer.locate_object(HotelModel, "entitymodel_ptr", EntityModel, "id", 10, {'display_name': 'Holiday Palace', 'entitymodel_ptr_id': 10, 'stars': 3, 'description': 'Hotel Holiday Palace.', '_entitymodel_ptr_cache': 'Holiday Palace', 'market_id': 2, 'id': 10} ) 
    datastore_reservationmodel_1.room_type =  importer.locate_object(RoomTypeModel, "entitymodel_ptr", EntityModel, "id", 3, {'display_name': 'Single', 'entitymodel_ptr_id': 3, 'description': 'Room for single person.', 'code': 'SINGLE', '_entitymodel_ptr_cache': 'Single', 'id': 3} ) 
    datastore_reservationmodel_1.board =  importer.locate_object(BoardModel, "entitymodel_ptr", EntityModel, "id", 5, {'display_name': 'Half-board', 'entitymodel_ptr_id': 5, 'description': 'Meal basis is half-board.', 'code': 'HB', '_entitymodel_ptr_cache': 'Half-board', 'id': 5} ) 
    datastore_reservationmodel_1 = importer.save_or_locate(datastore_reservationmodel_1)

    # Processing model: datastore.models.RouteModel

    from datastore.models import RouteModel

    datastore_routemodel_1 = RouteModel()
    datastore_routemodel_1.flight_provider =  importer.locate_object(FlightProviderModel, "entitymodel_ptr", EntityModel, "id", 11, {'display_name': 'RyanAir', 'entitymodel_ptr_id': 11, 'description': 'RyanAir flights.', 'code': 'FR', '_entitymodel_ptr_cache': 'RyanAir', 'id': 11} ) 
    datastore_routemodel_1.departure =  importer.locate_object(AirportModel, "entitymodel_ptr", EntityModel, "id", 14, {'display_name': 'Luton', 'entitymodel_ptr_id': 14, 'description': 'United Kingdom, London, Luton', 'code': 'LTN', '_entitymodel_ptr_cache': 'Luton', 'market_id': 2, 'id': 14} ) 
    datastore_routemodel_1.arrival =  importer.locate_object(AirportModel, "entitymodel_ptr", EntityModel, "id", 14, {'display_name': 'Luton', 'entitymodel_ptr_id': 14, 'description': 'United Kingdom, London, Luton', 'code': 'LTN', '_entitymodel_ptr_cache': 'Luton', 'market_id': 2, 'id': 14} ) 
    datastore_routemodel_1.cheapest_out = dateutil.parser.parse("02:00:00")
    datastore_routemodel_1.cheapest_return = dateutil.parser.parse("05:00:00")
    datastore_routemodel_1.bag_type =  importer.locate_object(BagTypeModel, "entitymodel_ptr", EntityModel, "id", 12, {'display_name': 'Lower bag type', 'weight': 15, 'entitymodel_ptr_id': 12, 'description': None, '_entitymodel_ptr_cache': 'Lower bag type', 'id': 12} ) 
    datastore_routemodel_1 = importer.save_or_locate(datastore_routemodel_1)

    datastore_routemodel_2 = RouteModel()
    datastore_routemodel_2.flight_provider =  importer.locate_object(FlightProviderModel, "entitymodel_ptr", EntityModel, "id", 11, {'display_name': 'RyanAir', 'entitymodel_ptr_id': 11, 'description': 'RyanAir flights.', 'code': 'FR', '_entitymodel_ptr_cache': 'RyanAir', 'id': 11} ) 
    datastore_routemodel_2.departure =  importer.locate_object(AirportModel, "entitymodel_ptr", EntityModel, "id", 14, {'display_name': 'Luton', 'entitymodel_ptr_id': 14, 'description': 'United Kingdom, London, Luton', 'code': 'LTN', '_entitymodel_ptr_cache': 'Luton', 'market_id': 2, 'id': 14} ) 
    datastore_routemodel_2.arrival =  importer.locate_object(AirportModel, "entitymodel_ptr", EntityModel, "id", 14, {'display_name': 'Luton', 'entitymodel_ptr_id': 14, 'description': 'United Kingdom, London, Luton', 'code': 'LTN', '_entitymodel_ptr_cache': 'Luton', 'market_id': 2, 'id': 14} ) 
    datastore_routemodel_2.cheapest_out = dateutil.parser.parse("02:00:00")
    datastore_routemodel_2.cheapest_return = dateutil.parser.parse("04:00:00")
    datastore_routemodel_2.bag_type =  importer.locate_object(BagTypeModel, "entitymodel_ptr", EntityModel, "id", 12, {'display_name': 'Lower bag type', 'weight': 15, 'entitymodel_ptr_id': 12, 'description': None, '_entitymodel_ptr_cache': 'Lower bag type', 'id': 12} ) 
    datastore_routemodel_2 = importer.save_or_locate(datastore_routemodel_2)

    # Processing model: datastore.models.JourneyModel

    from datastore.models import JourneyModel

    datastore_journeymodel_1 = JourneyModel()
    datastore_journeymodel_1.date = dateutil.parser.parse("2017-09-25")
    datastore_journeymodel_1.number_of_nights = 7
    datastore_journeymodel_1.number_of_passengers = 12
    datastore_journeymodel_1.stay = datastore_reservationmodel_1
    datastore_journeymodel_1 = importer.save_or_locate(datastore_journeymodel_1)

    datastore_journeymodel_1.inbound_carrier.add(datastore_routemodel_1)
    datastore_journeymodel_1.outbound_carrier.add(datastore_routemodel_2)

    # Processing model: datastore.models.PricePerPersonModel

    from datastore.models import PricePerPersonModel

    datastore_priceperpersonmodel_1 = PricePerPersonModel()
    datastore_priceperpersonmodel_1.journey = datastore_journeymodel_1
    datastore_priceperpersonmodel_1.supplier = None
    datastore_priceperpersonmodel_1.larger_bag_price = '1'
    datastore_priceperpersonmodel_1.larger_bag_weight = '1'
    datastore_priceperpersonmodel_1.lower_bag_price = '1'
    datastore_priceperpersonmodel_1.lower_bag_weight = '1'
    datastore_priceperpersonmodel_1.lowest_price = '1'
    datastore_priceperpersonmodel_1 = importer.save_or_locate(datastore_priceperpersonmodel_1)

    datastore_priceperpersonmodel_2 = PricePerPersonModel()
    datastore_priceperpersonmodel_2.journey = datastore_journeymodel_1
    datastore_priceperpersonmodel_2.supplier =  importer.locate_object(SupplierModel, "entitymodel_ptr", EntityModel, "id", 8, {'display_name': 'Ryanair Holidays', 'entitymodel_ptr_id': 8, 'description': 'Main portal of RyanAir Holidays.', '_entitymodel_ptr_cache': 'Ryanair Holidays', 'id': 8, 'portal': 'http://holidays.ryanair.com/?market=uk&lang=en&currency=GBP'} ) 
    datastore_priceperpersonmodel_2.larger_bag_price = '1.05'
    datastore_priceperpersonmodel_2.larger_bag_weight = '2000.21'
    datastore_priceperpersonmodel_2.lower_bag_price = '12.01'
    datastore_priceperpersonmodel_2.lower_bag_weight = '1230.20'
    datastore_priceperpersonmodel_2.lowest_price = '120'
    datastore_priceperpersonmodel_2 = importer.save_or_locate(datastore_priceperpersonmodel_2)

    datastore_priceperpersonmodel_3 = PricePerPersonModel()
    datastore_priceperpersonmodel_3.journey = datastore_journeymodel_1
    datastore_priceperpersonmodel_3.supplier =  importer.locate_object(SupplierModel, "entitymodel_ptr", EntityModel, "id", 8, {'display_name': 'Ryanair Holidays', 'entitymodel_ptr_id': 8, 'description': 'Main portal of RyanAir Holidays.', '_entitymodel_ptr_cache': 'Ryanair Holidays', 'id': 8, 'portal': 'http://holidays.ryanair.com/?market=uk&lang=en&currency=GBP'} ) 
    datastore_priceperpersonmodel_3.larger_bag_price = '1'
    datastore_priceperpersonmodel_3.larger_bag_weight = '2'
    datastore_priceperpersonmodel_3.lower_bag_price = '122'
    datastore_priceperpersonmodel_3.lower_bag_weight = '334'
    datastore_priceperpersonmodel_3.lowest_price = '2222'
    datastore_priceperpersonmodel_3 = importer.save_or_locate(datastore_priceperpersonmodel_3)

    datastore_priceperpersonmodel_4 = PricePerPersonModel()
    datastore_priceperpersonmodel_4.journey = datastore_journeymodel_1
    datastore_priceperpersonmodel_4.supplier =  importer.locate_object(SupplierModel, "entitymodel_ptr", EntityModel, "id", 8, {'display_name': 'Ryanair Holidays', 'entitymodel_ptr_id': 8, 'description': 'Main portal of RyanAir Holidays.', '_entitymodel_ptr_cache': 'Ryanair Holidays', 'id': 8, 'portal': 'http://holidays.ryanair.com/?market=uk&lang=en&currency=GBP'} ) 
    datastore_priceperpersonmodel_4.larger_bag_price = '233.05'
    datastore_priceperpersonmodel_4.larger_bag_weight = '233.05'
    datastore_priceperpersonmodel_4.lower_bag_price = '233.05'
    datastore_priceperpersonmodel_4.lower_bag_weight = '233.05'
    datastore_priceperpersonmodel_4.lowest_price = '233.05'
    datastore_priceperpersonmodel_4 = importer.save_or_locate(datastore_priceperpersonmodel_4)

    # Re-processing model: datastore.models.PricePerPersonModel


    datastore_priceperpersonmodel_2.market.add(  importer.locate_object(MarketModel, "entitymodel_ptr", EntityModel, "id", 2, {'display_name': 'United Kingdom', 'entitymodel_ptr_id': 2, 'description': 'Market of United Kingdom.', 'code': 'en_UK', '_entitymodel_ptr_cache': 'United Kingdom', 'id': 2} )  )

    datastore_priceperpersonmodel_3.market.add(  importer.locate_object(MarketModel, "entitymodel_ptr", EntityModel, "id", 2, {'display_name': 'United Kingdom', 'entitymodel_ptr_id': 2, 'description': 'Market of United Kingdom.', 'code': 'en_UK', '_entitymodel_ptr_cache': 'United Kingdom', 'id': 2} )  )

    datastore_priceperpersonmodel_4.market.add(  importer.locate_object(MarketModel, "entitymodel_ptr", EntityModel, "id", 2, {'display_name': 'United Kingdom', 'entitymodel_ptr_id': 2, 'description': 'Market of United Kingdom.', 'code': 'en_UK', '_entitymodel_ptr_cache': 'United Kingdom', 'id': 2} )  )
    datastore_priceperpersonmodel_4.market.add(  importer.locate_object(MarketModel, "entitymodel_ptr", EntityModel, "id", 25, {'display_name': 'Germany', 'entitymodel_ptr_id': 25, 'description': None, 'code': 'ge_DE', '_entitymodel_ptr_cache': 'Germany', 'id': 25} )  )
    datastore_priceperpersonmodel_4.market.add(  importer.locate_object(MarketModel, "entitymodel_ptr", EntityModel, "id", 26, {'display_name': 'Ireland', 'entitymodel_ptr_id': 26, 'description': None, 'code': 'ir_IR', '_entitymodel_ptr_cache': 'Ireland', 'id': 26} )  )
    datastore_priceperpersonmodel_4.market.add(  importer.locate_object(MarketModel, "entitymodel_ptr", EntityModel, "id", 27, {'display_name': 'Spain', 'entitymodel_ptr_id': 27, 'description': None, 'code': 'es_ES', '_entitymodel_ptr_cache': 'Spain', 'id': 27} )  )
    datastore_priceperpersonmodel_4.market.add(  importer.locate_object(MarketModel, "entitymodel_ptr", EntityModel, "id", 28, {'display_name': 'Scotland, UK', 'entitymodel_ptr_id': 28, 'description': None, 'code': 'sc_UK', '_entitymodel_ptr_cache': 'Scotland, UK', 'id': 28} )  )
    datastore_priceperpersonmodel_4.market.add(  importer.locate_object(MarketModel, "entitymodel_ptr", EntityModel, "id", 29, {'display_name': 'Italy', 'entitymodel_ptr_id': 29, 'description': None, 'code': 'it_IT', '_entitymodel_ptr_cache': 'Italy', 'id': 29} )  )

