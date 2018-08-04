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
# ./manage.py dumpscript mdm
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

    # Processing model: mdm.models.EntityModel

    from mdm.models import EntityModel

    mdm_entitymodel_1 = EntityModel()
    mdm_entitymodel_1.display_name = 'United Kingdom'
    mdm_entitymodel_1.description = 'Market of United Kingdom.'
    mdm_entitymodel_1 = importer.save_or_locate(mdm_entitymodel_1)

    mdm_entitymodel_2 = EntityModel()
    mdm_entitymodel_2.display_name = 'Single'
    mdm_entitymodel_2.description = 'Room for single person.'
    mdm_entitymodel_2 = importer.save_or_locate(mdm_entitymodel_2)

    mdm_entitymodel_3 = EntityModel()
    mdm_entitymodel_3.display_name = 'Double'
    mdm_entitymodel_3.description = 'Room with two beds.'
    mdm_entitymodel_3 = importer.save_or_locate(mdm_entitymodel_3)

    mdm_entitymodel_4 = EntityModel()
    mdm_entitymodel_4.display_name = 'Half-board'
    mdm_entitymodel_4.description = 'Meal basis is half-board.'
    mdm_entitymodel_4 = importer.save_or_locate(mdm_entitymodel_4)

    mdm_entitymodel_5 = EntityModel()
    mdm_entitymodel_5.display_name = 'All-inlcusive'
    mdm_entitymodel_5.description = 'Meal basis is all paid.'
    mdm_entitymodel_5 = importer.save_or_locate(mdm_entitymodel_5)

    mdm_entitymodel_6 = EntityModel()
    mdm_entitymodel_6.display_name = 'Breakfast'
    mdm_entitymodel_6.description = 'Only breakfast.'
    mdm_entitymodel_6 = importer.save_or_locate(mdm_entitymodel_6)

    mdm_entitymodel_7 = EntityModel()
    mdm_entitymodel_7.display_name = 'Ryanair Holidays'
    mdm_entitymodel_7.description = 'Main portal of RyanAir Holidays.'
    mdm_entitymodel_7 = importer.save_or_locate(mdm_entitymodel_7)

    mdm_entitymodel_8 = EntityModel()
    mdm_entitymodel_8.display_name = 'Holiday Palace'
    mdm_entitymodel_8.description = 'Hotel Holiday Palace.'
    mdm_entitymodel_8 = importer.save_or_locate(mdm_entitymodel_8)

    mdm_entitymodel_9 = EntityModel()
    mdm_entitymodel_9.display_name = 'RyanAir'
    mdm_entitymodel_9.description = 'RyanAir flights.'
    mdm_entitymodel_9 = importer.save_or_locate(mdm_entitymodel_9)

    mdm_entitymodel_10 = EntityModel()
    mdm_entitymodel_10.display_name = 'Lower bag type'
    mdm_entitymodel_10.description = None
    mdm_entitymodel_10 = importer.save_or_locate(mdm_entitymodel_10)

    mdm_entitymodel_11 = EntityModel()
    mdm_entitymodel_11.display_name = 'Larger bag type'
    mdm_entitymodel_11.description = None
    mdm_entitymodel_11 = importer.save_or_locate(mdm_entitymodel_11)

    mdm_entitymodel_12 = EntityModel()
    mdm_entitymodel_12.display_name = 'Luton'
    mdm_entitymodel_12.description = 'United Kingdom, London, Luton'
    mdm_entitymodel_12 = importer.save_or_locate(mdm_entitymodel_12)

    mdm_entitymodel_13 = EntityModel()
    mdm_entitymodel_13.display_name = 'On the Beach'
    mdm_entitymodel_13.description = None
    mdm_entitymodel_13 = importer.save_or_locate(mdm_entitymodel_13)

    mdm_entitymodel_14 = EntityModel()
    mdm_entitymodel_14.display_name = 'Love Holidays'
    mdm_entitymodel_14.description = None
    mdm_entitymodel_14 = importer.save_or_locate(mdm_entitymodel_14)

    mdm_entitymodel_15 = EntityModel()
    mdm_entitymodel_15.display_name = 'Travel Republic'
    mdm_entitymodel_15.description = None
    mdm_entitymodel_15 = importer.save_or_locate(mdm_entitymodel_15)

    mdm_entitymodel_16 = EntityModel()
    mdm_entitymodel_16.display_name = 'Jet2holidays'
    mdm_entitymodel_16.description = None
    mdm_entitymodel_16 = importer.save_or_locate(mdm_entitymodel_16)

    mdm_entitymodel_17 = EntityModel()
    mdm_entitymodel_17.display_name = 'Thomas Cook'
    mdm_entitymodel_17.description = None
    mdm_entitymodel_17 = importer.save_or_locate(mdm_entitymodel_17)

    mdm_entitymodel_18 = EntityModel()
    mdm_entitymodel_18.display_name = 'Jet2'
    mdm_entitymodel_18.description = None
    mdm_entitymodel_18 = importer.save_or_locate(mdm_entitymodel_18)

    mdm_entitymodel_19 = EntityModel()
    mdm_entitymodel_19.display_name = 'Easyjet'
    mdm_entitymodel_19.description = None
    mdm_entitymodel_19 = importer.save_or_locate(mdm_entitymodel_19)

    mdm_entitymodel_20 = EntityModel()
    mdm_entitymodel_20.display_name = 'Monarch'
    mdm_entitymodel_20.description = None
    mdm_entitymodel_20 = importer.save_or_locate(mdm_entitymodel_20)

    mdm_entitymodel_21 = EntityModel()
    mdm_entitymodel_21.display_name = 'Norwegian'
    mdm_entitymodel_21.description = None
    mdm_entitymodel_21 = importer.save_or_locate(mdm_entitymodel_21)

    mdm_entitymodel_22 = EntityModel()
    mdm_entitymodel_22.display_name = 'Vueling'
    mdm_entitymodel_22.description = None
    mdm_entitymodel_22 = importer.save_or_locate(mdm_entitymodel_22)

    mdm_entitymodel_23 = EntityModel()
    mdm_entitymodel_23.display_name = 'Germany'
    mdm_entitymodel_23.description = None
    mdm_entitymodel_23 = importer.save_or_locate(mdm_entitymodel_23)

    mdm_entitymodel_24 = EntityModel()
    mdm_entitymodel_24.display_name = 'Ireland'
    mdm_entitymodel_24.description = None
    mdm_entitymodel_24 = importer.save_or_locate(mdm_entitymodel_24)

    mdm_entitymodel_25 = EntityModel()
    mdm_entitymodel_25.display_name = 'Spain'
    mdm_entitymodel_25.description = None
    mdm_entitymodel_25 = importer.save_or_locate(mdm_entitymodel_25)

    mdm_entitymodel_26 = EntityModel()
    mdm_entitymodel_26.display_name = 'Scotland, UK'
    mdm_entitymodel_26.description = None
    mdm_entitymodel_26 = importer.save_or_locate(mdm_entitymodel_26)

    mdm_entitymodel_27 = EntityModel()
    mdm_entitymodel_27.display_name = 'Italy'
    mdm_entitymodel_27.description = None
    mdm_entitymodel_27 = importer.save_or_locate(mdm_entitymodel_27)

    mdm_entitymodel_28 = EntityModel()
    mdm_entitymodel_28.display_name = 'Villa Florida'
    mdm_entitymodel_28.description = None
    mdm_entitymodel_28 = importer.save_or_locate(mdm_entitymodel_28)

    mdm_entitymodel_29 = EntityModel()
    mdm_entitymodel_29.display_name = 'Green Park Hotel Pamphili'
    mdm_entitymodel_29.description = None
    mdm_entitymodel_29 = importer.save_or_locate(mdm_entitymodel_29)

    mdm_entitymodel_30 = EntityModel()
    mdm_entitymodel_30.display_name = 'VIK San Antonio'
    mdm_entitymodel_30.description = None
    mdm_entitymodel_30 = importer.save_or_locate(mdm_entitymodel_30)

    mdm_entitymodel_31 = EntityModel()
    mdm_entitymodel_31.display_name = 'Solana Hotel'
    mdm_entitymodel_31.description = None
    mdm_entitymodel_31 = importer.save_or_locate(mdm_entitymodel_31)

    mdm_entitymodel_32 = EntityModel()
    mdm_entitymodel_32.display_name = 'Tossamar'
    mdm_entitymodel_32.description = None
    mdm_entitymodel_32 = importer.save_or_locate(mdm_entitymodel_32)

    mdm_entitymodel_33 = EntityModel()
    mdm_entitymodel_33.display_name = 'Holiday Palace'
    mdm_entitymodel_33.description = None
    mdm_entitymodel_33 = importer.save_or_locate(mdm_entitymodel_33)

    mdm_entitymodel_34 = EntityModel()
    mdm_entitymodel_34.display_name = 'Rey Carlos'
    mdm_entitymodel_34.description = None
    mdm_entitymodel_34 = importer.save_or_locate(mdm_entitymodel_34)

    # Processing model: mdm.models.MarketModel

    from mdm.models import MarketModel

    mdm_marketmodel_1 = MarketModel()
    mdm_marketmodel_1.display_name = 'United Kingdom'
    mdm_marketmodel_1.description = 'Market of United Kingdom.'
    mdm_marketmodel_1.entitymodel_ptr = mdm_entitymodel_1
    mdm_marketmodel_1.code = 'en_UK'
    mdm_marketmodel_1 = importer.save_or_locate(mdm_marketmodel_1)

    mdm_marketmodel_2 = MarketModel()
    mdm_marketmodel_2.display_name = 'Germany'
    mdm_marketmodel_2.description = None
    mdm_marketmodel_2.entitymodel_ptr = mdm_entitymodel_23
    mdm_marketmodel_2.code = 'ge_DE'
    mdm_marketmodel_2 = importer.save_or_locate(mdm_marketmodel_2)

    mdm_marketmodel_3 = MarketModel()
    mdm_marketmodel_3.display_name = 'Ireland'
    mdm_marketmodel_3.description = None
    mdm_marketmodel_3.entitymodel_ptr = mdm_entitymodel_24
    mdm_marketmodel_3.code = 'ir_IR'
    mdm_marketmodel_3 = importer.save_or_locate(mdm_marketmodel_3)

    mdm_marketmodel_4 = MarketModel()
    mdm_marketmodel_4.display_name = 'Spain'
    mdm_marketmodel_4.description = None
    mdm_marketmodel_4.entitymodel_ptr = mdm_entitymodel_25
    mdm_marketmodel_4.code = 'es_ES'
    mdm_marketmodel_4 = importer.save_or_locate(mdm_marketmodel_4)

    mdm_marketmodel_5 = MarketModel()
    mdm_marketmodel_5.display_name = 'Scotland, UK'
    mdm_marketmodel_5.description = None
    mdm_marketmodel_5.entitymodel_ptr = mdm_entitymodel_26
    mdm_marketmodel_5.code = 'sc_UK'
    mdm_marketmodel_5 = importer.save_or_locate(mdm_marketmodel_5)

    mdm_marketmodel_6 = MarketModel()
    mdm_marketmodel_6.display_name = 'Italy'
    mdm_marketmodel_6.description = None
    mdm_marketmodel_6.entitymodel_ptr = mdm_entitymodel_27
    mdm_marketmodel_6.code = 'it_IT'
    mdm_marketmodel_6 = importer.save_or_locate(mdm_marketmodel_6)

    # Processing model: mdm.models.SupplierModel

    from mdm.models import SupplierModel

    mdm_suppliermodel_1 = SupplierModel()
    mdm_suppliermodel_1.display_name = 'Ryanair Holidays'
    mdm_suppliermodel_1.description = 'Main portal of RyanAir Holidays.'
    mdm_suppliermodel_1.entitymodel_ptr = mdm_entitymodel_7
    mdm_suppliermodel_1.portal = 'http://holidays.ryanair.com/?market=uk&lang=en&currency=GBP'
    mdm_suppliermodel_1 = importer.save_or_locate(mdm_suppliermodel_1)

    mdm_suppliermodel_2 = SupplierModel()
    mdm_suppliermodel_2.display_name = 'On the Beach'
    mdm_suppliermodel_2.description = None
    mdm_suppliermodel_2.entitymodel_ptr = mdm_entitymodel_13
    mdm_suppliermodel_2.portal = 'http://www.google.com'
    mdm_suppliermodel_2 = importer.save_or_locate(mdm_suppliermodel_2)

    mdm_suppliermodel_3 = SupplierModel()
    mdm_suppliermodel_3.display_name = 'Love Holidays'
    mdm_suppliermodel_3.description = None
    mdm_suppliermodel_3.entitymodel_ptr = mdm_entitymodel_14
    mdm_suppliermodel_3.portal = 'http://www.google.com'
    mdm_suppliermodel_3 = importer.save_or_locate(mdm_suppliermodel_3)

    mdm_suppliermodel_4 = SupplierModel()
    mdm_suppliermodel_4.display_name = 'Travel Republic'
    mdm_suppliermodel_4.description = None
    mdm_suppliermodel_4.entitymodel_ptr = mdm_entitymodel_15
    mdm_suppliermodel_4.portal = 'http://www.google.com'
    mdm_suppliermodel_4 = importer.save_or_locate(mdm_suppliermodel_4)

    mdm_suppliermodel_5 = SupplierModel()
    mdm_suppliermodel_5.display_name = 'Jet2holidays'
    mdm_suppliermodel_5.description = None
    mdm_suppliermodel_5.entitymodel_ptr = mdm_entitymodel_16
    mdm_suppliermodel_5.portal = 'http://www.google.com'
    mdm_suppliermodel_5 = importer.save_or_locate(mdm_suppliermodel_5)

    # Processing model: mdm.models.AirportModel

    from mdm.models import AirportModel

    mdm_airportmodel_1 = AirportModel()
    mdm_airportmodel_1.display_name = 'Luton'
    mdm_airportmodel_1.description = 'United Kingdom, London, Luton'
    mdm_airportmodel_1.entitymodel_ptr = mdm_entitymodel_12
    mdm_airportmodel_1.code = 'LTN'
    mdm_airportmodel_1.market = mdm_marketmodel_1
    mdm_airportmodel_1 = importer.save_or_locate(mdm_airportmodel_1)

    # Processing model: mdm.models.FlightProviderModel

    from mdm.models import FlightProviderModel

    mdm_flightprovidermodel_1 = FlightProviderModel()
    mdm_flightprovidermodel_1.display_name = 'RyanAir'
    mdm_flightprovidermodel_1.description = 'RyanAir flights.'
    mdm_flightprovidermodel_1.entitymodel_ptr = mdm_entitymodel_9
    mdm_flightprovidermodel_1.code = 'FR'
    mdm_flightprovidermodel_1 = importer.save_or_locate(mdm_flightprovidermodel_1)

    mdm_flightprovidermodel_2 = FlightProviderModel()
    mdm_flightprovidermodel_2.display_name = 'Thomas Cook'
    mdm_flightprovidermodel_2.description = None
    mdm_flightprovidermodel_2.entitymodel_ptr = mdm_entitymodel_17
    mdm_flightprovidermodel_2.code = 'HQ'
    mdm_flightprovidermodel_2 = importer.save_or_locate(mdm_flightprovidermodel_2)

    mdm_flightprovidermodel_3 = FlightProviderModel()
    mdm_flightprovidermodel_3.display_name = 'Jet2'
    mdm_flightprovidermodel_3.description = None
    mdm_flightprovidermodel_3.entitymodel_ptr = mdm_entitymodel_18
    mdm_flightprovidermodel_3.code = 'LS'
    mdm_flightprovidermodel_3 = importer.save_or_locate(mdm_flightprovidermodel_3)

    mdm_flightprovidermodel_4 = FlightProviderModel()
    mdm_flightprovidermodel_4.display_name = 'Easyjet'
    mdm_flightprovidermodel_4.description = None
    mdm_flightprovidermodel_4.entitymodel_ptr = mdm_entitymodel_19
    mdm_flightprovidermodel_4.code = 'U2'
    mdm_flightprovidermodel_4 = importer.save_or_locate(mdm_flightprovidermodel_4)

    mdm_flightprovidermodel_5 = FlightProviderModel()
    mdm_flightprovidermodel_5.display_name = 'Monarch'
    mdm_flightprovidermodel_5.description = None
    mdm_flightprovidermodel_5.entitymodel_ptr = mdm_entitymodel_20
    mdm_flightprovidermodel_5.code = 'ZB'
    mdm_flightprovidermodel_5 = importer.save_or_locate(mdm_flightprovidermodel_5)

    mdm_flightprovidermodel_6 = FlightProviderModel()
    mdm_flightprovidermodel_6.display_name = 'Norwegian'
    mdm_flightprovidermodel_6.description = None
    mdm_flightprovidermodel_6.entitymodel_ptr = mdm_entitymodel_21
    mdm_flightprovidermodel_6.code = 'DI'
    mdm_flightprovidermodel_6 = importer.save_or_locate(mdm_flightprovidermodel_6)

    mdm_flightprovidermodel_7 = FlightProviderModel()
    mdm_flightprovidermodel_7.display_name = 'Vueling'
    mdm_flightprovidermodel_7.description = None
    mdm_flightprovidermodel_7.entitymodel_ptr = mdm_entitymodel_22
    mdm_flightprovidermodel_7.code = 'VY'
    mdm_flightprovidermodel_7 = importer.save_or_locate(mdm_flightprovidermodel_7)

    # Processing model: mdm.models.HotelModel

    from mdm.models import HotelModel

    mdm_hotelmodel_1 = HotelModel()
    mdm_hotelmodel_1.display_name = 'Holiday Palace'
    mdm_hotelmodel_1.description = 'Hotel Holiday Palace.'
    mdm_hotelmodel_1.entitymodel_ptr = mdm_entitymodel_8
    mdm_hotelmodel_1.stars = 3
    mdm_hotelmodel_1.market = mdm_marketmodel_1
    mdm_hotelmodel_1 = importer.save_or_locate(mdm_hotelmodel_1)

    mdm_hotelmodel_2 = HotelModel()
    mdm_hotelmodel_2.display_name = 'Villa Florida'
    mdm_hotelmodel_2.description = None
    mdm_hotelmodel_2.entitymodel_ptr = mdm_entitymodel_28
    mdm_hotelmodel_2.stars = 3
    mdm_hotelmodel_2.market = mdm_marketmodel_1
    mdm_hotelmodel_2 = importer.save_or_locate(mdm_hotelmodel_2)

    mdm_hotelmodel_3 = HotelModel()
    mdm_hotelmodel_3.display_name = 'Green Park Hotel Pamphili'
    mdm_hotelmodel_3.description = None
    mdm_hotelmodel_3.entitymodel_ptr = mdm_entitymodel_29
    mdm_hotelmodel_3.stars = 4
    mdm_hotelmodel_3.market = mdm_marketmodel_2
    mdm_hotelmodel_3 = importer.save_or_locate(mdm_hotelmodel_3)

    mdm_hotelmodel_4 = HotelModel()
    mdm_hotelmodel_4.display_name = 'VIK San Antonio'
    mdm_hotelmodel_4.description = None
    mdm_hotelmodel_4.entitymodel_ptr = mdm_entitymodel_30
    mdm_hotelmodel_4.stars = 4
    mdm_hotelmodel_4.market = mdm_marketmodel_1
    mdm_hotelmodel_4 = importer.save_or_locate(mdm_hotelmodel_4)

    mdm_hotelmodel_5 = HotelModel()
    mdm_hotelmodel_5.display_name = 'Solana Hotel'
    mdm_hotelmodel_5.description = None
    mdm_hotelmodel_5.entitymodel_ptr = mdm_entitymodel_31
    mdm_hotelmodel_5.stars = 3
    mdm_hotelmodel_5.market = mdm_marketmodel_4
    mdm_hotelmodel_5 = importer.save_or_locate(mdm_hotelmodel_5)

    mdm_hotelmodel_6 = HotelModel()
    mdm_hotelmodel_6.display_name = 'Tossamar'
    mdm_hotelmodel_6.description = None
    mdm_hotelmodel_6.entitymodel_ptr = mdm_entitymodel_32
    mdm_hotelmodel_6.stars = 4
    mdm_hotelmodel_6.market = mdm_marketmodel_6
    mdm_hotelmodel_6 = importer.save_or_locate(mdm_hotelmodel_6)

    mdm_hotelmodel_7 = HotelModel()
    mdm_hotelmodel_7.display_name = 'Holiday Palace'
    mdm_hotelmodel_7.description = None
    mdm_hotelmodel_7.entitymodel_ptr = mdm_entitymodel_33
    mdm_hotelmodel_7.stars = 4
    mdm_hotelmodel_7.market = mdm_marketmodel_1
    mdm_hotelmodel_7 = importer.save_or_locate(mdm_hotelmodel_7)

    mdm_hotelmodel_8 = HotelModel()
    mdm_hotelmodel_8.display_name = 'Rey Carlos'
    mdm_hotelmodel_8.description = None
    mdm_hotelmodel_8.entitymodel_ptr = mdm_entitymodel_34
    mdm_hotelmodel_8.stars = 2
    mdm_hotelmodel_8.market = mdm_marketmodel_3
    mdm_hotelmodel_8 = importer.save_or_locate(mdm_hotelmodel_8)

    # Processing model: mdm.models.BoardModel

    from mdm.models import BoardModel

    mdm_boardmodel_1 = BoardModel()
    mdm_boardmodel_1.display_name = 'Half-board'
    mdm_boardmodel_1.description = 'Meal basis is half-board.'
    mdm_boardmodel_1.entitymodel_ptr = mdm_entitymodel_4
    mdm_boardmodel_1.code = 'HB'
    mdm_boardmodel_1 = importer.save_or_locate(mdm_boardmodel_1)

    mdm_boardmodel_2 = BoardModel()
    mdm_boardmodel_2.display_name = 'All-inlcusive'
    mdm_boardmodel_2.description = 'Meal basis is all paid.'
    mdm_boardmodel_2.entitymodel_ptr = mdm_entitymodel_5
    mdm_boardmodel_2.code = 'AI'
    mdm_boardmodel_2 = importer.save_or_locate(mdm_boardmodel_2)

    mdm_boardmodel_3 = BoardModel()
    mdm_boardmodel_3.display_name = 'Breakfast'
    mdm_boardmodel_3.description = 'Only breakfast.'
    mdm_boardmodel_3.entitymodel_ptr = mdm_entitymodel_6
    mdm_boardmodel_3.code = 'BR'
    mdm_boardmodel_3 = importer.save_or_locate(mdm_boardmodel_3)

    # Processing model: mdm.models.RoomTypeModel

    from mdm.models import RoomTypeModel

    mdm_roomtypemodel_1 = RoomTypeModel()
    mdm_roomtypemodel_1.display_name = 'Single'
    mdm_roomtypemodel_1.description = 'Room for single person.'
    mdm_roomtypemodel_1.entitymodel_ptr = mdm_entitymodel_2
    mdm_roomtypemodel_1.code = 'SINGLE'
    mdm_roomtypemodel_1 = importer.save_or_locate(mdm_roomtypemodel_1)

    mdm_roomtypemodel_2 = RoomTypeModel()
    mdm_roomtypemodel_2.display_name = 'Double'
    mdm_roomtypemodel_2.description = 'Room with two beds.'
    mdm_roomtypemodel_2.entitymodel_ptr = mdm_entitymodel_3
    mdm_roomtypemodel_2.code = 'DOUBLE'
    mdm_roomtypemodel_2 = importer.save_or_locate(mdm_roomtypemodel_2)

    # Processing model: mdm.models.BagTypeModel

    from mdm.models import BagTypeModel

    mdm_bagtypemodel_1 = BagTypeModel()
    mdm_bagtypemodel_1.display_name = 'Lower bag type'
    mdm_bagtypemodel_1.description = None
    mdm_bagtypemodel_1.entitymodel_ptr = mdm_entitymodel_10
    mdm_bagtypemodel_1.weight = 15
    mdm_bagtypemodel_1 = importer.save_or_locate(mdm_bagtypemodel_1)

    mdm_bagtypemodel_2 = BagTypeModel()
    mdm_bagtypemodel_2.display_name = 'Larger bag type'
    mdm_bagtypemodel_2.description = None
    mdm_bagtypemodel_2.entitymodel_ptr = mdm_entitymodel_11
    mdm_bagtypemodel_2.weight = 20
    mdm_bagtypemodel_2 = importer.save_or_locate(mdm_bagtypemodel_2)

