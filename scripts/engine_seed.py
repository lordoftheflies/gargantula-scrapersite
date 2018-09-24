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
# ../manage.py dumpscript engine
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

    # Processing model: engine.models.ProcessModel

    from engine.models import ProcessModel

    engine_processmodel_1 = ProcessModel()
    engine_processmodel_1.slug = ''
    engine_processmodel_1.friendly_name = 'Sample'
    engine_processmodel_1.description = 'Sample process for scraping data to provide samples of usage.\r\n\r\nFurther information: https://github.com/lordoftheflies/gargantula/wiki/Sample-project'
    engine_processmodel_1.active = True
    engine_processmodel_1.notebook = 'demo_notebook.ipynb'
    engine_processmodel_1 = importer.save_or_locate(engine_processmodel_1)

    engine_processmodel_2 = ProcessModel()
    engine_processmodel_2.slug = ''
    engine_processmodel_2.friendly_name = 'RyanAir best-offer'
    engine_processmodel_2.description = 'Best-offers from RyanAir webportal.'
    engine_processmodel_2.active = True
    engine_processmodel_2.notebook = 'demo_notebook.ipynb'
    engine_processmodel_2 = importer.save_or_locate(engine_processmodel_2)

    engine_processmodel_3 = ProcessModel()
    engine_processmodel_3.slug = ''
    engine_processmodel_3.friendly_name = 'On the Beach best-offer'
    engine_processmodel_3.description = 'Best-offers from On the Beach webportal.'
    engine_processmodel_3.active = True
    engine_processmodel_3.notebook = 'demo_notebook.ipynb'
    engine_processmodel_3 = importer.save_or_locate(engine_processmodel_3)

    engine_processmodel_4 = ProcessModel()
    engine_processmodel_4.slug = ''
    engine_processmodel_4.friendly_name = 'Expedia best-offer'
    engine_processmodel_4.description = 'Best-offers from Expedia webportal.'
    engine_processmodel_4.active = True
    engine_processmodel_4.notebook = 'demo_notebook.ipynb'
    engine_processmodel_4 = importer.save_or_locate(engine_processmodel_4)

    engine_processmodel_5 = ProcessModel()
    engine_processmodel_5.slug = ''
    engine_processmodel_5.friendly_name = 'Love Holidays best-offer'
    engine_processmodel_5.description = 'Best-offers from Love Holidays webportal.'
    engine_processmodel_5.active = True
    engine_processmodel_5.notebook = 'demo_notebook.ipynb'
    engine_processmodel_5 = importer.save_or_locate(engine_processmodel_5)

    engine_processmodel_6 = ProcessModel()
    engine_processmodel_6.slug = ''
    engine_processmodel_6.friendly_name = 'Travel Republic best-offer'
    engine_processmodel_6.description = 'Best-offers from Travel Republic webportal.'
    engine_processmodel_6.active = True
    engine_processmodel_6.notebook = 'demo_notebook.ipynb'
    engine_processmodel_6 = importer.save_or_locate(engine_processmodel_6)

    engine_processmodel_7 = ProcessModel()
    engine_processmodel_7.slug = ''
    engine_processmodel_7.friendly_name = 'EasyJet best-offer'
    engine_processmodel_7.description = 'Best-offers from EasyJet webportal.'
    engine_processmodel_7.active = True
    engine_processmodel_7.notebook = 'demo_notebook.ipynb'
    engine_processmodel_7 = importer.save_or_locate(engine_processmodel_7)

    engine_processmodel_8 = ProcessModel()
    engine_processmodel_8.slug = ''
    engine_processmodel_8.friendly_name = 'Jet2holidays best-offer'
    engine_processmodel_8.description = 'Best-offers from Jet2holidays webportal.'
    engine_processmodel_8.active = True
    engine_processmodel_8.notebook = 'demo_notebook.ipynb'
    engine_processmodel_8 = importer.save_or_locate(engine_processmodel_8)

    engine_processmodel_9 = ProcessModel()
    engine_processmodel_9.slug = 'csacska'
    engine_processmodel_9.friendly_name = 'Sample'
    engine_processmodel_9.description = 'Sample project for demonstrate capabilities of the software.'
    engine_processmodel_9.active = True
    engine_processmodel_9.notebook = 'demo_notebook.ipynb'
    engine_processmodel_9 = importer.save_or_locate(engine_processmodel_9)

    engine_processmodel_10 = ProcessModel()
    engine_processmodel_10.slug = ''
    engine_processmodel_10.friendly_name = 'Love Holidays best-offer comparison'
    engine_processmodel_10.description = 'Best-offers from Love Holidays webportal.'
    engine_processmodel_10.active = True
    engine_processmodel_10.notebook = 'demo_notebook.ipynb'
    engine_processmodel_10 = importer.save_or_locate(engine_processmodel_10)

    # Processing model: engine.models.ArgumentModel

    from engine.models import ArgumentModel

    engine_argumentmodel_1 = ArgumentModel()
    engine_argumentmodel_1.slug = 'price'
    engine_argumentmodel_1.friendly_name = 'Price'
    engine_argumentmodel_1.description = 'Number argument.'
    engine_argumentmodel_1.data_type = 'number'
    engine_argumentmodel_1.default_value = '100'
    engine_argumentmodel_1.process = engine_processmodel_9
    engine_argumentmodel_1 = importer.save_or_locate(engine_argumentmodel_1)

    engine_argumentmodel_2 = ArgumentModel()
    engine_argumentmodel_2.slug = 'created'
    engine_argumentmodel_2.friendly_name = 'Timestamp'
    engine_argumentmodel_2.description = 'Datetime argument.'
    engine_argumentmodel_2.data_type = 'date'
    engine_argumentmodel_2.default_value = '2018-08-06T10:00:00.0Z'
    engine_argumentmodel_2.process = engine_processmodel_9
    engine_argumentmodel_2 = importer.save_or_locate(engine_argumentmodel_2)

    engine_argumentmodel_3 = ArgumentModel()
    engine_argumentmodel_3.slug = 'from_location'
    engine_argumentmodel_3.friendly_name = 'From'
    engine_argumentmodel_3.description = 'Location enumeration argument.'
    engine_argumentmodel_3.data_type = 'text'
    engine_argumentmodel_3.default_value = 'Budapest'
    engine_argumentmodel_3.process = engine_processmodel_9
    engine_argumentmodel_3 = importer.save_or_locate(engine_argumentmodel_3)

    engine_argumentmodel_4 = ArgumentModel()
    engine_argumentmodel_4.slug = 'to_location'
    engine_argumentmodel_4.friendly_name = 'To'
    engine_argumentmodel_4.description = 'Location enumeration argument.'
    engine_argumentmodel_4.data_type = 'text'
    engine_argumentmodel_4.default_value = 'London'
    engine_argumentmodel_4.process = engine_processmodel_9
    engine_argumentmodel_4 = importer.save_or_locate(engine_argumentmodel_4)

    engine_argumentmodel_5 = ArgumentModel()
    engine_argumentmodel_5.slug = 'start'
    engine_argumentmodel_5.friendly_name = 'Start'
    engine_argumentmodel_5.description = 'Datetime argument.'
    engine_argumentmodel_5.data_type = 'date'
    engine_argumentmodel_5.default_value = '2018-08-06T12:00:00.0Z'
    engine_argumentmodel_5.process = engine_processmodel_9
    engine_argumentmodel_5 = importer.save_or_locate(engine_argumentmodel_5)

    engine_argumentmodel_6 = ArgumentModel()
    engine_argumentmodel_6.slug = 'arrival_date'
    engine_argumentmodel_6.friendly_name = 'Arrival Date'
    engine_argumentmodel_6.description = 'Arrival date when we want to search'
    engine_argumentmodel_6.data_type = 'date'
    engine_argumentmodel_6.default_value = None
    engine_argumentmodel_6.process = engine_processmodel_10
    engine_argumentmodel_6 = importer.save_or_locate(engine_argumentmodel_6)

    # Processing model: engine.models.ExecutionModel

    from engine.models import ExecutionModel

    engine_executionmodel_1 = ExecutionModel()
    engine_executionmodel_1.started = dateutil.parser.parse("2018-08-13T10:10:00+00:00")
    engine_executionmodel_1.ended = dateutil.parser.parse("2018-08-17T10:10:00+00:00")
    engine_executionmodel_1.process = engine_processmodel_9
    engine_executionmodel_1.configuration = '{}'
    engine_executionmodel_1.status = 'pending'
    engine_executionmodel_1 = importer.save_or_locate(engine_executionmodel_1)

    engine_executionmodel_2 = ExecutionModel()
    engine_executionmodel_2.started = dateutil.parser.parse("2018-08-13T10:10:00+00:00")
    engine_executionmodel_2.ended = dateutil.parser.parse("2018-08-17T10:10:00+00:00")
    engine_executionmodel_2.process = engine_processmodel_9
    engine_executionmodel_2.configuration = '{}'
    engine_executionmodel_2.status = 'pending'
    engine_executionmodel_2 = importer.save_or_locate(engine_executionmodel_2)

    engine_executionmodel_3 = ExecutionModel()
    engine_executionmodel_3.started = dateutil.parser.parse("2018-08-13T10:10:00+00:00")
    engine_executionmodel_3.ended = dateutil.parser.parse("2018-08-17T10:10:00+00:00")
    engine_executionmodel_3.process = engine_processmodel_9
    engine_executionmodel_3.configuration = '{}'
    engine_executionmodel_3.status = 'pending'
    engine_executionmodel_3 = importer.save_or_locate(engine_executionmodel_3)

    engine_executionmodel_4 = ExecutionModel()
    engine_executionmodel_4.started = dateutil.parser.parse("2018-08-13T10:10:00+00:00")
    engine_executionmodel_4.ended = dateutil.parser.parse("2018-08-17T10:10:00+00:00")
    engine_executionmodel_4.process = engine_processmodel_9
    engine_executionmodel_4.configuration = '{}'
    engine_executionmodel_4.status = 'completed'
    engine_executionmodel_4 = importer.save_or_locate(engine_executionmodel_4)

    engine_executionmodel_5 = ExecutionModel()
    engine_executionmodel_5.started = dateutil.parser.parse("2018-08-13T10:10:00+00:00")
    engine_executionmodel_5.ended = dateutil.parser.parse("2018-08-17T10:10:00+00:00")
    engine_executionmodel_5.process = engine_processmodel_9
    engine_executionmodel_5.configuration = '{}'
    engine_executionmodel_5.status = 'completed'
    engine_executionmodel_5 = importer.save_or_locate(engine_executionmodel_5)

    engine_executionmodel_6 = ExecutionModel()
    engine_executionmodel_6.started = dateutil.parser.parse("2018-08-13T10:10:00+00:00")
    engine_executionmodel_6.ended = dateutil.parser.parse("2018-08-17T10:10:00+00:00")
    engine_executionmodel_6.process = engine_processmodel_9
    engine_executionmodel_6.configuration = '{}'
    engine_executionmodel_6.status = 'completed'
    engine_executionmodel_6 = importer.save_or_locate(engine_executionmodel_6)

    engine_executionmodel_7 = ExecutionModel()
    engine_executionmodel_7.started = dateutil.parser.parse("2018-08-13T10:10:00+00:00")
    engine_executionmodel_7.ended = dateutil.parser.parse("2018-08-17T10:10:00+00:00")
    engine_executionmodel_7.process = engine_processmodel_9
    engine_executionmodel_7.configuration = '{}'
    engine_executionmodel_7.status = 'completed'
    engine_executionmodel_7 = importer.save_or_locate(engine_executionmodel_7)

    engine_executionmodel_8 = ExecutionModel()
    engine_executionmodel_8.started = dateutil.parser.parse("2018-08-13T10:10:00+00:00")
    engine_executionmodel_8.ended = dateutil.parser.parse("2018-08-17T10:10:00+00:00")
    engine_executionmodel_8.process = engine_processmodel_9
    engine_executionmodel_8.configuration = '{}'
    engine_executionmodel_8.status = 'paused'
    engine_executionmodel_8 = importer.save_or_locate(engine_executionmodel_8)

    engine_executionmodel_9 = ExecutionModel()
    engine_executionmodel_9.started = dateutil.parser.parse("2018-08-13T10:10:00+00:00")
    engine_executionmodel_9.ended = dateutil.parser.parse("2018-08-17T10:10:00+00:00")
    engine_executionmodel_9.process = engine_processmodel_9
    engine_executionmodel_9.configuration = '{}'
    engine_executionmodel_9.status = 'running'
    engine_executionmodel_9 = importer.save_or_locate(engine_executionmodel_9)

    engine_executionmodel_10 = ExecutionModel()
    engine_executionmodel_10.started = dateutil.parser.parse("2018-08-13T10:10:00+00:00")
    engine_executionmodel_10.ended = dateutil.parser.parse("2018-08-17T10:10:00+00:00")
    engine_executionmodel_10.process = engine_processmodel_9
    engine_executionmodel_10.configuration = '{}'
    engine_executionmodel_10.status = 'failed'
    engine_executionmodel_10 = importer.save_or_locate(engine_executionmodel_10)

    engine_executionmodel_11 = ExecutionModel()
    engine_executionmodel_11.started = dateutil.parser.parse("2018-08-05T01:17:30.797715+00:00")
    engine_executionmodel_11.ended = None
    engine_executionmodel_11.process = engine_processmodel_9
    engine_executionmodel_11.configuration = '{}'
    engine_executionmodel_11.status = 'pending'
    engine_executionmodel_11 = importer.save_or_locate(engine_executionmodel_11)

    engine_executionmodel_12 = ExecutionModel()
    engine_executionmodel_12.started = dateutil.parser.parse("2018-08-05T01:39:21.122598+00:00")
    engine_executionmodel_12.ended = None
    engine_executionmodel_12.process = engine_processmodel_9
    engine_executionmodel_12.configuration = '{}'
    engine_executionmodel_12.status = 'pending'
    engine_executionmodel_12 = importer.save_or_locate(engine_executionmodel_12)

    engine_executionmodel_13 = ExecutionModel()
    engine_executionmodel_13.started = dateutil.parser.parse("2018-08-05T01:57:56.755387+00:00")
    engine_executionmodel_13.ended = None
    engine_executionmodel_13.process = engine_processmodel_9
    engine_executionmodel_13.configuration = '{}'
    engine_executionmodel_13.status = 'pending'
    engine_executionmodel_13 = importer.save_or_locate(engine_executionmodel_13)

    engine_executionmodel_14 = ExecutionModel()
    engine_executionmodel_14.started = dateutil.parser.parse("2018-08-05T01:59:26.723574+00:00")
    engine_executionmodel_14.ended = None
    engine_executionmodel_14.process = engine_processmodel_9
    engine_executionmodel_14.configuration = '{}'
    engine_executionmodel_14.status = 'pending'
    engine_executionmodel_14 = importer.save_or_locate(engine_executionmodel_14)

    engine_executionmodel_15 = ExecutionModel()
    engine_executionmodel_15.started = dateutil.parser.parse("2018-08-05T02:00:49.963019+00:00")
    engine_executionmodel_15.ended = None
    engine_executionmodel_15.process = engine_processmodel_9
    engine_executionmodel_15.configuration = '{}'
    engine_executionmodel_15.status = 'pending'
    engine_executionmodel_15 = importer.save_or_locate(engine_executionmodel_15)

    engine_executionmodel_16 = ExecutionModel()
    engine_executionmodel_16.started = dateutil.parser.parse("2018-08-05T02:51:21.504681+00:00")
    engine_executionmodel_16.ended = None
    engine_executionmodel_16.process = engine_processmodel_9
    engine_executionmodel_16.configuration = '{}'
    engine_executionmodel_16.status = 'pending'
    engine_executionmodel_16 = importer.save_or_locate(engine_executionmodel_16)

    engine_executionmodel_17 = ExecutionModel()
    engine_executionmodel_17.started = dateutil.parser.parse("2018-08-05T02:53:24.491598+00:00")
    engine_executionmodel_17.ended = None
    engine_executionmodel_17.process = engine_processmodel_9
    engine_executionmodel_17.configuration = '{}'
    engine_executionmodel_17.status = 'pending'
    engine_executionmodel_17 = importer.save_or_locate(engine_executionmodel_17)

    engine_executionmodel_18 = ExecutionModel()
    engine_executionmodel_18.started = dateutil.parser.parse("2018-08-05T02:53:33.382678+00:00")
    engine_executionmodel_18.ended = None
    engine_executionmodel_18.process = engine_processmodel_9
    engine_executionmodel_18.configuration = '{}'
    engine_executionmodel_18.status = 'pending'
    engine_executionmodel_18 = importer.save_or_locate(engine_executionmodel_18)

    engine_executionmodel_19 = ExecutionModel()
    engine_executionmodel_19.started = dateutil.parser.parse("2018-08-05T02:54:38.289503+00:00")
    engine_executionmodel_19.ended = None
    engine_executionmodel_19.process = engine_processmodel_9
    engine_executionmodel_19.configuration = '{}'
    engine_executionmodel_19.status = 'pending'
    engine_executionmodel_19 = importer.save_or_locate(engine_executionmodel_19)

    engine_executionmodel_20 = ExecutionModel()
    engine_executionmodel_20.started = dateutil.parser.parse("2018-08-05T02:54:44.914500+00:00")
    engine_executionmodel_20.ended = None
    engine_executionmodel_20.process = engine_processmodel_9
    engine_executionmodel_20.configuration = '{}'
    engine_executionmodel_20.status = 'pending'
    engine_executionmodel_20 = importer.save_or_locate(engine_executionmodel_20)

    engine_executionmodel_21 = ExecutionModel()
    engine_executionmodel_21.started = dateutil.parser.parse("2018-08-05T02:57:28.925296+00:00")
    engine_executionmodel_21.ended = None
    engine_executionmodel_21.process = engine_processmodel_9
    engine_executionmodel_21.configuration = '{}'
    engine_executionmodel_21.status = 'pending'
    engine_executionmodel_21 = importer.save_or_locate(engine_executionmodel_21)

    engine_executionmodel_22 = ExecutionModel()
    engine_executionmodel_22.started = dateutil.parser.parse("2018-08-05T02:58:27.603306+00:00")
    engine_executionmodel_22.ended = None
    engine_executionmodel_22.process = engine_processmodel_9
    engine_executionmodel_22.configuration = '{}'
    engine_executionmodel_22.status = 'pending'
    engine_executionmodel_22 = importer.save_or_locate(engine_executionmodel_22)

    engine_executionmodel_23 = ExecutionModel()
    engine_executionmodel_23.started = dateutil.parser.parse("2018-08-05T02:59:39.134243+00:00")
    engine_executionmodel_23.ended = None
    engine_executionmodel_23.process = engine_processmodel_9
    engine_executionmodel_23.configuration = '{}'
    engine_executionmodel_23.status = 'pending'
    engine_executionmodel_23 = importer.save_or_locate(engine_executionmodel_23)

    engine_executionmodel_24 = ExecutionModel()
    engine_executionmodel_24.started = dateutil.parser.parse("2018-08-05T03:01:22.597465+00:00")
    engine_executionmodel_24.ended = None
    engine_executionmodel_24.process = engine_processmodel_9
    engine_executionmodel_24.configuration = '{}'
    engine_executionmodel_24.status = 'pending'
    engine_executionmodel_24 = importer.save_or_locate(engine_executionmodel_24)

    engine_executionmodel_25 = ExecutionModel()
    engine_executionmodel_25.started = dateutil.parser.parse("2018-08-05T03:02:43.969906+00:00")
    engine_executionmodel_25.ended = None
    engine_executionmodel_25.process = engine_processmodel_9
    engine_executionmodel_25.configuration = '{}'
    engine_executionmodel_25.status = 'pending'
    engine_executionmodel_25 = importer.save_or_locate(engine_executionmodel_25)

    engine_executionmodel_26 = ExecutionModel()
    engine_executionmodel_26.started = dateutil.parser.parse("2018-08-05T03:03:25.448926+00:00")
    engine_executionmodel_26.ended = None
    engine_executionmodel_26.process = engine_processmodel_9
    engine_executionmodel_26.configuration = '{}'
    engine_executionmodel_26.status = 'pending'
    engine_executionmodel_26 = importer.save_or_locate(engine_executionmodel_26)

    engine_executionmodel_27 = ExecutionModel()
    engine_executionmodel_27.started = dateutil.parser.parse("2018-08-05T03:08:21.265091+00:00")
    engine_executionmodel_27.ended = None
    engine_executionmodel_27.process = engine_processmodel_9
    engine_executionmodel_27.configuration = '{}'
    engine_executionmodel_27.status = 'pending'
    engine_executionmodel_27 = importer.save_or_locate(engine_executionmodel_27)

    engine_executionmodel_28 = ExecutionModel()
    engine_executionmodel_28.started = dateutil.parser.parse("2018-08-05T03:10:25.417005+00:00")
    engine_executionmodel_28.ended = None
    engine_executionmodel_28.process = engine_processmodel_9
    engine_executionmodel_28.configuration = '{}'
    engine_executionmodel_28.status = 'pending'
    engine_executionmodel_28 = importer.save_or_locate(engine_executionmodel_28)

    engine_executionmodel_29 = ExecutionModel()
    engine_executionmodel_29.started = dateutil.parser.parse("2018-08-05T03:13:36.552441+00:00")
    engine_executionmodel_29.ended = None
    engine_executionmodel_29.process = engine_processmodel_9
    engine_executionmodel_29.configuration = '{}'
    engine_executionmodel_29.status = 'pending'
    engine_executionmodel_29 = importer.save_or_locate(engine_executionmodel_29)

    engine_executionmodel_30 = ExecutionModel()
    engine_executionmodel_30.started = dateutil.parser.parse("2018-08-05T03:15:17.624896+00:00")
    engine_executionmodel_30.ended = None
    engine_executionmodel_30.process = engine_processmodel_9
    engine_executionmodel_30.configuration = '{}'
    engine_executionmodel_30.status = 'pending'
    engine_executionmodel_30 = importer.save_or_locate(engine_executionmodel_30)

    engine_executionmodel_31 = ExecutionModel()
    engine_executionmodel_31.started = dateutil.parser.parse("2018-08-05T03:15:45.970929+00:00")
    engine_executionmodel_31.ended = None
    engine_executionmodel_31.process = engine_processmodel_9
    engine_executionmodel_31.configuration = '{}'
    engine_executionmodel_31.status = 'pending'
    engine_executionmodel_31 = importer.save_or_locate(engine_executionmodel_31)

    engine_executionmodel_32 = ExecutionModel()
    engine_executionmodel_32.started = dateutil.parser.parse("2018-08-05T03:16:43.329423+00:00")
    engine_executionmodel_32.ended = None
    engine_executionmodel_32.process = engine_processmodel_9
    engine_executionmodel_32.configuration = '{}'
    engine_executionmodel_32.status = 'pending'
    engine_executionmodel_32 = importer.save_or_locate(engine_executionmodel_32)

    engine_executionmodel_33 = ExecutionModel()
    engine_executionmodel_33.started = dateutil.parser.parse("2018-08-05T03:17:41.685106+00:00")
    engine_executionmodel_33.ended = None
    engine_executionmodel_33.process = engine_processmodel_9
    engine_executionmodel_33.configuration = '{}'
    engine_executionmodel_33.status = 'pending'
    engine_executionmodel_33 = importer.save_or_locate(engine_executionmodel_33)

    engine_executionmodel_34 = ExecutionModel()
    engine_executionmodel_34.started = dateutil.parser.parse("2018-08-05T03:20:11.504172+00:00")
    engine_executionmodel_34.ended = None
    engine_executionmodel_34.process = engine_processmodel_9
    engine_executionmodel_34.configuration = '{}'
    engine_executionmodel_34.status = 'pending'
    engine_executionmodel_34 = importer.save_or_locate(engine_executionmodel_34)

    engine_executionmodel_35 = ExecutionModel()
    engine_executionmodel_35.started = dateutil.parser.parse("2018-08-05T03:20:52.699739+00:00")
    engine_executionmodel_35.ended = None
    engine_executionmodel_35.process = engine_processmodel_9
    engine_executionmodel_35.configuration = '{}'
    engine_executionmodel_35.status = 'pending'
    engine_executionmodel_35 = importer.save_or_locate(engine_executionmodel_35)

    engine_executionmodel_36 = ExecutionModel()
    engine_executionmodel_36.started = dateutil.parser.parse("2018-08-05T03:22:13.616939+00:00")
    engine_executionmodel_36.ended = None
    engine_executionmodel_36.process = engine_processmodel_9
    engine_executionmodel_36.configuration = '{}'
    engine_executionmodel_36.status = 'pending'
    engine_executionmodel_36 = importer.save_or_locate(engine_executionmodel_36)

    engine_executionmodel_37 = ExecutionModel()
    engine_executionmodel_37.started = dateutil.parser.parse("2018-08-05T03:23:09.664123+00:00")
    engine_executionmodel_37.ended = None
    engine_executionmodel_37.process = engine_processmodel_9
    engine_executionmodel_37.configuration = '{}'
    engine_executionmodel_37.status = 'pending'
    engine_executionmodel_37 = importer.save_or_locate(engine_executionmodel_37)

    engine_executionmodel_38 = ExecutionModel()
    engine_executionmodel_38.started = dateutil.parser.parse("2018-08-05T03:24:08.362232+00:00")
    engine_executionmodel_38.ended = None
    engine_executionmodel_38.process = engine_processmodel_9
    engine_executionmodel_38.configuration = '{}'
    engine_executionmodel_38.status = 'pending'
    engine_executionmodel_38 = importer.save_or_locate(engine_executionmodel_38)

    engine_executionmodel_39 = ExecutionModel()
    engine_executionmodel_39.started = dateutil.parser.parse("2018-08-05T03:25:01.818890+00:00")
    engine_executionmodel_39.ended = None
    engine_executionmodel_39.process = engine_processmodel_9
    engine_executionmodel_39.configuration = '{}'
    engine_executionmodel_39.status = 'pending'
    engine_executionmodel_39 = importer.save_or_locate(engine_executionmodel_39)

    engine_executionmodel_40 = ExecutionModel()
    engine_executionmodel_40.started = dateutil.parser.parse("2018-08-05T03:26:50.977547+00:00")
    engine_executionmodel_40.ended = None
    engine_executionmodel_40.process = engine_processmodel_9
    engine_executionmodel_40.configuration = '{}'
    engine_executionmodel_40.status = 'pending'
    engine_executionmodel_40 = importer.save_or_locate(engine_executionmodel_40)

    engine_executionmodel_41 = ExecutionModel()
    engine_executionmodel_41.started = dateutil.parser.parse("2018-08-05T03:27:06.453145+00:00")
    engine_executionmodel_41.ended = None
    engine_executionmodel_41.process = engine_processmodel_9
    engine_executionmodel_41.configuration = '{}'
    engine_executionmodel_41.status = 'pending'
    engine_executionmodel_41 = importer.save_or_locate(engine_executionmodel_41)

    engine_executionmodel_42 = ExecutionModel()
    engine_executionmodel_42.started = dateutil.parser.parse("2018-08-05T03:31:32.768032+00:00")
    engine_executionmodel_42.ended = None
    engine_executionmodel_42.process = engine_processmodel_9
    engine_executionmodel_42.configuration = '{}'
    engine_executionmodel_42.status = 'pending'
    engine_executionmodel_42 = importer.save_or_locate(engine_executionmodel_42)

    engine_executionmodel_43 = ExecutionModel()
    engine_executionmodel_43.started = dateutil.parser.parse("2018-08-05T03:31:50.034836+00:00")
    engine_executionmodel_43.ended = None
    engine_executionmodel_43.process = engine_processmodel_9
    engine_executionmodel_43.configuration = '{}'
    engine_executionmodel_43.status = 'pending'
    engine_executionmodel_43 = importer.save_or_locate(engine_executionmodel_43)

    engine_executionmodel_44 = ExecutionModel()
    engine_executionmodel_44.started = dateutil.parser.parse("2018-08-05T03:32:04.902872+00:00")
    engine_executionmodel_44.ended = None
    engine_executionmodel_44.process = engine_processmodel_9
    engine_executionmodel_44.configuration = '{}'
    engine_executionmodel_44.status = 'pending'
    engine_executionmodel_44 = importer.save_or_locate(engine_executionmodel_44)

    engine_executionmodel_45 = ExecutionModel()
    engine_executionmodel_45.started = dateutil.parser.parse("2018-08-05T03:43:12.307075+00:00")
    engine_executionmodel_45.ended = None
    engine_executionmodel_45.process = engine_processmodel_9
    engine_executionmodel_45.configuration = '{}'
    engine_executionmodel_45.status = 'pending'
    engine_executionmodel_45 = importer.save_or_locate(engine_executionmodel_45)

    engine_executionmodel_46 = ExecutionModel()
    engine_executionmodel_46.started = dateutil.parser.parse("2018-08-05T03:43:16.082921+00:00")
    engine_executionmodel_46.ended = None
    engine_executionmodel_46.process = engine_processmodel_9
    engine_executionmodel_46.configuration = '{}'
    engine_executionmodel_46.status = 'pending'
    engine_executionmodel_46 = importer.save_or_locate(engine_executionmodel_46)

    engine_executionmodel_47 = ExecutionModel()
    engine_executionmodel_47.started = dateutil.parser.parse("2018-08-05T03:43:32.666960+00:00")
    engine_executionmodel_47.ended = None
    engine_executionmodel_47.process = engine_processmodel_9
    engine_executionmodel_47.configuration = '{}'
    engine_executionmodel_47.status = 'pending'
    engine_executionmodel_47 = importer.save_or_locate(engine_executionmodel_47)

    engine_executionmodel_48 = ExecutionModel()
    engine_executionmodel_48.started = dateutil.parser.parse("2018-08-05T03:52:21.786338+00:00")
    engine_executionmodel_48.ended = None
    engine_executionmodel_48.process = engine_processmodel_9
    engine_executionmodel_48.configuration = '{}'
    engine_executionmodel_48.status = 'pending'
    engine_executionmodel_48 = importer.save_or_locate(engine_executionmodel_48)

    engine_executionmodel_49 = ExecutionModel()
    engine_executionmodel_49.started = dateutil.parser.parse("2018-08-05T03:52:51.299335+00:00")
    engine_executionmodel_49.ended = None
    engine_executionmodel_49.process = engine_processmodel_9
    engine_executionmodel_49.configuration = '{}'
    engine_executionmodel_49.status = 'pending'
    engine_executionmodel_49 = importer.save_or_locate(engine_executionmodel_49)

    engine_executionmodel_50 = ExecutionModel()
    engine_executionmodel_50.started = dateutil.parser.parse("2018-08-05T03:53:16.184150+00:00")
    engine_executionmodel_50.ended = None
    engine_executionmodel_50.process = engine_processmodel_9
    engine_executionmodel_50.configuration = '{}'
    engine_executionmodel_50.status = 'pending'
    engine_executionmodel_50 = importer.save_or_locate(engine_executionmodel_50)

    engine_executionmodel_51 = ExecutionModel()
    engine_executionmodel_51.started = dateutil.parser.parse("2018-08-05T03:54:01.359659+00:00")
    engine_executionmodel_51.ended = None
    engine_executionmodel_51.process = engine_processmodel_9
    engine_executionmodel_51.configuration = '{}'
    engine_executionmodel_51.status = 'pending'
    engine_executionmodel_51 = importer.save_or_locate(engine_executionmodel_51)

    engine_executionmodel_52 = ExecutionModel()
    engine_executionmodel_52.started = dateutil.parser.parse("2018-08-05T03:57:31.583321+00:00")
    engine_executionmodel_52.ended = None
    engine_executionmodel_52.process = engine_processmodel_9
    engine_executionmodel_52.configuration = '{}'
    engine_executionmodel_52.status = 'pending'
    engine_executionmodel_52 = importer.save_or_locate(engine_executionmodel_52)

    engine_executionmodel_53 = ExecutionModel()
    engine_executionmodel_53.started = dateutil.parser.parse("2018-08-05T03:58:22.323691+00:00")
    engine_executionmodel_53.ended = None
    engine_executionmodel_53.process = engine_processmodel_9
    engine_executionmodel_53.configuration = '{}'
    engine_executionmodel_53.status = 'pending'
    engine_executionmodel_53 = importer.save_or_locate(engine_executionmodel_53)

    engine_executionmodel_54 = ExecutionModel()
    engine_executionmodel_54.started = dateutil.parser.parse("2018-08-05T04:23:34.451451+00:00")
    engine_executionmodel_54.ended = None
    engine_executionmodel_54.process = engine_processmodel_9
    engine_executionmodel_54.configuration = '{"created": null, "to_location": null, "price": "10", "start": null, "from_location": null}'
    engine_executionmodel_54.status = 'pending'
    engine_executionmodel_54 = importer.save_or_locate(engine_executionmodel_54)

    engine_executionmodel_55 = ExecutionModel()
    engine_executionmodel_55.started = dateutil.parser.parse("2018-08-05T04:24:08.333310+00:00")
    engine_executionmodel_55.ended = None
    engine_executionmodel_55.process = engine_processmodel_9
    engine_executionmodel_55.configuration = '{"created": null, "to_location": null, "price": "10", "start": null, "from_location": null}'
    engine_executionmodel_55.status = 'pending'
    engine_executionmodel_55 = importer.save_or_locate(engine_executionmodel_55)

    engine_executionmodel_56 = ExecutionModel()
    engine_executionmodel_56.started = dateutil.parser.parse("2018-08-05T04:24:52.546108+00:00")
    engine_executionmodel_56.ended = None
    engine_executionmodel_56.process = engine_processmodel_9
    engine_executionmodel_56.configuration = '{"created": null, "to_location": null, "price": "10", "start": null, "from_location": null}'
    engine_executionmodel_56.status = 'pending'
    engine_executionmodel_56 = importer.save_or_locate(engine_executionmodel_56)

    engine_executionmodel_57 = ExecutionModel()
    engine_executionmodel_57.started = dateutil.parser.parse("2018-08-05T04:25:06.481662+00:00")
    engine_executionmodel_57.ended = None
    engine_executionmodel_57.process = engine_processmodel_9
    engine_executionmodel_57.configuration = '{"created": null, "to_location": null, "price": "10", "start": null, "from_location": null}'
    engine_executionmodel_57.status = 'pending'
    engine_executionmodel_57 = importer.save_or_locate(engine_executionmodel_57)

    engine_executionmodel_58 = ExecutionModel()
    engine_executionmodel_58.started = dateutil.parser.parse("2018-08-05T04:29:46.577935+00:00")
    engine_executionmodel_58.ended = None
    engine_executionmodel_58.process = engine_processmodel_9
    engine_executionmodel_58.configuration = '{"created": null, "to_location": null, "price": "10", "start": null, "from_location": null}'
    engine_executionmodel_58.status = 'pending'
    engine_executionmodel_58 = importer.save_or_locate(engine_executionmodel_58)

    engine_executionmodel_59 = ExecutionModel()
    engine_executionmodel_59.started = dateutil.parser.parse("2018-08-05T04:30:19.643979+00:00")
    engine_executionmodel_59.ended = None
    engine_executionmodel_59.process = engine_processmodel_9
    engine_executionmodel_59.configuration = '{"created": null, "to_location": null, "price": "10", "start": null, "from_location": null}'
    engine_executionmodel_59.status = 'pending'
    engine_executionmodel_59 = importer.save_or_locate(engine_executionmodel_59)

    engine_executionmodel_60 = ExecutionModel()
    engine_executionmodel_60.started = dateutil.parser.parse("2018-08-05T04:31:47.954697+00:00")
    engine_executionmodel_60.ended = None
    engine_executionmodel_60.process = engine_processmodel_9
    engine_executionmodel_60.configuration = '{"created": null, "to_location": null, "price": "10", "start": null, "from_location": null}'
    engine_executionmodel_60.status = 'pending'
    engine_executionmodel_60 = importer.save_or_locate(engine_executionmodel_60)

    engine_executionmodel_61 = ExecutionModel()
    engine_executionmodel_61.started = dateutil.parser.parse("2018-08-05T04:32:36.827156+00:00")
    engine_executionmodel_61.ended = None
    engine_executionmodel_61.process = engine_processmodel_9
    engine_executionmodel_61.configuration = '{"created": null, "to_location": null, "price": "10", "start": null, "from_location": null}'
    engine_executionmodel_61.status = 'pending'
    engine_executionmodel_61 = importer.save_or_locate(engine_executionmodel_61)

    engine_executionmodel_62 = ExecutionModel()
    engine_executionmodel_62.started = dateutil.parser.parse("2018-08-05T04:35:58.466769+00:00")
    engine_executionmodel_62.ended = None
    engine_executionmodel_62.process = engine_processmodel_9
    engine_executionmodel_62.configuration = '{"created": null, "to_location": null, "price": "10", "start": null, "from_location": null}'
    engine_executionmodel_62.status = 'pending'
    engine_executionmodel_62 = importer.save_or_locate(engine_executionmodel_62)

    engine_executionmodel_63 = ExecutionModel()
    engine_executionmodel_63.started = dateutil.parser.parse("2018-08-05T04:37:02.929439+00:00")
    engine_executionmodel_63.ended = None
    engine_executionmodel_63.process = engine_processmodel_9
    engine_executionmodel_63.configuration = '{"created": null, "to_location": null, "price": "10", "start": null, "from_location": null}'
    engine_executionmodel_63.status = 'pending'
    engine_executionmodel_63 = importer.save_or_locate(engine_executionmodel_63)

    engine_executionmodel_64 = ExecutionModel()
    engine_executionmodel_64.started = dateutil.parser.parse("2018-08-05T04:37:58.202441+00:00")
    engine_executionmodel_64.ended = None
    engine_executionmodel_64.process = engine_processmodel_9
    engine_executionmodel_64.configuration = '{"created": null, "to_location": null, "price": "10", "start": null, "from_location": null}'
    engine_executionmodel_64.status = 'pending'
    engine_executionmodel_64 = importer.save_or_locate(engine_executionmodel_64)

    engine_executionmodel_65 = ExecutionModel()
    engine_executionmodel_65.started = dateutil.parser.parse("2018-08-05T04:39:58.047472+00:00")
    engine_executionmodel_65.ended = None
    engine_executionmodel_65.process = engine_processmodel_9
    engine_executionmodel_65.configuration = '{"to_location": null, "price": "10", "from_location": null, "created": null, "start": null}'
    engine_executionmodel_65.status = 'pending'
    engine_executionmodel_65 = importer.save_or_locate(engine_executionmodel_65)

    engine_executionmodel_66 = ExecutionModel()
    engine_executionmodel_66.started = dateutil.parser.parse("2018-08-05T04:41:20.772601+00:00")
    engine_executionmodel_66.ended = None
    engine_executionmodel_66.process = engine_processmodel_9
    engine_executionmodel_66.configuration = '{"start": null, "created": null, "from_location": null, "price": "10", "to_location": null}'
    engine_executionmodel_66.status = 'pending'
    engine_executionmodel_66 = importer.save_or_locate(engine_executionmodel_66)

    engine_executionmodel_67 = ExecutionModel()
    engine_executionmodel_67.started = dateutil.parser.parse("2018-08-05T04:42:51.871910+00:00")
    engine_executionmodel_67.ended = None
    engine_executionmodel_67.process = engine_processmodel_9
    engine_executionmodel_67.configuration = '{"from_location": null, "price": "10", "to_location": null, "created": null, "start": null}'
    engine_executionmodel_67.status = 'pending'
    engine_executionmodel_67 = importer.save_or_locate(engine_executionmodel_67)

    engine_executionmodel_68 = ExecutionModel()
    engine_executionmodel_68.started = dateutil.parser.parse("2018-08-05T04:43:54.971970+00:00")
    engine_executionmodel_68.ended = None
    engine_executionmodel_68.process = engine_processmodel_9
    engine_executionmodel_68.configuration = '{"price": "10", "to_location": null, "start": null, "from_location": null, "created": null}'
    engine_executionmodel_68.status = 'pending'
    engine_executionmodel_68 = importer.save_or_locate(engine_executionmodel_68)

    engine_executionmodel_69 = ExecutionModel()
    engine_executionmodel_69.started = dateutil.parser.parse("2018-08-05T04:45:06.040978+00:00")
    engine_executionmodel_69.ended = None
    engine_executionmodel_69.process = engine_processmodel_9
    engine_executionmodel_69.configuration = '{"start": null, "created": null, "from_location": null, "to_location": null, "price": "10"}'
    engine_executionmodel_69.status = 'pending'
    engine_executionmodel_69 = importer.save_or_locate(engine_executionmodel_69)

    engine_executionmodel_70 = ExecutionModel()
    engine_executionmodel_70.started = dateutil.parser.parse("2018-08-05T04:46:27.711650+00:00")
    engine_executionmodel_70.ended = None
    engine_executionmodel_70.process = engine_processmodel_9
    engine_executionmodel_70.configuration = '{"start": null, "created": null, "from_location": null, "to_location": null, "price": "10"}'
    engine_executionmodel_70.status = 'pending'
    engine_executionmodel_70 = importer.save_or_locate(engine_executionmodel_70)

    engine_executionmodel_71 = ExecutionModel()
    engine_executionmodel_71.started = dateutil.parser.parse("2018-08-05T04:48:25.651401+00:00")
    engine_executionmodel_71.ended = None
    engine_executionmodel_71.process = engine_processmodel_9
    engine_executionmodel_71.configuration = '{"start": null, "created": null, "from_location": null, "to_location": null, "price": "10"}'
    engine_executionmodel_71.status = 'pending'
    engine_executionmodel_71 = importer.save_or_locate(engine_executionmodel_71)

    engine_executionmodel_72 = ExecutionModel()
    engine_executionmodel_72.started = dateutil.parser.parse("2018-08-05T04:49:33.289410+00:00")
    engine_executionmodel_72.ended = None
    engine_executionmodel_72.process = engine_processmodel_9
    engine_executionmodel_72.configuration = '{"from_location": null, "start": null, "to_location": null, "price": "10", "created": null}'
    engine_executionmodel_72.status = 'pending'
    engine_executionmodel_72 = importer.save_or_locate(engine_executionmodel_72)

    engine_executionmodel_73 = ExecutionModel()
    engine_executionmodel_73.started = dateutil.parser.parse("2018-08-05T04:50:22.624971+00:00")
    engine_executionmodel_73.ended = None
    engine_executionmodel_73.process = engine_processmodel_9
    engine_executionmodel_73.configuration = '{"from_location": null, "start": null, "to_location": null, "price": "10", "created": null}'
    engine_executionmodel_73.status = 'pending'
    engine_executionmodel_73 = importer.save_or_locate(engine_executionmodel_73)

    engine_executionmodel_74 = ExecutionModel()
    engine_executionmodel_74.started = dateutil.parser.parse("2018-08-05T04:54:20.128633+00:00")
    engine_executionmodel_74.ended = None
    engine_executionmodel_74.process = engine_processmodel_9
    engine_executionmodel_74.configuration = '{"from_location": null, "start": null, "to_location": null, "price": "10", "created": null}'
    engine_executionmodel_74.status = 'pending'
    engine_executionmodel_74 = importer.save_or_locate(engine_executionmodel_74)

    engine_executionmodel_75 = ExecutionModel()
    engine_executionmodel_75.started = dateutil.parser.parse("2018-08-05T04:56:34.894738+00:00")
    engine_executionmodel_75.ended = None
    engine_executionmodel_75.process = engine_processmodel_9
    engine_executionmodel_75.configuration = '{"price": "10", "start": null, "to_location": null, "from_location": null, "created": null}'
    engine_executionmodel_75.status = 'pending'
    engine_executionmodel_75 = importer.save_or_locate(engine_executionmodel_75)

    engine_executionmodel_76 = ExecutionModel()
    engine_executionmodel_76.started = dateutil.parser.parse("2018-08-05T04:58:47.306378+00:00")
    engine_executionmodel_76.ended = None
    engine_executionmodel_76.process = engine_processmodel_9
    engine_executionmodel_76.configuration = '{"price": "10", "start": null, "to_location": null, "from_location": null, "created": null}'
    engine_executionmodel_76.status = 'pending'
    engine_executionmodel_76 = importer.save_or_locate(engine_executionmodel_76)

    engine_executionmodel_77 = ExecutionModel()
    engine_executionmodel_77.started = dateutil.parser.parse("2018-08-05T05:02:25.509732+00:00")
    engine_executionmodel_77.ended = None
    engine_executionmodel_77.process = engine_processmodel_9
    engine_executionmodel_77.configuration = '{"start": null, "to_location": null, "created": null, "from_location": null, "price": "10"}'
    engine_executionmodel_77.status = 'pending'
    engine_executionmodel_77 = importer.save_or_locate(engine_executionmodel_77)

    engine_executionmodel_78 = ExecutionModel()
    engine_executionmodel_78.started = dateutil.parser.parse("2018-08-05T05:10:49.808365+00:00")
    engine_executionmodel_78.ended = None
    engine_executionmodel_78.process = engine_processmodel_9
    engine_executionmodel_78.configuration = '{"start": null, "to_location": null, "created": null, "from_location": null, "price": "10"}'
    engine_executionmodel_78.status = 'pending'
    engine_executionmodel_78 = importer.save_or_locate(engine_executionmodel_78)

    engine_executionmodel_79 = ExecutionModel()
    engine_executionmodel_79.started = dateutil.parser.parse("2018-08-05T05:13:35.147327+00:00")
    engine_executionmodel_79.ended = None
    engine_executionmodel_79.process = engine_processmodel_9
    engine_executionmodel_79.configuration = '{"start": null, "to_location": null, "created": null, "from_location": null, "price": "10"}'
    engine_executionmodel_79.status = 'pending'
    engine_executionmodel_79 = importer.save_or_locate(engine_executionmodel_79)

    engine_executionmodel_80 = ExecutionModel()
    engine_executionmodel_80.started = dateutil.parser.parse("2018-08-05T05:35:02.759901+00:00")
    engine_executionmodel_80.ended = None
    engine_executionmodel_80.process = engine_processmodel_9
    engine_executionmodel_80.configuration = '{"to_location": null, "price": "10", "from_location": null, "created": null, "start": null}'
    engine_executionmodel_80.status = 'pending'
    engine_executionmodel_80 = importer.save_or_locate(engine_executionmodel_80)

    engine_executionmodel_81 = ExecutionModel()
    engine_executionmodel_81.started = dateutil.parser.parse("2018-08-05T05:36:57.155287+00:00")
    engine_executionmodel_81.ended = None
    engine_executionmodel_81.process = engine_processmodel_9
    engine_executionmodel_81.configuration = '{"from_location": null, "created": null, "price": "10", "start": null, "to_location": null}'
    engine_executionmodel_81.status = 'pending'
    engine_executionmodel_81 = importer.save_or_locate(engine_executionmodel_81)

    engine_executionmodel_82 = ExecutionModel()
    engine_executionmodel_82.started = dateutil.parser.parse("2018-08-05T05:38:25.805861+00:00")
    engine_executionmodel_82.ended = None
    engine_executionmodel_82.process = engine_processmodel_9
    engine_executionmodel_82.configuration = '{"to_location": null, "price": "10", "start": null, "created": null, "from_location": null}'
    engine_executionmodel_82.status = 'pending'
    engine_executionmodel_82 = importer.save_or_locate(engine_executionmodel_82)

    engine_executionmodel_83 = ExecutionModel()
    engine_executionmodel_83.started = dateutil.parser.parse("2018-08-05T05:39:11.801753+00:00")
    engine_executionmodel_83.ended = None
    engine_executionmodel_83.process = engine_processmodel_9
    engine_executionmodel_83.configuration = '{"start": null, "from_location": null, "created": null, "to_location": null, "price": "10"}'
    engine_executionmodel_83.status = 'pending'
    engine_executionmodel_83 = importer.save_or_locate(engine_executionmodel_83)

    engine_executionmodel_84 = ExecutionModel()
    engine_executionmodel_84.started = dateutil.parser.parse("2018-08-05T05:46:35.133730+00:00")
    engine_executionmodel_84.ended = None
    engine_executionmodel_84.process = engine_processmodel_9
    engine_executionmodel_84.configuration = '{"from_location": null, "start": null, "to_location": null, "price": "10", "created": null}'
    engine_executionmodel_84.status = 'pending'
    engine_executionmodel_84 = importer.save_or_locate(engine_executionmodel_84)

    engine_executionmodel_85 = ExecutionModel()
    engine_executionmodel_85.started = dateutil.parser.parse("2018-08-05T05:53:07.860439+00:00")
    engine_executionmodel_85.ended = None
    engine_executionmodel_85.process = engine_processmodel_9
    engine_executionmodel_85.configuration = '{"from_location": null, "to_location": null, "price": "10", "start": null, "created": null}'
    engine_executionmodel_85.status = 'pending'
    engine_executionmodel_85 = importer.save_or_locate(engine_executionmodel_85)

    engine_executionmodel_86 = ExecutionModel()
    engine_executionmodel_86.started = dateutil.parser.parse("2018-08-05T05:53:59.748095+00:00")
    engine_executionmodel_86.ended = None
    engine_executionmodel_86.process = engine_processmodel_9
    engine_executionmodel_86.configuration = '{"to_location": null, "created": null, "from_location": null, "start": null, "price": "10"}'
    engine_executionmodel_86.status = 'pending'
    engine_executionmodel_86 = importer.save_or_locate(engine_executionmodel_86)

    engine_executionmodel_87 = ExecutionModel()
    engine_executionmodel_87.started = dateutil.parser.parse("2018-08-05T05:55:28.920629+00:00")
    engine_executionmodel_87.ended = None
    engine_executionmodel_87.process = engine_processmodel_9
    engine_executionmodel_87.configuration = '{"to_location": null, "created": null, "from_location": null, "start": null, "price": "10"}'
    engine_executionmodel_87.status = 'pending'
    engine_executionmodel_87 = importer.save_or_locate(engine_executionmodel_87)

    engine_executionmodel_88 = ExecutionModel()
    engine_executionmodel_88.started = dateutil.parser.parse("2018-08-05T05:57:23.613056+00:00")
    engine_executionmodel_88.ended = None
    engine_executionmodel_88.process = engine_processmodel_9
    engine_executionmodel_88.configuration = '{"to_location": null, "created": null, "from_location": null, "start": null, "price": "10"}'
    engine_executionmodel_88.status = 'pending'
    engine_executionmodel_88 = importer.save_or_locate(engine_executionmodel_88)

    engine_executionmodel_89 = ExecutionModel()
    engine_executionmodel_89.started = dateutil.parser.parse("2018-08-05T05:58:47.070245+00:00")
    engine_executionmodel_89.ended = None
    engine_executionmodel_89.process = engine_processmodel_9
    engine_executionmodel_89.configuration = '{"created": null, "start": null, "price": "10", "to_location": null, "from_location": null}'
    engine_executionmodel_89.status = 'pending'
    engine_executionmodel_89 = importer.save_or_locate(engine_executionmodel_89)

    engine_executionmodel_90 = ExecutionModel()
    engine_executionmodel_90.started = dateutil.parser.parse("2018-08-05T05:59:52.510785+00:00")
    engine_executionmodel_90.ended = None
    engine_executionmodel_90.process = engine_processmodel_9
    engine_executionmodel_90.configuration = '{"price": "10", "start": null, "to_location": null, "created": null, "from_location": null}'
    engine_executionmodel_90.status = 'pending'
    engine_executionmodel_90 = importer.save_or_locate(engine_executionmodel_90)

    engine_executionmodel_91 = ExecutionModel()
    engine_executionmodel_91.started = dateutil.parser.parse("2018-08-05T06:01:21.279582+00:00")
    engine_executionmodel_91.ended = None
    engine_executionmodel_91.process = engine_processmodel_9
    engine_executionmodel_91.configuration = '{"to_location": null, "start": null, "created": null, "price": "10", "from_location": null}'
    engine_executionmodel_91.status = 'pending'
    engine_executionmodel_91 = importer.save_or_locate(engine_executionmodel_91)

    engine_executionmodel_92 = ExecutionModel()
    engine_executionmodel_92.started = dateutil.parser.parse("2018-08-05T06:02:20.227294+00:00")
    engine_executionmodel_92.ended = None
    engine_executionmodel_92.process = engine_processmodel_9
    engine_executionmodel_92.configuration = '{"start": null, "to_location": null, "price": "10", "created": null, "from_location": null}'
    engine_executionmodel_92.status = 'pending'
    engine_executionmodel_92 = importer.save_or_locate(engine_executionmodel_92)

    engine_executionmodel_93 = ExecutionModel()
    engine_executionmodel_93.started = dateutil.parser.parse("2018-08-05T06:04:23.064257+00:00")
    engine_executionmodel_93.ended = None
    engine_executionmodel_93.process = engine_processmodel_9
    engine_executionmodel_93.configuration = '{"from_location": null, "to_location": null, "created": null, "start": null, "price": "10"}'
    engine_executionmodel_93.status = 'pending'
    engine_executionmodel_93 = importer.save_or_locate(engine_executionmodel_93)

    engine_executionmodel_94 = ExecutionModel()
    engine_executionmodel_94.started = dateutil.parser.parse("2018-08-05T06:04:56.497302+00:00")
    engine_executionmodel_94.ended = None
    engine_executionmodel_94.process = engine_processmodel_9
    engine_executionmodel_94.configuration = '{"price": "10", "from_location": null, "created": null, "to_location": null, "start": null}'
    engine_executionmodel_94.status = 'pending'
    engine_executionmodel_94 = importer.save_or_locate(engine_executionmodel_94)

    engine_executionmodel_95 = ExecutionModel()
    engine_executionmodel_95.started = dateutil.parser.parse("2018-08-05T06:08:06.811447+00:00")
    engine_executionmodel_95.ended = None
    engine_executionmodel_95.process = engine_processmodel_9
    engine_executionmodel_95.configuration = '{"start": null, "from_location": null, "created": null, "price": "10", "to_location": null}'
    engine_executionmodel_95.status = 'pending'
    engine_executionmodel_95 = importer.save_or_locate(engine_executionmodel_95)

    engine_executionmodel_96 = ExecutionModel()
    engine_executionmodel_96.started = dateutil.parser.parse("2018-08-05T06:10:47.186838+00:00")
    engine_executionmodel_96.ended = None
    engine_executionmodel_96.process = engine_processmodel_9
    engine_executionmodel_96.configuration = '{"to_location": null, "from_location": null, "start": null, "created": null, "price": "10"}'
    engine_executionmodel_96.status = 'pending'
    engine_executionmodel_96 = importer.save_or_locate(engine_executionmodel_96)

    engine_executionmodel_97 = ExecutionModel()
    engine_executionmodel_97.started = dateutil.parser.parse("2018-08-05T06:15:12.786808+00:00")
    engine_executionmodel_97.ended = None
    engine_executionmodel_97.process = engine_processmodel_9
    engine_executionmodel_97.configuration = '{"price": "10", "to_location": null, "from_location": null, "start": null, "created": null}'
    engine_executionmodel_97.status = 'pending'
    engine_executionmodel_97 = importer.save_or_locate(engine_executionmodel_97)

    engine_executionmodel_98 = ExecutionModel()
    engine_executionmodel_98.started = dateutil.parser.parse("2018-08-05T06:17:10.385545+00:00")
    engine_executionmodel_98.ended = None
    engine_executionmodel_98.process = engine_processmodel_9
    engine_executionmodel_98.configuration = '{"start": null, "to_location": null, "created": null, "price": "10", "from_location": null}'
    engine_executionmodel_98.status = 'pending'
    engine_executionmodel_98 = importer.save_or_locate(engine_executionmodel_98)

    engine_executionmodel_99 = ExecutionModel()
    engine_executionmodel_99.started = dateutil.parser.parse("2018-08-05T06:17:59.275901+00:00")
    engine_executionmodel_99.ended = None
    engine_executionmodel_99.process = engine_processmodel_9
    engine_executionmodel_99.configuration = '{"to_location": null, "price": "10", "created": null, "from_location": null, "start": null}'
    engine_executionmodel_99.status = 'pending'
    engine_executionmodel_99 = importer.save_or_locate(engine_executionmodel_99)

    engine_executionmodel_100 = ExecutionModel()
    engine_executionmodel_100.started = dateutil.parser.parse("2018-08-05T06:19:32.564632+00:00")
    engine_executionmodel_100.ended = None
    engine_executionmodel_100.process = engine_processmodel_9
    engine_executionmodel_100.configuration = '{"start": null, "from_location": null, "to_location": null, "price": "10", "created": null}'
    engine_executionmodel_100.status = 'pending'
    engine_executionmodel_100 = importer.save_or_locate(engine_executionmodel_100)

    engine_executionmodel_101 = ExecutionModel()
    engine_executionmodel_101.started = dateutil.parser.parse("2018-08-05T06:20:03.249182+00:00")
    engine_executionmodel_101.ended = None
    engine_executionmodel_101.process = engine_processmodel_9
    engine_executionmodel_101.configuration = '{"created": null, "start": null, "from_location": null, "price": "10", "to_location": null}'
    engine_executionmodel_101.status = 'pending'
    engine_executionmodel_101 = importer.save_or_locate(engine_executionmodel_101)

    engine_executionmodel_102 = ExecutionModel()
    engine_executionmodel_102.started = dateutil.parser.parse("2018-08-05T06:25:02.248726+00:00")
    engine_executionmodel_102.ended = None
    engine_executionmodel_102.process = engine_processmodel_9
    engine_executionmodel_102.configuration = '{"price": "10", "to_location": null, "from_location": null, "start": null, "created": null}'
    engine_executionmodel_102.status = 'pending'
    engine_executionmodel_102 = importer.save_or_locate(engine_executionmodel_102)

    engine_executionmodel_103 = ExecutionModel()
    engine_executionmodel_103.started = dateutil.parser.parse("2018-08-05T06:26:11.529152+00:00")
    engine_executionmodel_103.ended = None
    engine_executionmodel_103.process = engine_processmodel_9
    engine_executionmodel_103.configuration = '{"to_location": null, "created": null, "price": "10", "from_location": null, "start": null}'
    engine_executionmodel_103.status = 'pending'
    engine_executionmodel_103 = importer.save_or_locate(engine_executionmodel_103)

    engine_executionmodel_104 = ExecutionModel()
    engine_executionmodel_104.started = dateutil.parser.parse("2018-08-05T13:18:15.847995+00:00")
    engine_executionmodel_104.ended = None
    engine_executionmodel_104.process = engine_processmodel_9
    engine_executionmodel_104.configuration = '{"from_location": null, "price": "10", "start": null, "to_location": null, "created": null}'
    engine_executionmodel_104.status = 'pending'
    engine_executionmodel_104 = importer.save_or_locate(engine_executionmodel_104)

    engine_executionmodel_105 = ExecutionModel()
    engine_executionmodel_105.started = dateutil.parser.parse("2018-08-05T13:21:24.355009+00:00")
    engine_executionmodel_105.ended = None
    engine_executionmodel_105.process = engine_processmodel_9
    engine_executionmodel_105.configuration = '{"from_location": null, "created": null, "to_location": null, "price": "10", "start": null}'
    engine_executionmodel_105.status = 'pending'
    engine_executionmodel_105 = importer.save_or_locate(engine_executionmodel_105)

    engine_executionmodel_106 = ExecutionModel()
    engine_executionmodel_106.started = dateutil.parser.parse("2018-08-05T13:25:27.074092+00:00")
    engine_executionmodel_106.ended = dateutil.parser.parse("2018-08-05T13:25:36.130937+00:00")
    engine_executionmodel_106.process = engine_processmodel_9
    engine_executionmodel_106.configuration = '{"from_location": null, "to_location": null, "price": "10", "created": null, "start": null}'
    engine_executionmodel_106.status = 'completed'
    engine_executionmodel_106 = importer.save_or_locate(engine_executionmodel_106)

    engine_executionmodel_107 = ExecutionModel()
    engine_executionmodel_107.started = dateutil.parser.parse("2018-08-05T13:34:07.255559+00:00")
    engine_executionmodel_107.ended = dateutil.parser.parse("2018-08-05T13:34:16.319846+00:00")
    engine_executionmodel_107.process = engine_processmodel_9
    engine_executionmodel_107.configuration = '{"price": "100", "to_location": "London", "created": "2018-08-06T10:00:00", "from_location": "Budapest", "start": "2018-08-06T12:00:00"}'
    engine_executionmodel_107.status = 'completed'
    engine_executionmodel_107 = importer.save_or_locate(engine_executionmodel_107)

    engine_executionmodel_108 = ExecutionModel()
    engine_executionmodel_108.started = dateutil.parser.parse("2018-08-05T13:26:44.686197+00:00")
    engine_executionmodel_108.ended = dateutil.parser.parse("2018-08-05T13:26:53.741211+00:00")
    engine_executionmodel_108.process = engine_processmodel_9
    engine_executionmodel_108.configuration = '{"price": "10", "to_location": null, "created": null, "from_location": null, "start": null}'
    engine_executionmodel_108.status = 'completed'
    engine_executionmodel_108 = importer.save_or_locate(engine_executionmodel_108)

    engine_executionmodel_109 = ExecutionModel()
    engine_executionmodel_109.started = dateutil.parser.parse("2018-08-07T14:02:32.115126+00:00")
    engine_executionmodel_109.ended = None
    engine_executionmodel_109.process = engine_processmodel_9
    engine_executionmodel_109.configuration = '{"price": "100", "to_location": "London", "from_location": "Budapest", "start": "2018-08-06T12:00:00.0Z", "created": "2018-08-06T10:00:00.0Z"}'
    engine_executionmodel_109.status = 'running'
    engine_executionmodel_109 = importer.save_or_locate(engine_executionmodel_109)

    engine_executionmodel_110 = ExecutionModel()
    engine_executionmodel_110.started = dateutil.parser.parse("2018-08-07T14:02:32.116332+00:00")
    engine_executionmodel_110.ended = None
    engine_executionmodel_110.process = engine_processmodel_9
    engine_executionmodel_110.configuration = '{"price": "100", "to_location": "London", "from_location": "Budapest", "start": "2018-08-06T12:00:00.0Z", "created": "2018-08-06T10:00:00.0Z"}'
    engine_executionmodel_110.status = 'running'
    engine_executionmodel_110 = importer.save_or_locate(engine_executionmodel_110)

    engine_executionmodel_111 = ExecutionModel()
    engine_executionmodel_111.started = dateutil.parser.parse("2018-08-07T14:43:40.936728+00:00")
    engine_executionmodel_111.ended = None
    engine_executionmodel_111.process = engine_processmodel_9
    engine_executionmodel_111.configuration = '{"to_location": "London", "created": "2018-08-06T10:00:00.0Z", "start": "2018-08-06T12:00:00.0Z", "price": "100", "from_location": "Budapest"}'
    engine_executionmodel_111.status = 'running'
    engine_executionmodel_111 = importer.save_or_locate(engine_executionmodel_111)

    engine_executionmodel_112 = ExecutionModel()
    engine_executionmodel_112.started = dateutil.parser.parse("2018-08-07T16:36:19.989469+00:00")
    engine_executionmodel_112.ended = None
    engine_executionmodel_112.process = engine_processmodel_10
    engine_executionmodel_112.configuration = '{"arrival_date": null}'
    engine_executionmodel_112.status = 'running'
    engine_executionmodel_112 = importer.save_or_locate(engine_executionmodel_112)

