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
# ../manage.py dumpscript mdm
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

    # Processing model: mdm.models.AirportModel

    from mdm.models import AirportModel

    mdm_airports_1 = AirportModel()
    mdm_airports_1.code = 'GTW'
    mdm_airports_1.display_name = 'London-Gatwick'
    mdm_airports_1.description = 'London-Gatwick, United Kingdom'
    mdm_airports_1 = importer.save_or_locate(mdm_airports_1)

    mdm_airports_2 = AirportModel()
    mdm_airports_2.code = 'NCL'
    mdm_airports_2.display_name = 'Newcastle'
    mdm_airports_2.description = 'Newcastle'
    mdm_airports_2 = importer.save_or_locate(mdm_airports_2)

    mdm_airports_3 = AirportModel()
    mdm_airports_3.code = 'STN'
    mdm_airports_3.display_name = 'London-Stanstad'
    mdm_airports_3.description = 'London-Stanstad'
    mdm_airports_3 = importer.save_or_locate(mdm_airports_3)

    mdm_airports_4 = AirportModel()
    mdm_airports_4.code = 'LTN'
    mdm_airports_4.display_name = 'London-Luton'
    mdm_airports_4.description = 'London-Luton'
    mdm_airports_4 = importer.save_or_locate(mdm_airports_4)

    mdm_airports_5 = AirportModel()
    mdm_airports_5.code = 'GLA'
    mdm_airports_5.display_name = 'Glasgow'
    mdm_airports_5.description = 'Glasgow'
    mdm_airports_5 = importer.save_or_locate(mdm_airports_5)

    mdm_airports_6 = AirportModel()
    mdm_airports_6.code = 'MAN'
    mdm_airports_6.display_name = 'Manchester'
    mdm_airports_6.description = 'Manchester'
    mdm_airports_6 = importer.save_or_locate(mdm_airports_6)

    mdm_airports_7 = AirportModel()
    mdm_airports_7.code = 'BHX'
    mdm_airports_7.display_name = 'Birmingham'
    mdm_airports_7.description = 'Birmingham'
    mdm_airports_7 = importer.save_or_locate(mdm_airports_7)

    mdm_airports_8 = AirportModel()
    mdm_airports_8.code = 'DUB'
    mdm_airports_8.display_name = 'Dublin'
    mdm_airports_8.description = 'Dublin'
    mdm_airports_8 = importer.save_or_locate(mdm_airports_8)

    mdm_airports_9 = AirportModel()
    mdm_airports_9.code = 'MAD'
    mdm_airports_9.display_name = 'Madrid'
    mdm_airports_9.description = 'Madrid'
    mdm_airports_9 = importer.save_or_locate(mdm_airports_9)

    mdm_airports_10 = AirportModel()
    mdm_airports_10.code = 'BCN'
    mdm_airports_10.display_name = 'Barcelona'
    mdm_airports_10.description = 'Barcelona'
    mdm_airports_10 = importer.save_or_locate(mdm_airports_10)

    mdm_airports_11 = AirportModel()
    mdm_airports_11.code = 'PMI'
    mdm_airports_11.display_name = 'Palma de Majorca'
    mdm_airports_11.description = 'Palma de Majorca'
    mdm_airports_11 = importer.save_or_locate(mdm_airports_11)

    mdm_airports_12 = AirportModel()
    mdm_airports_12.code = 'VLC'
    mdm_airports_12.display_name = 'Valencia'
    mdm_airports_12.description = 'Valencia'
    mdm_airports_12 = importer.save_or_locate(mdm_airports_12)

    mdm_airports_13 = AirportModel()
    mdm_airports_13.code = 'AGP'
    mdm_airports_13.display_name = 'Malaga'
    mdm_airports_13.description = 'Malaga'
    mdm_airports_13 = importer.save_or_locate(mdm_airports_13)

    mdm_airports_14 = AirportModel()
    mdm_airports_14.code = 'SXF'
    mdm_airports_14.display_name = 'Berlin-Schönefeld'
    mdm_airports_14.description = 'Berlin-Schönefeld'
    mdm_airports_14 = importer.save_or_locate(mdm_airports_14)

    mdm_airports_15 = AirportModel()
    mdm_airports_15.code = 'HHN'
    mdm_airports_15.display_name = 'Frankfurt-Hahn'
    mdm_airports_15.description = 'Frankfurt-Hahn'
    mdm_airports_15 = importer.save_or_locate(mdm_airports_15)

    mdm_airports_16 = AirportModel()
    mdm_airports_16.code = 'FRA'
    mdm_airports_16.display_name = 'Frankfurt-International'
    mdm_airports_16.description = 'Frankfurt-International'
    mdm_airports_16 = importer.save_or_locate(mdm_airports_16)

    mdm_airports_17 = AirportModel()
    mdm_airports_17.code = 'TXL'
    mdm_airports_17.display_name = 'Berlin-Tegel'
    mdm_airports_17.description = 'Berlin-Tegel'
    mdm_airports_17 = importer.save_or_locate(mdm_airports_17)

    mdm_airports_18 = AirportModel()
    mdm_airports_18.code = 'CGN'
    mdm_airports_18.display_name = 'Köln-Cologne'
    mdm_airports_18.description = 'Köln-Cologne'
    mdm_airports_18 = importer.save_or_locate(mdm_airports_18)

    mdm_airports_19 = AirportModel()
    mdm_airports_19.code = 'TSF'
    mdm_airports_19.display_name = 'Venezia Treviso'
    mdm_airports_19.description = 'Venezia Treviso TSF'
    mdm_airports_19 = importer.save_or_locate(mdm_airports_19)

    mdm_airports_20 = AirportModel()
    mdm_airports_20.code = 'VCE'
    mdm_airports_20.display_name = 'Venezia Santa Lucia'
    mdm_airports_20.description = 'Venezia Santa Lucia VCE'
    mdm_airports_20 = importer.save_or_locate(mdm_airports_20)

    mdm_airports_21 = AirportModel()
    mdm_airports_21.code = 'BGY'
    mdm_airports_21.display_name = 'Bergamo'
    mdm_airports_21.description = 'Bergamo'
    mdm_airports_21 = importer.save_or_locate(mdm_airports_21)

    mdm_airports_22 = AirportModel()
    mdm_airports_22.code = 'MXP'
    mdm_airports_22.display_name = 'Milano'
    mdm_airports_22.description = 'Milano'
    mdm_airports_22 = importer.save_or_locate(mdm_airports_22)

    mdm_airports_23 = AirportModel()
    mdm_airports_23.code = 'TPS'
    mdm_airports_23.display_name = 'Trapani'
    mdm_airports_23.description = 'Trapani'
    mdm_airports_23 = importer.save_or_locate(mdm_airports_23)

    mdm_airports_24 = AirportModel()
    mdm_airports_24.code = 'BLQ'
    mdm_airports_24.display_name = 'Bologna'
    mdm_airports_24.description = 'Bologna'
    mdm_airports_24 = importer.save_or_locate(mdm_airports_24)

    mdm_airports_25 = AirportModel()
    mdm_airports_25.code = 'CAG'
    mdm_airports_25.display_name = 'Cagliari'
    mdm_airports_25.description = 'Cagliari'
    mdm_airports_25 = importer.save_or_locate(mdm_airports_25)

    mdm_airports_26 = AirportModel()
    mdm_airports_26.code = 'AHO'
    mdm_airports_26.display_name = 'Alghero'
    mdm_airports_26.description = 'Alghero'
    mdm_airports_26 = importer.save_or_locate(mdm_airports_26)

    mdm_airports_27 = AirportModel()
    mdm_airports_27.code = 'OLB'
    mdm_airports_27.display_name = 'Olbia'
    mdm_airports_27.description = 'Olbia'
    mdm_airports_27 = importer.save_or_locate(mdm_airports_27)

    mdm_airports_28 = AirportModel()
    mdm_airports_28.code = 'BRI'
    mdm_airports_28.display_name = 'Bari'
    mdm_airports_28.description = 'Bari'
    mdm_airports_28 = importer.save_or_locate(mdm_airports_28)

    mdm_airports_29 = AirportModel()
    mdm_airports_29.code = 'PSA'
    mdm_airports_29.display_name = 'Pisa'
    mdm_airports_29.description = 'Pisa'
    mdm_airports_29 = importer.save_or_locate(mdm_airports_29)

    # Processing model: mdm.models.BagTypeModel

    from mdm.models import BagTypeModel

    mdm_bagtype_1 = BagTypeModel()
    mdm_bagtype_1.code = 'W15'
    mdm_bagtype_1.weight = 15
    mdm_bagtype_1.display_name = 'Small size'
    mdm_bagtype_1.description = 'Small size luggage up to 15 kg'
    mdm_bagtype_1 = importer.save_or_locate(mdm_bagtype_1)

    mdm_bagtype_2 = BagTypeModel()
    mdm_bagtype_2.code = 'W20'
    mdm_bagtype_2.weight = 20
    mdm_bagtype_2.display_name = 'Large size'
    mdm_bagtype_2.description = 'Large size luggage above 20 kg'
    mdm_bagtype_2 = importer.save_or_locate(mdm_bagtype_2)

    # Processing model: mdm.models.BoardModel

    from mdm.models import BoardModel

    mdm_boards_1 = BoardModel()
    mdm_boards_1.code = 'RO'
    mdm_boards_1.display_name = 'Room only'
    mdm_boards_1.description = 'Room only or without breakfast'
    mdm_boards_1 = importer.save_or_locate(mdm_boards_1)

    mdm_boards_2 = BoardModel()
    mdm_boards_2.code = 'BB'
    mdm_boards_2.display_name = 'Bed and breakfast'
    mdm_boards_2.description = 'Bed and breakfast or With breakfast or Breakfast included'
    mdm_boards_2 = importer.save_or_locate(mdm_boards_2)

    mdm_boards_3 = BoardModel()
    mdm_boards_3.code = 'HB'
    mdm_boards_3.display_name = 'Half board'
    mdm_boards_3.description = 'Half board'
    mdm_boards_3 = importer.save_or_locate(mdm_boards_3)

    mdm_boards_4 = BoardModel()
    mdm_boards_4.code = 'FB'
    mdm_boards_4.display_name = 'Full board'
    mdm_boards_4.description = 'Full board'
    mdm_boards_4 = importer.save_or_locate(mdm_boards_4)

    mdm_boards_5 = BoardModel()
    mdm_boards_5.code = 'AI'
    mdm_boards_5.display_name = 'All inclusive'
    mdm_boards_5.description = 'All inclusive'
    mdm_boards_5 = importer.save_or_locate(mdm_boards_5)

    mdm_boards_6 = BoardModel()
    mdm_boards_6.code = 'SC'
    mdm_boards_6.display_name = 'Self catering'
    mdm_boards_6.description = 'Self catering'
    mdm_boards_6 = importer.save_or_locate(mdm_boards_6)

    # Processing model: mdm.models.FlightProviderModel

    from mdm.models import FlightProviderModel

    mdm_flightprovider_1 = FlightProviderModel()
    mdm_flightprovider_1.code = 'X3'
    mdm_flightprovider_1.display_name = 'TUI'
    mdm_flightprovider_1.description = 'TUI'
    mdm_flightprovider_1 = importer.save_or_locate(mdm_flightprovider_1)

    mdm_flightprovider_2 = FlightProviderModel()
    mdm_flightprovider_2.code = 'FR'
    mdm_flightprovider_2.display_name = 'Ryanair'
    mdm_flightprovider_2.description = 'Ryanair'
    mdm_flightprovider_2 = importer.save_or_locate(mdm_flightprovider_2)

    mdm_flightprovider_3 = FlightProviderModel()
    mdm_flightprovider_3.code = 'HQ'
    mdm_flightprovider_3.display_name = 'Thomas Cook'
    mdm_flightprovider_3.description = 'Thomas Cook'
    mdm_flightprovider_3 = importer.save_or_locate(mdm_flightprovider_3)

    mdm_flightprovider_4 = FlightProviderModel()
    mdm_flightprovider_4.code = 'LS'
    mdm_flightprovider_4.display_name = 'Jet2'
    mdm_flightprovider_4.description = 'Jet2'
    mdm_flightprovider_4 = importer.save_or_locate(mdm_flightprovider_4)

    mdm_flightprovider_5 = FlightProviderModel()
    mdm_flightprovider_5.code = 'U2'
    mdm_flightprovider_5.display_name = 'Easyjet'
    mdm_flightprovider_5.description = 'Easyjet'
    mdm_flightprovider_5 = importer.save_or_locate(mdm_flightprovider_5)

    mdm_flightprovider_6 = FlightProviderModel()
    mdm_flightprovider_6.code = 'ZB'
    mdm_flightprovider_6.display_name = 'Monarch'
    mdm_flightprovider_6.description = 'Monarch'
    mdm_flightprovider_6 = importer.save_or_locate(mdm_flightprovider_6)

    mdm_flightprovider_7 = FlightProviderModel()
    mdm_flightprovider_7.code = 'DI'
    mdm_flightprovider_7.display_name = 'Norwegian'
    mdm_flightprovider_7.description = 'Norwegian'
    mdm_flightprovider_7 = importer.save_or_locate(mdm_flightprovider_7)

    mdm_flightprovider_8 = FlightProviderModel()
    mdm_flightprovider_8.code = 'VY'
    mdm_flightprovider_8.display_name = 'Vueling'
    mdm_flightprovider_8.description = 'Vueling'
    mdm_flightprovider_8 = importer.save_or_locate(mdm_flightprovider_8)

    mdm_flightprovider_9 = FlightProviderModel()
    mdm_flightprovider_9.code = 'EI'
    mdm_flightprovider_9.display_name = 'Air Lingus'
    mdm_flightprovider_9.description = 'Air Lingus'
    mdm_flightprovider_9 = importer.save_or_locate(mdm_flightprovider_9)

    mdm_flightprovider_10 = FlightProviderModel()
    mdm_flightprovider_10.code = 'IB'
    mdm_flightprovider_10.display_name = 'Iberia'
    mdm_flightprovider_10.description = 'Iberia'
    mdm_flightprovider_10 = importer.save_or_locate(mdm_flightprovider_10)

    mdm_flightprovider_11 = FlightProviderModel()
    mdm_flightprovider_11.code = 'UX'
    mdm_flightprovider_11.display_name = 'Air Europa'
    mdm_flightprovider_11.description = 'Air Europa'
    mdm_flightprovider_11 = importer.save_or_locate(mdm_flightprovider_11)

    mdm_flightprovider_12 = FlightProviderModel()
    mdm_flightprovider_12.code = 'HV'
    mdm_flightprovider_12.display_name = 'Transavia'
    mdm_flightprovider_12.description = 'Transavia'
    mdm_flightprovider_12 = importer.save_or_locate(mdm_flightprovider_12)

    mdm_flightprovider_13 = FlightProviderModel()
    mdm_flightprovider_13.code = 'SK'
    mdm_flightprovider_13.display_name = 'Scandinavian Airlines System'
    mdm_flightprovider_13.description = 'Scandinavian Airlines System'
    mdm_flightprovider_13 = importer.save_or_locate(mdm_flightprovider_13)

    mdm_flightprovider_14 = FlightProviderModel()
    mdm_flightprovider_14.code = 'CI'
    mdm_flightprovider_14.display_name = 'Condor Airlines'
    mdm_flightprovider_14.description = 'Condor Airlines'
    mdm_flightprovider_14 = importer.save_or_locate(mdm_flightprovider_14)

    mdm_flightprovider_15 = FlightProviderModel()
    mdm_flightprovider_15.code = 'AZ'
    mdm_flightprovider_15.display_name = 'Alitalia'
    mdm_flightprovider_15.description = 'Alitalia'
    mdm_flightprovider_15 = importer.save_or_locate(mdm_flightprovider_15)

    mdm_flightprovider_16 = FlightProviderModel()
    mdm_flightprovider_16.code = 'BA'
    mdm_flightprovider_16.display_name = 'British Airways'
    mdm_flightprovider_16.description = 'British Airways'
    mdm_flightprovider_16 = importer.save_or_locate(mdm_flightprovider_16)

    mdm_flightprovider_17 = FlightProviderModel()
    mdm_flightprovider_17.code = '4U'
    mdm_flightprovider_17.display_name = 'Germanwings'
    mdm_flightprovider_17.description = 'Germanwings'
    mdm_flightprovider_17 = importer.save_or_locate(mdm_flightprovider_17)

    mdm_flightprovider_18 = FlightProviderModel()
    mdm_flightprovider_18.code = 'LH'
    mdm_flightprovider_18.display_name = 'Lufthansa'
    mdm_flightprovider_18.description = 'Lufthansa'
    mdm_flightprovider_18 = importer.save_or_locate(mdm_flightprovider_18)

    mdm_flightprovider_19 = FlightProviderModel()
    mdm_flightprovider_19.code = 'EW'
    mdm_flightprovider_19.display_name = 'Eurowings'
    mdm_flightprovider_19.description = 'Eurowings'
    mdm_flightprovider_19 = importer.save_or_locate(mdm_flightprovider_19)

    mdm_flightprovider_20 = FlightProviderModel()
    mdm_flightprovider_20.code = 'AB'
    mdm_flightprovider_20.display_name = 'Air Berlin'
    mdm_flightprovider_20.description = 'Air Berlin'
    mdm_flightprovider_20 = importer.save_or_locate(mdm_flightprovider_20)

    mdm_flightprovider_21 = FlightProviderModel()
    mdm_flightprovider_21.code = 'A3'
    mdm_flightprovider_21.display_name = 'Aegean Airlines'
    mdm_flightprovider_21.description = 'Aegean Airlines'
    mdm_flightprovider_21 = importer.save_or_locate(mdm_flightprovider_21)

    mdm_flightprovider_22 = FlightProviderModel()
    mdm_flightprovider_22.code = 'DE'
    mdm_flightprovider_22.display_name = 'Condor Flugdienst GmbH'
    mdm_flightprovider_22.description = 'Condor Flugdienst GmbH'
    mdm_flightprovider_22 = importer.save_or_locate(mdm_flightprovider_22)

    mdm_flightprovider_23 = FlightProviderModel()
    mdm_flightprovider_23.code = 'HG'
    mdm_flightprovider_23.display_name = 'Niki Luftfahrt'
    mdm_flightprovider_23.description = 'Niki Luftfahrt'
    mdm_flightprovider_23 = importer.save_or_locate(mdm_flightprovider_23)

    mdm_flightprovider_24 = FlightProviderModel()
    mdm_flightprovider_24.code = 'YW'
    mdm_flightprovider_24.display_name = 'Air Nosturm'
    mdm_flightprovider_24.description = 'Air Nosturm'
    mdm_flightprovider_24 = importer.save_or_locate(mdm_flightprovider_24)

    mdm_flightprovider_25 = FlightProviderModel()
    mdm_flightprovider_25.code = 'V7'
    mdm_flightprovider_25.display_name = 'Volotea'
    mdm_flightprovider_25.description = 'Volotea'
    mdm_flightprovider_25 = importer.save_or_locate(mdm_flightprovider_25)

    mdm_flightprovider_26 = FlightProviderModel()
    mdm_flightprovider_26.code = 'BV'
    mdm_flightprovider_26.display_name = 'Blue Panorama'
    mdm_flightprovider_26.description = 'Blue Panorama'
    mdm_flightprovider_26 = importer.save_or_locate(mdm_flightprovider_26)

    mdm_flightprovider_27 = FlightProviderModel()
    mdm_flightprovider_27.code = 'KM'
    mdm_flightprovider_27.display_name = 'Air Malta'
    mdm_flightprovider_27.description = 'Air Malta'
    mdm_flightprovider_27 = importer.save_or_locate(mdm_flightprovider_27)

    mdm_flightprovider_28 = FlightProviderModel()
    mdm_flightprovider_28.code = 'OK'
    mdm_flightprovider_28.display_name = 'CSA Czech Airlines'
    mdm_flightprovider_28.description = 'CSA Czech Airlines'
    mdm_flightprovider_28 = importer.save_or_locate(mdm_flightprovider_28)

    mdm_flightprovider_29 = FlightProviderModel()
    mdm_flightprovider_29.code = 'WZ'
    mdm_flightprovider_29.display_name = 'Wizz Air'
    mdm_flightprovider_29.description = 'Wizz Air'
    mdm_flightprovider_29 = importer.save_or_locate(mdm_flightprovider_29)

    mdm_flightprovider_30 = FlightProviderModel()
    mdm_flightprovider_30.code = 'NS'
    mdm_flightprovider_30.display_name = 'Neos Air'
    mdm_flightprovider_30.description = 'Neos Air'
    mdm_flightprovider_30 = importer.save_or_locate(mdm_flightprovider_30)

    # Processing model: mdm.models.HotelModel

    from mdm.models import HotelModel


    # Processing model: mdm.models.MarketModel

    from mdm.models import MarketModel

    mdm_markets_1 = MarketModel()
    mdm_markets_1.code = 'UK'
    mdm_markets_1.display_name = 'United Kingdom'
    mdm_markets_1.description = 'United Kingdom'
    mdm_markets_1 = importer.save_or_locate(mdm_markets_1)

    mdm_markets_2 = MarketModel()
    mdm_markets_2.code = 'ES'
    mdm_markets_2.display_name = 'Spain'
    mdm_markets_2.description = 'Spain'
    mdm_markets_2 = importer.save_or_locate(mdm_markets_2)

    mdm_markets_3 = MarketModel()
    mdm_markets_3.code = 'DE'
    mdm_markets_3.display_name = 'Germany'
    mdm_markets_3.description = 'Germany'
    mdm_markets_3 = importer.save_or_locate(mdm_markets_3)

    mdm_markets_4 = MarketModel()
    mdm_markets_4.code = 'IT'
    mdm_markets_4.display_name = 'Italy'
    mdm_markets_4.description = 'Italy'
    mdm_markets_4 = importer.save_or_locate(mdm_markets_4)

    mdm_markets_5 = MarketModel()
    mdm_markets_5.code = 'IE'
    mdm_markets_5.display_name = 'Ireland'
    mdm_markets_5.description = 'Ireland'
    mdm_markets_5 = importer.save_or_locate(mdm_markets_5)

    # Processing model: mdm.models.RoomTypeModel

    from mdm.models import RoomTypeModel


    # Processing model: mdm.models.SupplierModel

    from mdm.models import SupplierModel

    mdm_suppliers_1 = SupplierModel()
    mdm_suppliers_1.code = ''
    mdm_suppliers_1.display_name = 'Ryanair Holidays UK'
    mdm_suppliers_1.description = 'Ryanair Holidays UK'
    mdm_suppliers_1.portal = 'http://holidays.ryanair.com/?market=uk&lang=en&currency=GBP'
    mdm_suppliers_1 = importer.save_or_locate(mdm_suppliers_1)

