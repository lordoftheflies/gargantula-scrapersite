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
# ./manage.py dumpscript botapp
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

    # Processing model: botapp.models.ProjectModel

    from botapp.models import ProjectModel

    botapp_projectmodel_1 = ProjectModel()
    botapp_projectmodel_1.name = 'RyanAir Holidays'
    botapp_projectmodel_1.scrapy = 'portalcrawler'
    botapp_projectmodel_1.version = '3.13.54'
    botapp_projectmodel_1.spider = 'angular'
    botapp_projectmodel_1.portal_url = 'https://www.ryanair.com/hu/hu/'
    botapp_projectmodel_1 = importer.save_or_locate(botapp_projectmodel_1)

    # Processing model: botapp.models.ClickAndWaitProjectStepModel

    from botapp.models import ClickAndWaitProjectStepModel

    botapp_projectstepmodel_1 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_1.display_name = 'Indulási állomás felugró megnyitása'
    botapp_projectstepmodel_1.order_index = 1
    botapp_projectstepmodel_1.action_type = 'clickAndWait'
    botapp_projectstepmodel_1.value = '1.0'
    botapp_projectstepmodel_1.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_1.variable = False
    botapp_projectstepmodel_1.project = botapp_projectmodel_1
    botapp_projectstepmodel_1 = importer.save_or_locate(botapp_projectstepmodel_1)

    botapp_projectstepmodel_2 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_2.display_name = 'Indulási ország kiválasztása'
    botapp_projectstepmodel_2.order_index = 2
    botapp_projectstepmodel_2.action_type = 'clickAndWait'
    botapp_projectstepmodel_2.value = '1.0'
    botapp_projectstepmodel_2.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div.core-list-item.core-list-item-rounded.clicked'
    botapp_projectstepmodel_2.variable = False
    botapp_projectstepmodel_2.project = botapp_projectmodel_1
    botapp_projectstepmodel_2 = importer.save_or_locate(botapp_projectstepmodel_2)

    botapp_projectstepmodel_3 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_3.display_name = 'Indulási repülőtér kiválasztása'
    botapp_projectstepmodel_3.order_index = 3
    botapp_projectstepmodel_3.action_type = 'clickAndWait'
    botapp_projectstepmodel_3.value = '1.0'
    botapp_projectstepmodel_3.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div.core-list-item.core-list-item-rounded.clicked > span'
    botapp_projectstepmodel_3.variable = False
    botapp_projectstepmodel_3.project = botapp_projectmodel_1
    botapp_projectstepmodel_3 = importer.save_or_locate(botapp_projectstepmodel_3)

    botapp_projectstepmodel_4 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_4.display_name = 'Érkezési állomás felugró megnyitása'
    botapp_projectstepmodel_4.order_index = 4
    botapp_projectstepmodel_4.action_type = 'clickAndWait'
    botapp_projectstepmodel_4.value = '1.0'
    botapp_projectstepmodel_4.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_4.variable = False
    botapp_projectstepmodel_4.project = botapp_projectmodel_1
    botapp_projectstepmodel_4 = importer.save_or_locate(botapp_projectstepmodel_4)

    botapp_projectstepmodel_5 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_5.display_name = 'Érkezési ország kiválasztása'
    botapp_projectstepmodel_5.order_index = 5
    botapp_projectstepmodel_5.action_type = 'clickAndWait'
    botapp_projectstepmodel_5.value = '1.0'
    botapp_projectstepmodel_5.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div:nth-child(4)'
    botapp_projectstepmodel_5.variable = False
    botapp_projectstepmodel_5.project = botapp_projectmodel_1
    botapp_projectstepmodel_5 = importer.save_or_locate(botapp_projectstepmodel_5)

    botapp_projectstepmodel_6 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_6.display_name = 'Érkezési repülőtér kiválasztása'
    botapp_projectstepmodel_6.order_index = 6
    botapp_projectstepmodel_6.action_type = 'clickAndWait'
    botapp_projectstepmodel_6.value = '1.0'
    botapp_projectstepmodel_6.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div:nth-child(3) > span'
    botapp_projectstepmodel_6.variable = False
    botapp_projectstepmodel_6.project = botapp_projectmodel_1
    botapp_projectstepmodel_6 = importer.save_or_locate(botapp_projectstepmodel_6)

    botapp_projectstepmodel_7 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_7.display_name = 'Utasok felugró kiválasztása'
    botapp_projectstepmodel_7.order_index = 7
    botapp_projectstepmodel_7.action_type = 'clickAndWait'
    botapp_projectstepmodel_7.value = '1.0'
    botapp_projectstepmodel_7.html_query = '#row-dates-pax > div.col-passengers > div:nth-child(2) > div:nth-child(5) > div > div.value'
    botapp_projectstepmodel_7.variable = False
    botapp_projectstepmodel_7.project = botapp_projectmodel_1
    botapp_projectstepmodel_7 = importer.save_or_locate(botapp_projectstepmodel_7)

    botapp_projectstepmodel_8 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_8.display_name = '1 (+1) utas hozzáadása'
    botapp_projectstepmodel_8.order_index = 8
    botapp_projectstepmodel_8.action_type = 'clickAndWait'
    botapp_projectstepmodel_8.value = '1.0'
    botapp_projectstepmodel_8.html_query = '#row-dates-pax > div.col-passengers > div.popup-passenger-input.opened > div > div > div.content > popup-content > div:nth-child(6) > div > div.details-controls > core-inc-dec > button.core-btn.inc.core-btn-wrap'
    botapp_projectstepmodel_8.variable = False
    botapp_projectstepmodel_8.project = botapp_projectmodel_1
    botapp_projectstepmodel_8 = importer.save_or_locate(botapp_projectstepmodel_8)

    botapp_projectstepmodel_9 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_9.display_name = 'Indulási időpont kiválasztása'
    botapp_projectstepmodel_9.order_index = 9
    botapp_projectstepmodel_9.action_type = 'clickAndWait'
    botapp_projectstepmodel_9.value = '1.0'
    botapp_projectstepmodel_9.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required > div.focused > div'
    botapp_projectstepmodel_9.variable = False
    botapp_projectstepmodel_9.project = botapp_projectmodel_1
    botapp_projectstepmodel_9 = importer.save_or_locate(botapp_projectstepmodel_9)

    botapp_projectstepmodel_10 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_10.display_name = 'Visszaút kiválasztása'
    botapp_projectstepmodel_10.order_index = 10
    botapp_projectstepmodel_10.action_type = 'clickAndWait'
    botapp_projectstepmodel_10.value = '1.0'
    botapp_projectstepmodel_10.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.core-date-range.popup-start-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.six-rows.scrollable > ul > li:nth-child(1) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_10.variable = False
    botapp_projectstepmodel_10.project = botapp_projectmodel_1
    botapp_projectstepmodel_10 = importer.save_or_locate(botapp_projectstepmodel_10)

    botapp_projectstepmodel_11 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_11.display_name = 'Indulásra kattintás'
    botapp_projectstepmodel_11.order_index = 11
    botapp_projectstepmodel_11.action_type = 'clickAndWait'
    botapp_projectstepmodel_11.value = '1.0'
    botapp_projectstepmodel_11.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-to > div > div.core-date-range.popup-end-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.scrollable.six-rows > ul > li:nth-child(2) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_11.variable = False
    botapp_projectstepmodel_11.project = botapp_projectmodel_1
    botapp_projectstepmodel_11 = importer.save_or_locate(botapp_projectstepmodel_11)

    botapp_projectstepmodel_12 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_12.display_name = 'Oda "összegtől" gomb megnyomása'
    botapp_projectstepmodel_12.order_index = 12
    botapp_projectstepmodel_12.action_type = 'clickAndWait'
    botapp_projectstepmodel_12.value = '1.0'
    botapp_projectstepmodel_12.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-right > button:nth-child(2)'
    botapp_projectstepmodel_12.variable = False
    botapp_projectstepmodel_12.project = botapp_projectmodel_1
    botapp_projectstepmodel_12 = importer.save_or_locate(botapp_projectstepmodel_12)

    botapp_projectstepmodel_13 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_13.display_name = 'Oda normál viteldíj beállítása'
    botapp_projectstepmodel_13.order_index = 13
    botapp_projectstepmodel_13.action_type = 'clickAndWait'
    botapp_projectstepmodel_13.value = '1.0'
    botapp_projectstepmodel_13.html_query = '#flight-FR\x07e 8415\x07e \x10 \x07e \x07e BUD\x07e 09\x02f 09\x02f 2017\x10 20\x03a 20\x07e CRL\x07e 09\x02f 09\x02f 2017\x10 22\x03a 25\x07e > div > div.flight-header__min-price.hide-mobile'
    botapp_projectstepmodel_13.variable = False
    botapp_projectstepmodel_13.project = botapp_projectmodel_1
    botapp_projectstepmodel_13 = importer.save_or_locate(botapp_projectstepmodel_13)

    botapp_projectstepmodel_14 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_14.display_name = 'Vissza "összegtől" gomb megnyomása'
    botapp_projectstepmodel_14.order_index = 14
    botapp_projectstepmodel_14.action_type = 'clickAndWait'
    botapp_projectstepmodel_14.value = '1.0'
    botapp_projectstepmodel_14.html_query = '#flight-FR\x07e 8416\x07e \x10 \x07e \x07e CRL\x07e 10\x02f 14\x02f 2017\x10 17\x03a 55\x07e BUD\x07e 10\x02f 14\x02f 2017\x10 19\x03a 55\x07e > div > div.flight-header__min-price.hide-mobile > flights-table-price > div > div.core-btn-primary'
    botapp_projectstepmodel_14.variable = False
    botapp_projectstepmodel_14.project = botapp_projectmodel_1
    botapp_projectstepmodel_14 = importer.save_or_locate(botapp_projectstepmodel_14)

    botapp_projectstepmodel_15 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_15.display_name = 'Folytatás gombra kattintés'
    botapp_projectstepmodel_15.order_index = 15
    botapp_projectstepmodel_15.action_type = 'clickAndWait'
    botapp_projectstepmodel_15.value = '1.0'
    botapp_projectstepmodel_15.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-cnt > button'
    botapp_projectstepmodel_15.variable = False
    botapp_projectstepmodel_15.project = botapp_projectmodel_1
    botapp_projectstepmodel_15 = importer.save_or_locate(botapp_projectstepmodel_15)

    botapp_projectstepmodel_16 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_16.display_name = 'Csomag hozzáadása'
    botapp_projectstepmodel_16.order_index = 17
    botapp_projectstepmodel_16.action_type = 'clickAndWait'
    botapp_projectstepmodel_16.value = '1.0'
    botapp_projectstepmodel_16.html_query = 'body > div.FR > main > div.body-section > extras-panels > section > article > leaderboard > div > extras-card:nth-child(3) > ng-include > div > div.action > button.core-btn-primary.add'
    botapp_projectstepmodel_16.variable = False
    botapp_projectstepmodel_16.project = botapp_projectmodel_1
    botapp_projectstepmodel_16 = importer.save_or_locate(botapp_projectstepmodel_16)

    botapp_projectstepmodel_17 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_17.display_name = 'Csomag hozzáadása felugró'
    botapp_projectstepmodel_17.order_index = 18
    botapp_projectstepmodel_17.action_type = 'clickAndWait'
    botapp_projectstepmodel_17.value = '1.0'
    botapp_projectstepmodel_17.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div'
    botapp_projectstepmodel_17.variable = False
    botapp_projectstepmodel_17.project = botapp_projectmodel_1
    botapp_projectstepmodel_17 = importer.save_or_locate(botapp_projectstepmodel_17)

    # Processing model: botapp.models.StoreSelectedValueProjectStepModel

    from botapp.models import StoreSelectedValueProjectStepModel

    botapp_projectstepmodel_18 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_18.display_name = 'Összeg mentése'
    botapp_projectstepmodel_18.order_index = 16
    botapp_projectstepmodel_18.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_18.value = 'lowest_price'
    botapp_projectstepmodel_18.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-total > trips-breakdown > div.breakdown > div > div.price-number.notranslate.short-price'
    botapp_projectstepmodel_18.variable = True
    botapp_projectstepmodel_18.project = botapp_projectmodel_1
    botapp_projectstepmodel_18 = importer.save_or_locate(botapp_projectstepmodel_18)

    botapp_projectstepmodel_19 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_19.display_name = 'Kisebb csomag súly'
    botapp_projectstepmodel_19.order_index = 19
    botapp_projectstepmodel_19.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_19.value = 'lower_bag_weight'
    botapp_projectstepmodel_19.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(1) > span.bag-item__weight'
    botapp_projectstepmodel_19.variable = True
    botapp_projectstepmodel_19.project = botapp_projectmodel_1
    botapp_projectstepmodel_19 = importer.save_or_locate(botapp_projectstepmodel_19)

    botapp_projectstepmodel_20 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_20.display_name = 'Kisebb csomag ár'
    botapp_projectstepmodel_20.order_index = 20
    botapp_projectstepmodel_20.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_20.value = 'lower_bag_price'
    botapp_projectstepmodel_20.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_20.variable = True
    botapp_projectstepmodel_20.project = botapp_projectmodel_1
    botapp_projectstepmodel_20 = importer.save_or_locate(botapp_projectstepmodel_20)

    botapp_projectstepmodel_21 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_21.display_name = 'Nagyobb csomag súly'
    botapp_projectstepmodel_21.order_index = 21
    botapp_projectstepmodel_21.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_21.value = 'larger_bag_weight'
    botapp_projectstepmodel_21.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__weight'
    botapp_projectstepmodel_21.variable = True
    botapp_projectstepmodel_21.project = botapp_projectmodel_1
    botapp_projectstepmodel_21 = importer.save_or_locate(botapp_projectstepmodel_21)

    botapp_projectstepmodel_22 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_22.display_name = 'Nagyobb csomag ár'
    botapp_projectstepmodel_22.order_index = 22
    botapp_projectstepmodel_22.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_22.value = 'larger_bag_price'
    botapp_projectstepmodel_22.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_22.variable = True
    botapp_projectstepmodel_22.project = botapp_projectmodel_1
    botapp_projectstepmodel_22 = importer.save_or_locate(botapp_projectstepmodel_22)