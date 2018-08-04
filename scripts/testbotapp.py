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

    botapp_projectmodel_2 = ProjectModel()
    botapp_projectmodel_2.name = 'RyanAir Holidays'
    botapp_projectmodel_2.scrapy = 'portalcrawler'
    botapp_projectmodel_2.version = '3.13.54'
    botapp_projectmodel_2.spider = 'angular'
    botapp_projectmodel_2.portal_url = 'https://www.ryanair.com/hu/hu/'
    botapp_projectmodel_2 = importer.save_or_locate(botapp_projectmodel_2)

    # Processing model: botapp.models.ProjectStepModel

    from botapp.models import ProjectStepModel

    botapp_projectstepmodel_1 = ProjectStepModel()
    botapp_projectstepmodel_1.display_name = 'Indulási állomás felugró megnyitása'
    botapp_projectstepmodel_1.order_index = 1
    botapp_projectstepmodel_1.action_type = 'clickAndWait'
    botapp_projectstepmodel_1.value = '1.0'
    botapp_projectstepmodel_1.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_1.variable = False
    botapp_projectstepmodel_1.project = botapp_projectmodel_1
    botapp_projectstepmodel_1 = importer.save_or_locate(botapp_projectstepmodel_1)

    botapp_projectstepmodel_2 = ProjectStepModel()
    botapp_projectstepmodel_2.display_name = 'Indulási ország kiválasztása'
    botapp_projectstepmodel_2.order_index = 2
    botapp_projectstepmodel_2.action_type = 'clickAndWait'
    botapp_projectstepmodel_2.value = '1.0'
    botapp_projectstepmodel_2.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div.core-list-item.core-list-item-rounded.clicked'
    botapp_projectstepmodel_2.variable = False
    botapp_projectstepmodel_2.project = botapp_projectmodel_1
    botapp_projectstepmodel_2 = importer.save_or_locate(botapp_projectstepmodel_2)

    botapp_projectstepmodel_3 = ProjectStepModel()
    botapp_projectstepmodel_3.display_name = 'Indulási repülőtér kiválasztása'
    botapp_projectstepmodel_3.order_index = 3
    botapp_projectstepmodel_3.action_type = 'clickAndWait'
    botapp_projectstepmodel_3.value = '1.0'
    botapp_projectstepmodel_3.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div.core-list-item.core-list-item-rounded.clicked > span'
    botapp_projectstepmodel_3.variable = False
    botapp_projectstepmodel_3.project = botapp_projectmodel_1
    botapp_projectstepmodel_3 = importer.save_or_locate(botapp_projectstepmodel_3)

    botapp_projectstepmodel_4 = ProjectStepModel()
    botapp_projectstepmodel_4.display_name = 'Érkezési állomás felugró megnyitása'
    botapp_projectstepmodel_4.order_index = 4
    botapp_projectstepmodel_4.action_type = 'clickAndWait'
    botapp_projectstepmodel_4.value = '1.0'
    botapp_projectstepmodel_4.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_4.variable = False
    botapp_projectstepmodel_4.project = botapp_projectmodel_1
    botapp_projectstepmodel_4 = importer.save_or_locate(botapp_projectstepmodel_4)

    botapp_projectstepmodel_5 = ProjectStepModel()
    botapp_projectstepmodel_5.display_name = 'Érkezési ország kiválasztása'
    botapp_projectstepmodel_5.order_index = 5
    botapp_projectstepmodel_5.action_type = 'clickAndWait'
    botapp_projectstepmodel_5.value = '1.0'
    botapp_projectstepmodel_5.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div:nth-child(4)'
    botapp_projectstepmodel_5.variable = False
    botapp_projectstepmodel_5.project = botapp_projectmodel_1
    botapp_projectstepmodel_5 = importer.save_or_locate(botapp_projectstepmodel_5)

    botapp_projectstepmodel_6 = ProjectStepModel()
    botapp_projectstepmodel_6.display_name = 'Érkezési repülőtér kiválasztása'
    botapp_projectstepmodel_6.order_index = 6
    botapp_projectstepmodel_6.action_type = 'clickAndWait'
    botapp_projectstepmodel_6.value = '1.0'
    botapp_projectstepmodel_6.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div:nth-child(3) > span'
    botapp_projectstepmodel_6.variable = False
    botapp_projectstepmodel_6.project = botapp_projectmodel_1
    botapp_projectstepmodel_6 = importer.save_or_locate(botapp_projectstepmodel_6)

    botapp_projectstepmodel_7 = ProjectStepModel()
    botapp_projectstepmodel_7.display_name = 'Utasok felugró kiválasztása'
    botapp_projectstepmodel_7.order_index = 7
    botapp_projectstepmodel_7.action_type = 'clickAndWait'
    botapp_projectstepmodel_7.value = '1.0'
    botapp_projectstepmodel_7.html_query = '#row-dates-pax > div.col-passengers > div:nth-child(2) > div:nth-child(5) > div > div.value'
    botapp_projectstepmodel_7.variable = False
    botapp_projectstepmodel_7.project = botapp_projectmodel_1
    botapp_projectstepmodel_7 = importer.save_or_locate(botapp_projectstepmodel_7)

    botapp_projectstepmodel_8 = ProjectStepModel()
    botapp_projectstepmodel_8.display_name = '1 (+1) utas hozzáadása'
    botapp_projectstepmodel_8.order_index = 8
    botapp_projectstepmodel_8.action_type = 'clickAndWait'
    botapp_projectstepmodel_8.value = '1.0'
    botapp_projectstepmodel_8.html_query = '#row-dates-pax > div.col-passengers > div.popup-passenger-input.opened > div > div > div.content > popup-content > div:nth-child(6) > div > div.details-controls > core-inc-dec > button.core-btn.inc.core-btn-wrap'
    botapp_projectstepmodel_8.variable = False
    botapp_projectstepmodel_8.project = botapp_projectmodel_1
    botapp_projectstepmodel_8 = importer.save_or_locate(botapp_projectstepmodel_8)

    botapp_projectstepmodel_9 = ProjectStepModel()
    botapp_projectstepmodel_9.display_name = 'Indulási időpont kiválasztása'
    botapp_projectstepmodel_9.order_index = 9
    botapp_projectstepmodel_9.action_type = 'clickAndWait'
    botapp_projectstepmodel_9.value = '1.0'
    botapp_projectstepmodel_9.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required > div.focused > div'
    botapp_projectstepmodel_9.variable = False
    botapp_projectstepmodel_9.project = botapp_projectmodel_1
    botapp_projectstepmodel_9 = importer.save_or_locate(botapp_projectstepmodel_9)

    botapp_projectstepmodel_10 = ProjectStepModel()
    botapp_projectstepmodel_10.display_name = 'Visszaút kiválasztása'
    botapp_projectstepmodel_10.order_index = 10
    botapp_projectstepmodel_10.action_type = 'clickAndWait'
    botapp_projectstepmodel_10.value = '1.0'
    botapp_projectstepmodel_10.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.core-date-range.popup-start-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.six-rows.scrollable > ul > li:nth-child(1) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_10.variable = False
    botapp_projectstepmodel_10.project = botapp_projectmodel_1
    botapp_projectstepmodel_10 = importer.save_or_locate(botapp_projectstepmodel_10)

    botapp_projectstepmodel_11 = ProjectStepModel()
    botapp_projectstepmodel_11.display_name = 'Indulásra kattintás'
    botapp_projectstepmodel_11.order_index = 11
    botapp_projectstepmodel_11.action_type = 'clickAndWait'
    botapp_projectstepmodel_11.value = '1.0'
    botapp_projectstepmodel_11.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-to > div > div.core-date-range.popup-end-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.scrollable.six-rows > ul > li:nth-child(2) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_11.variable = False
    botapp_projectstepmodel_11.project = botapp_projectmodel_1
    botapp_projectstepmodel_11 = importer.save_or_locate(botapp_projectstepmodel_11)

    botapp_projectstepmodel_12 = ProjectStepModel()
    botapp_projectstepmodel_12.display_name = 'Oda "összegtől" gomb megnyomása'
    botapp_projectstepmodel_12.order_index = 12
    botapp_projectstepmodel_12.action_type = 'clickAndWait'
    botapp_projectstepmodel_12.value = '1.0'
    botapp_projectstepmodel_12.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-right > button:nth-child(2)'
    botapp_projectstepmodel_12.variable = False
    botapp_projectstepmodel_12.project = botapp_projectmodel_1
    botapp_projectstepmodel_12 = importer.save_or_locate(botapp_projectstepmodel_12)

    botapp_projectstepmodel_13 = ProjectStepModel()
    botapp_projectstepmodel_13.display_name = 'Oda normál viteldíj beállítása'
    botapp_projectstepmodel_13.order_index = 13
    botapp_projectstepmodel_13.action_type = 'clickAndWait'
    botapp_projectstepmodel_13.value = '1.0'
    botapp_projectstepmodel_13.html_query = '#flight-FR\x07e 8415\x07e \x10 \x07e \x07e BUD\x07e 09\x02f 09\x02f 2017\x10 20\x03a 20\x07e CRL\x07e 09\x02f 09\x02f 2017\x10 22\x03a 25\x07e > div > div.flight-header__min-price.hide-mobile'
    botapp_projectstepmodel_13.variable = False
    botapp_projectstepmodel_13.project = botapp_projectmodel_1
    botapp_projectstepmodel_13 = importer.save_or_locate(botapp_projectstepmodel_13)

    botapp_projectstepmodel_14 = ProjectStepModel()
    botapp_projectstepmodel_14.display_name = 'Vissza "összegtől" gomb megnyomása'
    botapp_projectstepmodel_14.order_index = 14
    botapp_projectstepmodel_14.action_type = 'clickAndWait'
    botapp_projectstepmodel_14.value = '1.0'
    botapp_projectstepmodel_14.html_query = '#flight-FR\x07e 8416\x07e \x10 \x07e \x07e CRL\x07e 10\x02f 14\x02f 2017\x10 17\x03a 55\x07e BUD\x07e 10\x02f 14\x02f 2017\x10 19\x03a 55\x07e > div > div.flight-header__min-price.hide-mobile > flights-table-price > div > div.core-btn-primary'
    botapp_projectstepmodel_14.variable = False
    botapp_projectstepmodel_14.project = botapp_projectmodel_1
    botapp_projectstepmodel_14 = importer.save_or_locate(botapp_projectstepmodel_14)

    botapp_projectstepmodel_15 = ProjectStepModel()
    botapp_projectstepmodel_15.display_name = 'Folytatás gombra kattintés'
    botapp_projectstepmodel_15.order_index = 15
    botapp_projectstepmodel_15.action_type = 'clickAndWait'
    botapp_projectstepmodel_15.value = '1.0'
    botapp_projectstepmodel_15.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-cnt > button'
    botapp_projectstepmodel_15.variable = False
    botapp_projectstepmodel_15.project = botapp_projectmodel_1
    botapp_projectstepmodel_15 = importer.save_or_locate(botapp_projectstepmodel_15)

    botapp_projectstepmodel_16 = ProjectStepModel()
    botapp_projectstepmodel_16.display_name = 'Csomag hozzáadása'
    botapp_projectstepmodel_16.order_index = 17
    botapp_projectstepmodel_16.action_type = 'clickAndWait'
    botapp_projectstepmodel_16.value = '1.0'
    botapp_projectstepmodel_16.html_query = 'body > div.FR > main > div.body-section > extras-panels > section > article > leaderboard > div > extras-card:nth-child(3) > ng-include > div > div.action > button.core-btn-primary.add'
    botapp_projectstepmodel_16.variable = False
    botapp_projectstepmodel_16.project = botapp_projectmodel_1
    botapp_projectstepmodel_16 = importer.save_or_locate(botapp_projectstepmodel_16)

    botapp_projectstepmodel_17 = ProjectStepModel()
    botapp_projectstepmodel_17.display_name = 'Csomag hozzáadása felugró'
    botapp_projectstepmodel_17.order_index = 18
    botapp_projectstepmodel_17.action_type = 'clickAndWait'
    botapp_projectstepmodel_17.value = '1.0'
    botapp_projectstepmodel_17.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div'
    botapp_projectstepmodel_17.variable = False
    botapp_projectstepmodel_17.project = botapp_projectmodel_1
    botapp_projectstepmodel_17 = importer.save_or_locate(botapp_projectstepmodel_17)

    botapp_projectstepmodel_18 = ProjectStepModel()
    botapp_projectstepmodel_18.display_name = 'Összeg mentése'
    botapp_projectstepmodel_18.order_index = 16
    botapp_projectstepmodel_18.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_18.value = 'lowest_price'
    botapp_projectstepmodel_18.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-total > trips-breakdown > div.breakdown > div > div.price-number.notranslate.short-price'
    botapp_projectstepmodel_18.variable = True
    botapp_projectstepmodel_18.project = botapp_projectmodel_1
    botapp_projectstepmodel_18 = importer.save_or_locate(botapp_projectstepmodel_18)

    botapp_projectstepmodel_19 = ProjectStepModel()
    botapp_projectstepmodel_19.display_name = 'Kisebb csomag súly'
    botapp_projectstepmodel_19.order_index = 19
    botapp_projectstepmodel_19.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_19.value = 'lower_bag_weight'
    botapp_projectstepmodel_19.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(1) > span.bag-item__weight'
    botapp_projectstepmodel_19.variable = True
    botapp_projectstepmodel_19.project = botapp_projectmodel_1
    botapp_projectstepmodel_19 = importer.save_or_locate(botapp_projectstepmodel_19)

    botapp_projectstepmodel_20 = ProjectStepModel()
    botapp_projectstepmodel_20.display_name = 'Kisebb csomag ár'
    botapp_projectstepmodel_20.order_index = 20
    botapp_projectstepmodel_20.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_20.value = 'lower_bag_price'
    botapp_projectstepmodel_20.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_20.variable = True
    botapp_projectstepmodel_20.project = botapp_projectmodel_1
    botapp_projectstepmodel_20 = importer.save_or_locate(botapp_projectstepmodel_20)

    botapp_projectstepmodel_21 = ProjectStepModel()
    botapp_projectstepmodel_21.display_name = 'Nagyobb csomag súly'
    botapp_projectstepmodel_21.order_index = 21
    botapp_projectstepmodel_21.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_21.value = 'larger_bag_weight'
    botapp_projectstepmodel_21.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__weight'
    botapp_projectstepmodel_21.variable = True
    botapp_projectstepmodel_21.project = botapp_projectmodel_1
    botapp_projectstepmodel_21 = importer.save_or_locate(botapp_projectstepmodel_21)

    botapp_projectstepmodel_22 = ProjectStepModel()
    botapp_projectstepmodel_22.display_name = 'Nagyobb csomag ár'
    botapp_projectstepmodel_22.order_index = 22
    botapp_projectstepmodel_22.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_22.value = 'larger_bag_price'
    botapp_projectstepmodel_22.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_22.variable = True
    botapp_projectstepmodel_22.project = botapp_projectmodel_1
    botapp_projectstepmodel_22 = importer.save_or_locate(botapp_projectstepmodel_22)

    botapp_projectstepmodel_23 = ProjectStepModel()
    botapp_projectstepmodel_23.display_name = 'Indulási állomás felugró megnyitása'
    botapp_projectstepmodel_23.order_index = 1
    botapp_projectstepmodel_23.action_type = 'clickAndWait'
    botapp_projectstepmodel_23.value = '1.0'
    botapp_projectstepmodel_23.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_23.variable = False
    botapp_projectstepmodel_23.project = botapp_projectmodel_2
    botapp_projectstepmodel_23 = importer.save_or_locate(botapp_projectstepmodel_23)

    botapp_projectstepmodel_24 = ProjectStepModel()
    botapp_projectstepmodel_24.display_name = 'Indulási ország kiválasztása'
    botapp_projectstepmodel_24.order_index = 2
    botapp_projectstepmodel_24.action_type = 'clickAndWait'
    botapp_projectstepmodel_24.value = '1.0'
    botapp_projectstepmodel_24.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div.core-list-item.core-list-item-rounded.clicked'
    botapp_projectstepmodel_24.variable = False
    botapp_projectstepmodel_24.project = botapp_projectmodel_2
    botapp_projectstepmodel_24 = importer.save_or_locate(botapp_projectstepmodel_24)

    botapp_projectstepmodel_25 = ProjectStepModel()
    botapp_projectstepmodel_25.display_name = 'Indulási repülőtér kiválasztása'
    botapp_projectstepmodel_25.order_index = 3
    botapp_projectstepmodel_25.action_type = 'clickAndWait'
    botapp_projectstepmodel_25.value = '1.0'
    botapp_projectstepmodel_25.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div.core-list-item.core-list-item-rounded.clicked > span'
    botapp_projectstepmodel_25.variable = False
    botapp_projectstepmodel_25.project = botapp_projectmodel_2
    botapp_projectstepmodel_25 = importer.save_or_locate(botapp_projectstepmodel_25)

    botapp_projectstepmodel_26 = ProjectStepModel()
    botapp_projectstepmodel_26.display_name = 'Érkezési állomás felugró megnyitása'
    botapp_projectstepmodel_26.order_index = 4
    botapp_projectstepmodel_26.action_type = 'clickAndWait'
    botapp_projectstepmodel_26.value = '1.0'
    botapp_projectstepmodel_26.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_26.variable = False
    botapp_projectstepmodel_26.project = botapp_projectmodel_2
    botapp_projectstepmodel_26 = importer.save_or_locate(botapp_projectstepmodel_26)

    botapp_projectstepmodel_27 = ProjectStepModel()
    botapp_projectstepmodel_27.display_name = 'Érkezési ország kiválasztása'
    botapp_projectstepmodel_27.order_index = 5
    botapp_projectstepmodel_27.action_type = 'clickAndWait'
    botapp_projectstepmodel_27.value = '1.0'
    botapp_projectstepmodel_27.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div:nth-child(4)'
    botapp_projectstepmodel_27.variable = False
    botapp_projectstepmodel_27.project = botapp_projectmodel_2
    botapp_projectstepmodel_27 = importer.save_or_locate(botapp_projectstepmodel_27)

    botapp_projectstepmodel_28 = ProjectStepModel()
    botapp_projectstepmodel_28.display_name = 'Érkezési repülőtér kiválasztása'
    botapp_projectstepmodel_28.order_index = 6
    botapp_projectstepmodel_28.action_type = 'clickAndWait'
    botapp_projectstepmodel_28.value = '1.0'
    botapp_projectstepmodel_28.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div:nth-child(3) > span'
    botapp_projectstepmodel_28.variable = False
    botapp_projectstepmodel_28.project = botapp_projectmodel_2
    botapp_projectstepmodel_28 = importer.save_or_locate(botapp_projectstepmodel_28)

    botapp_projectstepmodel_29 = ProjectStepModel()
    botapp_projectstepmodel_29.display_name = 'Utasok felugró kiválasztása'
    botapp_projectstepmodel_29.order_index = 7
    botapp_projectstepmodel_29.action_type = 'clickAndWait'
    botapp_projectstepmodel_29.value = '1.0'
    botapp_projectstepmodel_29.html_query = '#row-dates-pax > div.col-passengers > div:nth-child(2) > div:nth-child(5) > div > div.value'
    botapp_projectstepmodel_29.variable = False
    botapp_projectstepmodel_29.project = botapp_projectmodel_2
    botapp_projectstepmodel_29 = importer.save_or_locate(botapp_projectstepmodel_29)

    botapp_projectstepmodel_30 = ProjectStepModel()
    botapp_projectstepmodel_30.display_name = '1 (+1) utas hozzáadása'
    botapp_projectstepmodel_30.order_index = 8
    botapp_projectstepmodel_30.action_type = 'clickAndWait'
    botapp_projectstepmodel_30.value = '1.0'
    botapp_projectstepmodel_30.html_query = '#row-dates-pax > div.col-passengers > div.popup-passenger-input.opened > div > div > div.content > popup-content > div:nth-child(6) > div > div.details-controls > core-inc-dec > button.core-btn.inc.core-btn-wrap'
    botapp_projectstepmodel_30.variable = False
    botapp_projectstepmodel_30.project = botapp_projectmodel_2
    botapp_projectstepmodel_30 = importer.save_or_locate(botapp_projectstepmodel_30)

    botapp_projectstepmodel_31 = ProjectStepModel()
    botapp_projectstepmodel_31.display_name = 'Indulási időpont kiválasztása'
    botapp_projectstepmodel_31.order_index = 9
    botapp_projectstepmodel_31.action_type = 'clickAndWait'
    botapp_projectstepmodel_31.value = '1.0'
    botapp_projectstepmodel_31.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required > div.focused > div'
    botapp_projectstepmodel_31.variable = False
    botapp_projectstepmodel_31.project = botapp_projectmodel_2
    botapp_projectstepmodel_31 = importer.save_or_locate(botapp_projectstepmodel_31)

    botapp_projectstepmodel_32 = ProjectStepModel()
    botapp_projectstepmodel_32.display_name = 'Visszaút kiválasztása'
    botapp_projectstepmodel_32.order_index = 10
    botapp_projectstepmodel_32.action_type = 'clickAndWait'
    botapp_projectstepmodel_32.value = '1.0'
    botapp_projectstepmodel_32.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.core-date-range.popup-start-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.six-rows.scrollable > ul > li:nth-child(1) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_32.variable = False
    botapp_projectstepmodel_32.project = botapp_projectmodel_2
    botapp_projectstepmodel_32 = importer.save_or_locate(botapp_projectstepmodel_32)

    botapp_projectstepmodel_33 = ProjectStepModel()
    botapp_projectstepmodel_33.display_name = 'Indulásra kattintás'
    botapp_projectstepmodel_33.order_index = 11
    botapp_projectstepmodel_33.action_type = 'clickAndWait'
    botapp_projectstepmodel_33.value = '1.0'
    botapp_projectstepmodel_33.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-to > div > div.core-date-range.popup-end-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.scrollable.six-rows > ul > li:nth-child(2) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_33.variable = False
    botapp_projectstepmodel_33.project = botapp_projectmodel_2
    botapp_projectstepmodel_33 = importer.save_or_locate(botapp_projectstepmodel_33)

    botapp_projectstepmodel_34 = ProjectStepModel()
    botapp_projectstepmodel_34.display_name = 'Oda "összegtől" gomb megnyomása'
    botapp_projectstepmodel_34.order_index = 12
    botapp_projectstepmodel_34.action_type = 'clickAndWait'
    botapp_projectstepmodel_34.value = '1.0'
    botapp_projectstepmodel_34.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-right > button:nth-child(2)'
    botapp_projectstepmodel_34.variable = False
    botapp_projectstepmodel_34.project = botapp_projectmodel_2
    botapp_projectstepmodel_34 = importer.save_or_locate(botapp_projectstepmodel_34)

    botapp_projectstepmodel_35 = ProjectStepModel()
    botapp_projectstepmodel_35.display_name = 'Oda normál viteldíj beállítása'
    botapp_projectstepmodel_35.order_index = 13
    botapp_projectstepmodel_35.action_type = 'clickAndWait'
    botapp_projectstepmodel_35.value = '1.0'
    botapp_projectstepmodel_35.html_query = '#flight-FR\x07e 8415\x07e \x10 \x07e \x07e BUD\x07e 09\x02f 09\x02f 2017\x10 20\x03a 20\x07e CRL\x07e 09\x02f 09\x02f 2017\x10 22\x03a 25\x07e > div > div.flight-header__min-price.hide-mobile'
    botapp_projectstepmodel_35.variable = False
    botapp_projectstepmodel_35.project = botapp_projectmodel_2
    botapp_projectstepmodel_35 = importer.save_or_locate(botapp_projectstepmodel_35)

    botapp_projectstepmodel_36 = ProjectStepModel()
    botapp_projectstepmodel_36.display_name = 'Vissza "összegtől" gomb megnyomása'
    botapp_projectstepmodel_36.order_index = 14
    botapp_projectstepmodel_36.action_type = 'clickAndWait'
    botapp_projectstepmodel_36.value = '1.0'
    botapp_projectstepmodel_36.html_query = '#flight-FR\x07e 8416\x07e \x10 \x07e \x07e CRL\x07e 10\x02f 14\x02f 2017\x10 17\x03a 55\x07e BUD\x07e 10\x02f 14\x02f 2017\x10 19\x03a 55\x07e > div > div.flight-header__min-price.hide-mobile > flights-table-price > div > div.core-btn-primary'
    botapp_projectstepmodel_36.variable = False
    botapp_projectstepmodel_36.project = botapp_projectmodel_2
    botapp_projectstepmodel_36 = importer.save_or_locate(botapp_projectstepmodel_36)

    botapp_projectstepmodel_37 = ProjectStepModel()
    botapp_projectstepmodel_37.display_name = 'Folytatás gombra kattintés'
    botapp_projectstepmodel_37.order_index = 15
    botapp_projectstepmodel_37.action_type = 'clickAndWait'
    botapp_projectstepmodel_37.value = '1.0'
    botapp_projectstepmodel_37.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-cnt > button'
    botapp_projectstepmodel_37.variable = False
    botapp_projectstepmodel_37.project = botapp_projectmodel_2
    botapp_projectstepmodel_37 = importer.save_or_locate(botapp_projectstepmodel_37)

    botapp_projectstepmodel_38 = ProjectStepModel()
    botapp_projectstepmodel_38.display_name = 'Csomag hozzáadása'
    botapp_projectstepmodel_38.order_index = 17
    botapp_projectstepmodel_38.action_type = 'clickAndWait'
    botapp_projectstepmodel_38.value = '1.0'
    botapp_projectstepmodel_38.html_query = 'body > div.FR > main > div.body-section > extras-panels > section > article > leaderboard > div > extras-card:nth-child(3) > ng-include > div > div.action > button.core-btn-primary.add'
    botapp_projectstepmodel_38.variable = False
    botapp_projectstepmodel_38.project = botapp_projectmodel_2
    botapp_projectstepmodel_38 = importer.save_or_locate(botapp_projectstepmodel_38)

    botapp_projectstepmodel_39 = ProjectStepModel()
    botapp_projectstepmodel_39.display_name = 'Csomag hozzáadása felugró'
    botapp_projectstepmodel_39.order_index = 18
    botapp_projectstepmodel_39.action_type = 'clickAndWait'
    botapp_projectstepmodel_39.value = '1.0'
    botapp_projectstepmodel_39.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div'
    botapp_projectstepmodel_39.variable = False
    botapp_projectstepmodel_39.project = botapp_projectmodel_2
    botapp_projectstepmodel_39 = importer.save_or_locate(botapp_projectstepmodel_39)

    botapp_projectstepmodel_40 = ProjectStepModel()
    botapp_projectstepmodel_40.display_name = 'Összeg mentése'
    botapp_projectstepmodel_40.order_index = 16
    botapp_projectstepmodel_40.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_40.value = 'lowest_price'
    botapp_projectstepmodel_40.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-total > trips-breakdown > div.breakdown > div > div.price-number.notranslate.short-price'
    botapp_projectstepmodel_40.variable = True
    botapp_projectstepmodel_40.project = botapp_projectmodel_2
    botapp_projectstepmodel_40 = importer.save_or_locate(botapp_projectstepmodel_40)

    botapp_projectstepmodel_41 = ProjectStepModel()
    botapp_projectstepmodel_41.display_name = 'Kisebb csomag súly'
    botapp_projectstepmodel_41.order_index = 19
    botapp_projectstepmodel_41.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_41.value = 'lower_bag_weight'
    botapp_projectstepmodel_41.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(1) > span.bag-item__weight'
    botapp_projectstepmodel_41.variable = True
    botapp_projectstepmodel_41.project = botapp_projectmodel_2
    botapp_projectstepmodel_41 = importer.save_or_locate(botapp_projectstepmodel_41)

    botapp_projectstepmodel_42 = ProjectStepModel()
    botapp_projectstepmodel_42.display_name = 'Kisebb csomag ár'
    botapp_projectstepmodel_42.order_index = 20
    botapp_projectstepmodel_42.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_42.value = 'lower_bag_price'
    botapp_projectstepmodel_42.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_42.variable = True
    botapp_projectstepmodel_42.project = botapp_projectmodel_2
    botapp_projectstepmodel_42 = importer.save_or_locate(botapp_projectstepmodel_42)

    botapp_projectstepmodel_43 = ProjectStepModel()
    botapp_projectstepmodel_43.display_name = 'Nagyobb csomag súly'
    botapp_projectstepmodel_43.order_index = 21
    botapp_projectstepmodel_43.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_43.value = 'larger_bag_weight'
    botapp_projectstepmodel_43.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__weight'
    botapp_projectstepmodel_43.variable = True
    botapp_projectstepmodel_43.project = botapp_projectmodel_2
    botapp_projectstepmodel_43 = importer.save_or_locate(botapp_projectstepmodel_43)

    botapp_projectstepmodel_44 = ProjectStepModel()
    botapp_projectstepmodel_44.display_name = 'Nagyobb csomag ár'
    botapp_projectstepmodel_44.order_index = 22
    botapp_projectstepmodel_44.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_44.value = 'larger_bag_price'
    botapp_projectstepmodel_44.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_44.variable = True
    botapp_projectstepmodel_44.project = botapp_projectmodel_2
    botapp_projectstepmodel_44 = importer.save_or_locate(botapp_projectstepmodel_44)

    # Processing model: botapp.models.ClickProjectStepModel

    from botapp.models import ClickProjectStepModel

    botapp_projectstepmodel_1 = ClickProjectStepModel()
    botapp_projectstepmodel_1.display_name = 'Indulási állomás felugró megnyitása'
    botapp_projectstepmodel_1.order_index = 1
    botapp_projectstepmodel_1.action_type = 'clickAndWait'
    botapp_projectstepmodel_1.value = '1.0'
    botapp_projectstepmodel_1.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_1.variable = False
    botapp_projectstepmodel_1.project = botapp_projectmodel_1
    botapp_projectstepmodel_1 = importer.save_or_locate(botapp_projectstepmodel_1)

    botapp_projectstepmodel_2 = ClickProjectStepModel()
    botapp_projectstepmodel_2.display_name = 'Indulási ország kiválasztása'
    botapp_projectstepmodel_2.order_index = 2
    botapp_projectstepmodel_2.action_type = 'clickAndWait'
    botapp_projectstepmodel_2.value = '1.0'
    botapp_projectstepmodel_2.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div.core-list-item.core-list-item-rounded.clicked'
    botapp_projectstepmodel_2.variable = False
    botapp_projectstepmodel_2.project = botapp_projectmodel_1
    botapp_projectstepmodel_2 = importer.save_or_locate(botapp_projectstepmodel_2)

    botapp_projectstepmodel_3 = ClickProjectStepModel()
    botapp_projectstepmodel_3.display_name = 'Indulási repülőtér kiválasztása'
    botapp_projectstepmodel_3.order_index = 3
    botapp_projectstepmodel_3.action_type = 'clickAndWait'
    botapp_projectstepmodel_3.value = '1.0'
    botapp_projectstepmodel_3.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div.core-list-item.core-list-item-rounded.clicked > span'
    botapp_projectstepmodel_3.variable = False
    botapp_projectstepmodel_3.project = botapp_projectmodel_1
    botapp_projectstepmodel_3 = importer.save_or_locate(botapp_projectstepmodel_3)

    botapp_projectstepmodel_4 = ClickProjectStepModel()
    botapp_projectstepmodel_4.display_name = 'Érkezési állomás felugró megnyitása'
    botapp_projectstepmodel_4.order_index = 4
    botapp_projectstepmodel_4.action_type = 'clickAndWait'
    botapp_projectstepmodel_4.value = '1.0'
    botapp_projectstepmodel_4.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_4.variable = False
    botapp_projectstepmodel_4.project = botapp_projectmodel_1
    botapp_projectstepmodel_4 = importer.save_or_locate(botapp_projectstepmodel_4)

    botapp_projectstepmodel_5 = ClickProjectStepModel()
    botapp_projectstepmodel_5.display_name = 'Érkezési ország kiválasztása'
    botapp_projectstepmodel_5.order_index = 5
    botapp_projectstepmodel_5.action_type = 'clickAndWait'
    botapp_projectstepmodel_5.value = '1.0'
    botapp_projectstepmodel_5.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div:nth-child(4)'
    botapp_projectstepmodel_5.variable = False
    botapp_projectstepmodel_5.project = botapp_projectmodel_1
    botapp_projectstepmodel_5 = importer.save_or_locate(botapp_projectstepmodel_5)

    botapp_projectstepmodel_6 = ClickProjectStepModel()
    botapp_projectstepmodel_6.display_name = 'Érkezési repülőtér kiválasztása'
    botapp_projectstepmodel_6.order_index = 6
    botapp_projectstepmodel_6.action_type = 'clickAndWait'
    botapp_projectstepmodel_6.value = '1.0'
    botapp_projectstepmodel_6.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div:nth-child(3) > span'
    botapp_projectstepmodel_6.variable = False
    botapp_projectstepmodel_6.project = botapp_projectmodel_1
    botapp_projectstepmodel_6 = importer.save_or_locate(botapp_projectstepmodel_6)

    botapp_projectstepmodel_7 = ClickProjectStepModel()
    botapp_projectstepmodel_7.display_name = 'Utasok felugró kiválasztása'
    botapp_projectstepmodel_7.order_index = 7
    botapp_projectstepmodel_7.action_type = 'clickAndWait'
    botapp_projectstepmodel_7.value = '1.0'
    botapp_projectstepmodel_7.html_query = '#row-dates-pax > div.col-passengers > div:nth-child(2) > div:nth-child(5) > div > div.value'
    botapp_projectstepmodel_7.variable = False
    botapp_projectstepmodel_7.project = botapp_projectmodel_1
    botapp_projectstepmodel_7 = importer.save_or_locate(botapp_projectstepmodel_7)

    botapp_projectstepmodel_8 = ClickProjectStepModel()
    botapp_projectstepmodel_8.display_name = '1 (+1) utas hozzáadása'
    botapp_projectstepmodel_8.order_index = 8
    botapp_projectstepmodel_8.action_type = 'clickAndWait'
    botapp_projectstepmodel_8.value = '1.0'
    botapp_projectstepmodel_8.html_query = '#row-dates-pax > div.col-passengers > div.popup-passenger-input.opened > div > div > div.content > popup-content > div:nth-child(6) > div > div.details-controls > core-inc-dec > button.core-btn.inc.core-btn-wrap'
    botapp_projectstepmodel_8.variable = False
    botapp_projectstepmodel_8.project = botapp_projectmodel_1
    botapp_projectstepmodel_8 = importer.save_or_locate(botapp_projectstepmodel_8)

    botapp_projectstepmodel_9 = ClickProjectStepModel()
    botapp_projectstepmodel_9.display_name = 'Indulási időpont kiválasztása'
    botapp_projectstepmodel_9.order_index = 9
    botapp_projectstepmodel_9.action_type = 'clickAndWait'
    botapp_projectstepmodel_9.value = '1.0'
    botapp_projectstepmodel_9.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required > div.focused > div'
    botapp_projectstepmodel_9.variable = False
    botapp_projectstepmodel_9.project = botapp_projectmodel_1
    botapp_projectstepmodel_9 = importer.save_or_locate(botapp_projectstepmodel_9)

    botapp_projectstepmodel_10 = ClickProjectStepModel()
    botapp_projectstepmodel_10.display_name = 'Visszaút kiválasztása'
    botapp_projectstepmodel_10.order_index = 10
    botapp_projectstepmodel_10.action_type = 'clickAndWait'
    botapp_projectstepmodel_10.value = '1.0'
    botapp_projectstepmodel_10.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.core-date-range.popup-start-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.six-rows.scrollable > ul > li:nth-child(1) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_10.variable = False
    botapp_projectstepmodel_10.project = botapp_projectmodel_1
    botapp_projectstepmodel_10 = importer.save_or_locate(botapp_projectstepmodel_10)

    botapp_projectstepmodel_11 = ClickProjectStepModel()
    botapp_projectstepmodel_11.display_name = 'Indulásra kattintás'
    botapp_projectstepmodel_11.order_index = 11
    botapp_projectstepmodel_11.action_type = 'clickAndWait'
    botapp_projectstepmodel_11.value = '1.0'
    botapp_projectstepmodel_11.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-to > div > div.core-date-range.popup-end-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.scrollable.six-rows > ul > li:nth-child(2) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_11.variable = False
    botapp_projectstepmodel_11.project = botapp_projectmodel_1
    botapp_projectstepmodel_11 = importer.save_or_locate(botapp_projectstepmodel_11)

    botapp_projectstepmodel_12 = ClickProjectStepModel()
    botapp_projectstepmodel_12.display_name = 'Oda "összegtől" gomb megnyomása'
    botapp_projectstepmodel_12.order_index = 12
    botapp_projectstepmodel_12.action_type = 'clickAndWait'
    botapp_projectstepmodel_12.value = '1.0'
    botapp_projectstepmodel_12.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-right > button:nth-child(2)'
    botapp_projectstepmodel_12.variable = False
    botapp_projectstepmodel_12.project = botapp_projectmodel_1
    botapp_projectstepmodel_12 = importer.save_or_locate(botapp_projectstepmodel_12)

    botapp_projectstepmodel_13 = ClickProjectStepModel()
    botapp_projectstepmodel_13.display_name = 'Oda normál viteldíj beállítása'
    botapp_projectstepmodel_13.order_index = 13
    botapp_projectstepmodel_13.action_type = 'clickAndWait'
    botapp_projectstepmodel_13.value = '1.0'
    botapp_projectstepmodel_13.html_query = '#flight-FR\x07e 8415\x07e \x10 \x07e \x07e BUD\x07e 09\x02f 09\x02f 2017\x10 20\x03a 20\x07e CRL\x07e 09\x02f 09\x02f 2017\x10 22\x03a 25\x07e > div > div.flight-header__min-price.hide-mobile'
    botapp_projectstepmodel_13.variable = False
    botapp_projectstepmodel_13.project = botapp_projectmodel_1
    botapp_projectstepmodel_13 = importer.save_or_locate(botapp_projectstepmodel_13)

    botapp_projectstepmodel_14 = ClickProjectStepModel()
    botapp_projectstepmodel_14.display_name = 'Vissza "összegtől" gomb megnyomása'
    botapp_projectstepmodel_14.order_index = 14
    botapp_projectstepmodel_14.action_type = 'clickAndWait'
    botapp_projectstepmodel_14.value = '1.0'
    botapp_projectstepmodel_14.html_query = '#flight-FR\x07e 8416\x07e \x10 \x07e \x07e CRL\x07e 10\x02f 14\x02f 2017\x10 17\x03a 55\x07e BUD\x07e 10\x02f 14\x02f 2017\x10 19\x03a 55\x07e > div > div.flight-header__min-price.hide-mobile > flights-table-price > div > div.core-btn-primary'
    botapp_projectstepmodel_14.variable = False
    botapp_projectstepmodel_14.project = botapp_projectmodel_1
    botapp_projectstepmodel_14 = importer.save_or_locate(botapp_projectstepmodel_14)

    botapp_projectstepmodel_15 = ClickProjectStepModel()
    botapp_projectstepmodel_15.display_name = 'Folytatás gombra kattintés'
    botapp_projectstepmodel_15.order_index = 15
    botapp_projectstepmodel_15.action_type = 'clickAndWait'
    botapp_projectstepmodel_15.value = '1.0'
    botapp_projectstepmodel_15.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-cnt > button'
    botapp_projectstepmodel_15.variable = False
    botapp_projectstepmodel_15.project = botapp_projectmodel_1
    botapp_projectstepmodel_15 = importer.save_or_locate(botapp_projectstepmodel_15)

    botapp_projectstepmodel_16 = ClickProjectStepModel()
    botapp_projectstepmodel_16.display_name = 'Csomag hozzáadása'
    botapp_projectstepmodel_16.order_index = 17
    botapp_projectstepmodel_16.action_type = 'clickAndWait'
    botapp_projectstepmodel_16.value = '1.0'
    botapp_projectstepmodel_16.html_query = 'body > div.FR > main > div.body-section > extras-panels > section > article > leaderboard > div > extras-card:nth-child(3) > ng-include > div > div.action > button.core-btn-primary.add'
    botapp_projectstepmodel_16.variable = False
    botapp_projectstepmodel_16.project = botapp_projectmodel_1
    botapp_projectstepmodel_16 = importer.save_or_locate(botapp_projectstepmodel_16)

    botapp_projectstepmodel_17 = ClickProjectStepModel()
    botapp_projectstepmodel_17.display_name = 'Csomag hozzáadása felugró'
    botapp_projectstepmodel_17.order_index = 18
    botapp_projectstepmodel_17.action_type = 'clickAndWait'
    botapp_projectstepmodel_17.value = '1.0'
    botapp_projectstepmodel_17.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div'
    botapp_projectstepmodel_17.variable = False
    botapp_projectstepmodel_17.project = botapp_projectmodel_1
    botapp_projectstepmodel_17 = importer.save_or_locate(botapp_projectstepmodel_17)

    botapp_projectstepmodel_18 = ClickProjectStepModel()
    botapp_projectstepmodel_18.display_name = 'Összeg mentése'
    botapp_projectstepmodel_18.order_index = 16
    botapp_projectstepmodel_18.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_18.value = 'lowest_price'
    botapp_projectstepmodel_18.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-total > trips-breakdown > div.breakdown > div > div.price-number.notranslate.short-price'
    botapp_projectstepmodel_18.variable = True
    botapp_projectstepmodel_18.project = botapp_projectmodel_1
    botapp_projectstepmodel_18 = importer.save_or_locate(botapp_projectstepmodel_18)

    botapp_projectstepmodel_19 = ClickProjectStepModel()
    botapp_projectstepmodel_19.display_name = 'Kisebb csomag súly'
    botapp_projectstepmodel_19.order_index = 19
    botapp_projectstepmodel_19.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_19.value = 'lower_bag_weight'
    botapp_projectstepmodel_19.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(1) > span.bag-item__weight'
    botapp_projectstepmodel_19.variable = True
    botapp_projectstepmodel_19.project = botapp_projectmodel_1
    botapp_projectstepmodel_19 = importer.save_or_locate(botapp_projectstepmodel_19)

    botapp_projectstepmodel_20 = ClickProjectStepModel()
    botapp_projectstepmodel_20.display_name = 'Kisebb csomag ár'
    botapp_projectstepmodel_20.order_index = 20
    botapp_projectstepmodel_20.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_20.value = 'lower_bag_price'
    botapp_projectstepmodel_20.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_20.variable = True
    botapp_projectstepmodel_20.project = botapp_projectmodel_1
    botapp_projectstepmodel_20 = importer.save_or_locate(botapp_projectstepmodel_20)

    botapp_projectstepmodel_21 = ClickProjectStepModel()
    botapp_projectstepmodel_21.display_name = 'Nagyobb csomag súly'
    botapp_projectstepmodel_21.order_index = 21
    botapp_projectstepmodel_21.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_21.value = 'larger_bag_weight'
    botapp_projectstepmodel_21.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__weight'
    botapp_projectstepmodel_21.variable = True
    botapp_projectstepmodel_21.project = botapp_projectmodel_1
    botapp_projectstepmodel_21 = importer.save_or_locate(botapp_projectstepmodel_21)

    botapp_projectstepmodel_22 = ClickProjectStepModel()
    botapp_projectstepmodel_22.display_name = 'Nagyobb csomag ár'
    botapp_projectstepmodel_22.order_index = 22
    botapp_projectstepmodel_22.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_22.value = 'larger_bag_price'
    botapp_projectstepmodel_22.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_22.variable = True
    botapp_projectstepmodel_22.project = botapp_projectmodel_1
    botapp_projectstepmodel_22 = importer.save_or_locate(botapp_projectstepmodel_22)

    botapp_projectstepmodel_23 = ClickProjectStepModel()
    botapp_projectstepmodel_23.display_name = 'Indulási állomás felugró megnyitása'
    botapp_projectstepmodel_23.order_index = 1
    botapp_projectstepmodel_23.action_type = 'clickAndWait'
    botapp_projectstepmodel_23.value = '1.0'
    botapp_projectstepmodel_23.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_23.variable = False
    botapp_projectstepmodel_23.project = botapp_projectmodel_2
    botapp_projectstepmodel_23 = importer.save_or_locate(botapp_projectstepmodel_23)

    botapp_projectstepmodel_24 = ClickProjectStepModel()
    botapp_projectstepmodel_24.display_name = 'Indulási ország kiválasztása'
    botapp_projectstepmodel_24.order_index = 2
    botapp_projectstepmodel_24.action_type = 'clickAndWait'
    botapp_projectstepmodel_24.value = '1.0'
    botapp_projectstepmodel_24.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div.core-list-item.core-list-item-rounded.clicked'
    botapp_projectstepmodel_24.variable = False
    botapp_projectstepmodel_24.project = botapp_projectmodel_2
    botapp_projectstepmodel_24 = importer.save_or_locate(botapp_projectstepmodel_24)

    botapp_projectstepmodel_25 = ClickProjectStepModel()
    botapp_projectstepmodel_25.display_name = 'Indulási repülőtér kiválasztása'
    botapp_projectstepmodel_25.order_index = 3
    botapp_projectstepmodel_25.action_type = 'clickAndWait'
    botapp_projectstepmodel_25.value = '1.0'
    botapp_projectstepmodel_25.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div.core-list-item.core-list-item-rounded.clicked > span'
    botapp_projectstepmodel_25.variable = False
    botapp_projectstepmodel_25.project = botapp_projectmodel_2
    botapp_projectstepmodel_25 = importer.save_or_locate(botapp_projectstepmodel_25)

    botapp_projectstepmodel_26 = ClickProjectStepModel()
    botapp_projectstepmodel_26.display_name = 'Érkezési állomás felugró megnyitása'
    botapp_projectstepmodel_26.order_index = 4
    botapp_projectstepmodel_26.action_type = 'clickAndWait'
    botapp_projectstepmodel_26.value = '1.0'
    botapp_projectstepmodel_26.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_26.variable = False
    botapp_projectstepmodel_26.project = botapp_projectmodel_2
    botapp_projectstepmodel_26 = importer.save_or_locate(botapp_projectstepmodel_26)

    botapp_projectstepmodel_27 = ClickProjectStepModel()
    botapp_projectstepmodel_27.display_name = 'Érkezési ország kiválasztása'
    botapp_projectstepmodel_27.order_index = 5
    botapp_projectstepmodel_27.action_type = 'clickAndWait'
    botapp_projectstepmodel_27.value = '1.0'
    botapp_projectstepmodel_27.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div:nth-child(4)'
    botapp_projectstepmodel_27.variable = False
    botapp_projectstepmodel_27.project = botapp_projectmodel_2
    botapp_projectstepmodel_27 = importer.save_or_locate(botapp_projectstepmodel_27)

    botapp_projectstepmodel_28 = ClickProjectStepModel()
    botapp_projectstepmodel_28.display_name = 'Érkezési repülőtér kiválasztása'
    botapp_projectstepmodel_28.order_index = 6
    botapp_projectstepmodel_28.action_type = 'clickAndWait'
    botapp_projectstepmodel_28.value = '1.0'
    botapp_projectstepmodel_28.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div:nth-child(3) > span'
    botapp_projectstepmodel_28.variable = False
    botapp_projectstepmodel_28.project = botapp_projectmodel_2
    botapp_projectstepmodel_28 = importer.save_or_locate(botapp_projectstepmodel_28)

    botapp_projectstepmodel_29 = ClickProjectStepModel()
    botapp_projectstepmodel_29.display_name = 'Utasok felugró kiválasztása'
    botapp_projectstepmodel_29.order_index = 7
    botapp_projectstepmodel_29.action_type = 'clickAndWait'
    botapp_projectstepmodel_29.value = '1.0'
    botapp_projectstepmodel_29.html_query = '#row-dates-pax > div.col-passengers > div:nth-child(2) > div:nth-child(5) > div > div.value'
    botapp_projectstepmodel_29.variable = False
    botapp_projectstepmodel_29.project = botapp_projectmodel_2
    botapp_projectstepmodel_29 = importer.save_or_locate(botapp_projectstepmodel_29)

    botapp_projectstepmodel_30 = ClickProjectStepModel()
    botapp_projectstepmodel_30.display_name = '1 (+1) utas hozzáadása'
    botapp_projectstepmodel_30.order_index = 8
    botapp_projectstepmodel_30.action_type = 'clickAndWait'
    botapp_projectstepmodel_30.value = '1.0'
    botapp_projectstepmodel_30.html_query = '#row-dates-pax > div.col-passengers > div.popup-passenger-input.opened > div > div > div.content > popup-content > div:nth-child(6) > div > div.details-controls > core-inc-dec > button.core-btn.inc.core-btn-wrap'
    botapp_projectstepmodel_30.variable = False
    botapp_projectstepmodel_30.project = botapp_projectmodel_2
    botapp_projectstepmodel_30 = importer.save_or_locate(botapp_projectstepmodel_30)

    botapp_projectstepmodel_31 = ClickProjectStepModel()
    botapp_projectstepmodel_31.display_name = 'Indulási időpont kiválasztása'
    botapp_projectstepmodel_31.order_index = 9
    botapp_projectstepmodel_31.action_type = 'clickAndWait'
    botapp_projectstepmodel_31.value = '1.0'
    botapp_projectstepmodel_31.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required > div.focused > div'
    botapp_projectstepmodel_31.variable = False
    botapp_projectstepmodel_31.project = botapp_projectmodel_2
    botapp_projectstepmodel_31 = importer.save_or_locate(botapp_projectstepmodel_31)

    botapp_projectstepmodel_32 = ClickProjectStepModel()
    botapp_projectstepmodel_32.display_name = 'Visszaút kiválasztása'
    botapp_projectstepmodel_32.order_index = 10
    botapp_projectstepmodel_32.action_type = 'clickAndWait'
    botapp_projectstepmodel_32.value = '1.0'
    botapp_projectstepmodel_32.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.core-date-range.popup-start-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.six-rows.scrollable > ul > li:nth-child(1) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_32.variable = False
    botapp_projectstepmodel_32.project = botapp_projectmodel_2
    botapp_projectstepmodel_32 = importer.save_or_locate(botapp_projectstepmodel_32)

    botapp_projectstepmodel_33 = ClickProjectStepModel()
    botapp_projectstepmodel_33.display_name = 'Indulásra kattintás'
    botapp_projectstepmodel_33.order_index = 11
    botapp_projectstepmodel_33.action_type = 'clickAndWait'
    botapp_projectstepmodel_33.value = '1.0'
    botapp_projectstepmodel_33.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-to > div > div.core-date-range.popup-end-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.scrollable.six-rows > ul > li:nth-child(2) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_33.variable = False
    botapp_projectstepmodel_33.project = botapp_projectmodel_2
    botapp_projectstepmodel_33 = importer.save_or_locate(botapp_projectstepmodel_33)

    botapp_projectstepmodel_34 = ClickProjectStepModel()
    botapp_projectstepmodel_34.display_name = 'Oda "összegtől" gomb megnyomása'
    botapp_projectstepmodel_34.order_index = 12
    botapp_projectstepmodel_34.action_type = 'clickAndWait'
    botapp_projectstepmodel_34.value = '1.0'
    botapp_projectstepmodel_34.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-right > button:nth-child(2)'
    botapp_projectstepmodel_34.variable = False
    botapp_projectstepmodel_34.project = botapp_projectmodel_2
    botapp_projectstepmodel_34 = importer.save_or_locate(botapp_projectstepmodel_34)

    botapp_projectstepmodel_35 = ClickProjectStepModel()
    botapp_projectstepmodel_35.display_name = 'Oda normál viteldíj beállítása'
    botapp_projectstepmodel_35.order_index = 13
    botapp_projectstepmodel_35.action_type = 'clickAndWait'
    botapp_projectstepmodel_35.value = '1.0'
    botapp_projectstepmodel_35.html_query = '#flight-FR\x07e 8415\x07e \x10 \x07e \x07e BUD\x07e 09\x02f 09\x02f 2017\x10 20\x03a 20\x07e CRL\x07e 09\x02f 09\x02f 2017\x10 22\x03a 25\x07e > div > div.flight-header__min-price.hide-mobile'
    botapp_projectstepmodel_35.variable = False
    botapp_projectstepmodel_35.project = botapp_projectmodel_2
    botapp_projectstepmodel_35 = importer.save_or_locate(botapp_projectstepmodel_35)

    botapp_projectstepmodel_36 = ClickProjectStepModel()
    botapp_projectstepmodel_36.display_name = 'Vissza "összegtől" gomb megnyomása'
    botapp_projectstepmodel_36.order_index = 14
    botapp_projectstepmodel_36.action_type = 'clickAndWait'
    botapp_projectstepmodel_36.value = '1.0'
    botapp_projectstepmodel_36.html_query = '#flight-FR\x07e 8416\x07e \x10 \x07e \x07e CRL\x07e 10\x02f 14\x02f 2017\x10 17\x03a 55\x07e BUD\x07e 10\x02f 14\x02f 2017\x10 19\x03a 55\x07e > div > div.flight-header__min-price.hide-mobile > flights-table-price > div > div.core-btn-primary'
    botapp_projectstepmodel_36.variable = False
    botapp_projectstepmodel_36.project = botapp_projectmodel_2
    botapp_projectstepmodel_36 = importer.save_or_locate(botapp_projectstepmodel_36)

    botapp_projectstepmodel_37 = ClickProjectStepModel()
    botapp_projectstepmodel_37.display_name = 'Folytatás gombra kattintés'
    botapp_projectstepmodel_37.order_index = 15
    botapp_projectstepmodel_37.action_type = 'clickAndWait'
    botapp_projectstepmodel_37.value = '1.0'
    botapp_projectstepmodel_37.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-cnt > button'
    botapp_projectstepmodel_37.variable = False
    botapp_projectstepmodel_37.project = botapp_projectmodel_2
    botapp_projectstepmodel_37 = importer.save_or_locate(botapp_projectstepmodel_37)

    botapp_projectstepmodel_38 = ClickProjectStepModel()
    botapp_projectstepmodel_38.display_name = 'Csomag hozzáadása'
    botapp_projectstepmodel_38.order_index = 17
    botapp_projectstepmodel_38.action_type = 'clickAndWait'
    botapp_projectstepmodel_38.value = '1.0'
    botapp_projectstepmodel_38.html_query = 'body > div.FR > main > div.body-section > extras-panels > section > article > leaderboard > div > extras-card:nth-child(3) > ng-include > div > div.action > button.core-btn-primary.add'
    botapp_projectstepmodel_38.variable = False
    botapp_projectstepmodel_38.project = botapp_projectmodel_2
    botapp_projectstepmodel_38 = importer.save_or_locate(botapp_projectstepmodel_38)

    botapp_projectstepmodel_39 = ClickProjectStepModel()
    botapp_projectstepmodel_39.display_name = 'Csomag hozzáadása felugró'
    botapp_projectstepmodel_39.order_index = 18
    botapp_projectstepmodel_39.action_type = 'clickAndWait'
    botapp_projectstepmodel_39.value = '1.0'
    botapp_projectstepmodel_39.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div'
    botapp_projectstepmodel_39.variable = False
    botapp_projectstepmodel_39.project = botapp_projectmodel_2
    botapp_projectstepmodel_39 = importer.save_or_locate(botapp_projectstepmodel_39)

    botapp_projectstepmodel_40 = ClickProjectStepModel()
    botapp_projectstepmodel_40.display_name = 'Összeg mentése'
    botapp_projectstepmodel_40.order_index = 16
    botapp_projectstepmodel_40.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_40.value = 'lowest_price'
    botapp_projectstepmodel_40.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-total > trips-breakdown > div.breakdown > div > div.price-number.notranslate.short-price'
    botapp_projectstepmodel_40.variable = True
    botapp_projectstepmodel_40.project = botapp_projectmodel_2
    botapp_projectstepmodel_40 = importer.save_or_locate(botapp_projectstepmodel_40)

    botapp_projectstepmodel_41 = ClickProjectStepModel()
    botapp_projectstepmodel_41.display_name = 'Kisebb csomag súly'
    botapp_projectstepmodel_41.order_index = 19
    botapp_projectstepmodel_41.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_41.value = 'lower_bag_weight'
    botapp_projectstepmodel_41.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(1) > span.bag-item__weight'
    botapp_projectstepmodel_41.variable = True
    botapp_projectstepmodel_41.project = botapp_projectmodel_2
    botapp_projectstepmodel_41 = importer.save_or_locate(botapp_projectstepmodel_41)

    botapp_projectstepmodel_42 = ClickProjectStepModel()
    botapp_projectstepmodel_42.display_name = 'Kisebb csomag ár'
    botapp_projectstepmodel_42.order_index = 20
    botapp_projectstepmodel_42.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_42.value = 'lower_bag_price'
    botapp_projectstepmodel_42.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_42.variable = True
    botapp_projectstepmodel_42.project = botapp_projectmodel_2
    botapp_projectstepmodel_42 = importer.save_or_locate(botapp_projectstepmodel_42)

    botapp_projectstepmodel_43 = ClickProjectStepModel()
    botapp_projectstepmodel_43.display_name = 'Nagyobb csomag súly'
    botapp_projectstepmodel_43.order_index = 21
    botapp_projectstepmodel_43.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_43.value = 'larger_bag_weight'
    botapp_projectstepmodel_43.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__weight'
    botapp_projectstepmodel_43.variable = True
    botapp_projectstepmodel_43.project = botapp_projectmodel_2
    botapp_projectstepmodel_43 = importer.save_or_locate(botapp_projectstepmodel_43)

    botapp_projectstepmodel_44 = ClickProjectStepModel()
    botapp_projectstepmodel_44.display_name = 'Nagyobb csomag ár'
    botapp_projectstepmodel_44.order_index = 22
    botapp_projectstepmodel_44.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_44.value = 'larger_bag_price'
    botapp_projectstepmodel_44.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_44.variable = True
    botapp_projectstepmodel_44.project = botapp_projectmodel_2
    botapp_projectstepmodel_44 = importer.save_or_locate(botapp_projectstepmodel_44)

    # Processing model: botapp.models.OpenProjectStepModel

    from botapp.models import OpenProjectStepModel

    botapp_projectstepmodel_1 = OpenProjectStepModel()
    botapp_projectstepmodel_1.display_name = 'Indulási állomás felugró megnyitása'
    botapp_projectstepmodel_1.order_index = 1
    botapp_projectstepmodel_1.action_type = 'clickAndWait'
    botapp_projectstepmodel_1.value = '1.0'
    botapp_projectstepmodel_1.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_1.variable = False
    botapp_projectstepmodel_1.project = botapp_projectmodel_1
    botapp_projectstepmodel_1 = importer.save_or_locate(botapp_projectstepmodel_1)

    botapp_projectstepmodel_2 = OpenProjectStepModel()
    botapp_projectstepmodel_2.display_name = 'Indulási ország kiválasztása'
    botapp_projectstepmodel_2.order_index = 2
    botapp_projectstepmodel_2.action_type = 'clickAndWait'
    botapp_projectstepmodel_2.value = '1.0'
    botapp_projectstepmodel_2.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div.core-list-item.core-list-item-rounded.clicked'
    botapp_projectstepmodel_2.variable = False
    botapp_projectstepmodel_2.project = botapp_projectmodel_1
    botapp_projectstepmodel_2 = importer.save_or_locate(botapp_projectstepmodel_2)

    botapp_projectstepmodel_3 = OpenProjectStepModel()
    botapp_projectstepmodel_3.display_name = 'Indulási repülőtér kiválasztása'
    botapp_projectstepmodel_3.order_index = 3
    botapp_projectstepmodel_3.action_type = 'clickAndWait'
    botapp_projectstepmodel_3.value = '1.0'
    botapp_projectstepmodel_3.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div.core-list-item.core-list-item-rounded.clicked > span'
    botapp_projectstepmodel_3.variable = False
    botapp_projectstepmodel_3.project = botapp_projectmodel_1
    botapp_projectstepmodel_3 = importer.save_or_locate(botapp_projectstepmodel_3)

    botapp_projectstepmodel_4 = OpenProjectStepModel()
    botapp_projectstepmodel_4.display_name = 'Érkezési állomás felugró megnyitása'
    botapp_projectstepmodel_4.order_index = 4
    botapp_projectstepmodel_4.action_type = 'clickAndWait'
    botapp_projectstepmodel_4.value = '1.0'
    botapp_projectstepmodel_4.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_4.variable = False
    botapp_projectstepmodel_4.project = botapp_projectmodel_1
    botapp_projectstepmodel_4 = importer.save_or_locate(botapp_projectstepmodel_4)

    botapp_projectstepmodel_5 = OpenProjectStepModel()
    botapp_projectstepmodel_5.display_name = 'Érkezési ország kiválasztása'
    botapp_projectstepmodel_5.order_index = 5
    botapp_projectstepmodel_5.action_type = 'clickAndWait'
    botapp_projectstepmodel_5.value = '1.0'
    botapp_projectstepmodel_5.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div:nth-child(4)'
    botapp_projectstepmodel_5.variable = False
    botapp_projectstepmodel_5.project = botapp_projectmodel_1
    botapp_projectstepmodel_5 = importer.save_or_locate(botapp_projectstepmodel_5)

    botapp_projectstepmodel_6 = OpenProjectStepModel()
    botapp_projectstepmodel_6.display_name = 'Érkezési repülőtér kiválasztása'
    botapp_projectstepmodel_6.order_index = 6
    botapp_projectstepmodel_6.action_type = 'clickAndWait'
    botapp_projectstepmodel_6.value = '1.0'
    botapp_projectstepmodel_6.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div:nth-child(3) > span'
    botapp_projectstepmodel_6.variable = False
    botapp_projectstepmodel_6.project = botapp_projectmodel_1
    botapp_projectstepmodel_6 = importer.save_or_locate(botapp_projectstepmodel_6)

    botapp_projectstepmodel_7 = OpenProjectStepModel()
    botapp_projectstepmodel_7.display_name = 'Utasok felugró kiválasztása'
    botapp_projectstepmodel_7.order_index = 7
    botapp_projectstepmodel_7.action_type = 'clickAndWait'
    botapp_projectstepmodel_7.value = '1.0'
    botapp_projectstepmodel_7.html_query = '#row-dates-pax > div.col-passengers > div:nth-child(2) > div:nth-child(5) > div > div.value'
    botapp_projectstepmodel_7.variable = False
    botapp_projectstepmodel_7.project = botapp_projectmodel_1
    botapp_projectstepmodel_7 = importer.save_or_locate(botapp_projectstepmodel_7)

    botapp_projectstepmodel_8 = OpenProjectStepModel()
    botapp_projectstepmodel_8.display_name = '1 (+1) utas hozzáadása'
    botapp_projectstepmodel_8.order_index = 8
    botapp_projectstepmodel_8.action_type = 'clickAndWait'
    botapp_projectstepmodel_8.value = '1.0'
    botapp_projectstepmodel_8.html_query = '#row-dates-pax > div.col-passengers > div.popup-passenger-input.opened > div > div > div.content > popup-content > div:nth-child(6) > div > div.details-controls > core-inc-dec > button.core-btn.inc.core-btn-wrap'
    botapp_projectstepmodel_8.variable = False
    botapp_projectstepmodel_8.project = botapp_projectmodel_1
    botapp_projectstepmodel_8 = importer.save_or_locate(botapp_projectstepmodel_8)

    botapp_projectstepmodel_9 = OpenProjectStepModel()
    botapp_projectstepmodel_9.display_name = 'Indulási időpont kiválasztása'
    botapp_projectstepmodel_9.order_index = 9
    botapp_projectstepmodel_9.action_type = 'clickAndWait'
    botapp_projectstepmodel_9.value = '1.0'
    botapp_projectstepmodel_9.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required > div.focused > div'
    botapp_projectstepmodel_9.variable = False
    botapp_projectstepmodel_9.project = botapp_projectmodel_1
    botapp_projectstepmodel_9 = importer.save_or_locate(botapp_projectstepmodel_9)

    botapp_projectstepmodel_10 = OpenProjectStepModel()
    botapp_projectstepmodel_10.display_name = 'Visszaút kiválasztása'
    botapp_projectstepmodel_10.order_index = 10
    botapp_projectstepmodel_10.action_type = 'clickAndWait'
    botapp_projectstepmodel_10.value = '1.0'
    botapp_projectstepmodel_10.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.core-date-range.popup-start-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.six-rows.scrollable > ul > li:nth-child(1) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_10.variable = False
    botapp_projectstepmodel_10.project = botapp_projectmodel_1
    botapp_projectstepmodel_10 = importer.save_or_locate(botapp_projectstepmodel_10)

    botapp_projectstepmodel_11 = OpenProjectStepModel()
    botapp_projectstepmodel_11.display_name = 'Indulásra kattintás'
    botapp_projectstepmodel_11.order_index = 11
    botapp_projectstepmodel_11.action_type = 'clickAndWait'
    botapp_projectstepmodel_11.value = '1.0'
    botapp_projectstepmodel_11.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-to > div > div.core-date-range.popup-end-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.scrollable.six-rows > ul > li:nth-child(2) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_11.variable = False
    botapp_projectstepmodel_11.project = botapp_projectmodel_1
    botapp_projectstepmodel_11 = importer.save_or_locate(botapp_projectstepmodel_11)

    botapp_projectstepmodel_12 = OpenProjectStepModel()
    botapp_projectstepmodel_12.display_name = 'Oda "összegtől" gomb megnyomása'
    botapp_projectstepmodel_12.order_index = 12
    botapp_projectstepmodel_12.action_type = 'clickAndWait'
    botapp_projectstepmodel_12.value = '1.0'
    botapp_projectstepmodel_12.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-right > button:nth-child(2)'
    botapp_projectstepmodel_12.variable = False
    botapp_projectstepmodel_12.project = botapp_projectmodel_1
    botapp_projectstepmodel_12 = importer.save_or_locate(botapp_projectstepmodel_12)

    botapp_projectstepmodel_13 = OpenProjectStepModel()
    botapp_projectstepmodel_13.display_name = 'Oda normál viteldíj beállítása'
    botapp_projectstepmodel_13.order_index = 13
    botapp_projectstepmodel_13.action_type = 'clickAndWait'
    botapp_projectstepmodel_13.value = '1.0'
    botapp_projectstepmodel_13.html_query = '#flight-FR\x07e 8415\x07e \x10 \x07e \x07e BUD\x07e 09\x02f 09\x02f 2017\x10 20\x03a 20\x07e CRL\x07e 09\x02f 09\x02f 2017\x10 22\x03a 25\x07e > div > div.flight-header__min-price.hide-mobile'
    botapp_projectstepmodel_13.variable = False
    botapp_projectstepmodel_13.project = botapp_projectmodel_1
    botapp_projectstepmodel_13 = importer.save_or_locate(botapp_projectstepmodel_13)

    botapp_projectstepmodel_14 = OpenProjectStepModel()
    botapp_projectstepmodel_14.display_name = 'Vissza "összegtől" gomb megnyomása'
    botapp_projectstepmodel_14.order_index = 14
    botapp_projectstepmodel_14.action_type = 'clickAndWait'
    botapp_projectstepmodel_14.value = '1.0'
    botapp_projectstepmodel_14.html_query = '#flight-FR\x07e 8416\x07e \x10 \x07e \x07e CRL\x07e 10\x02f 14\x02f 2017\x10 17\x03a 55\x07e BUD\x07e 10\x02f 14\x02f 2017\x10 19\x03a 55\x07e > div > div.flight-header__min-price.hide-mobile > flights-table-price > div > div.core-btn-primary'
    botapp_projectstepmodel_14.variable = False
    botapp_projectstepmodel_14.project = botapp_projectmodel_1
    botapp_projectstepmodel_14 = importer.save_or_locate(botapp_projectstepmodel_14)

    botapp_projectstepmodel_15 = OpenProjectStepModel()
    botapp_projectstepmodel_15.display_name = 'Folytatás gombra kattintés'
    botapp_projectstepmodel_15.order_index = 15
    botapp_projectstepmodel_15.action_type = 'clickAndWait'
    botapp_projectstepmodel_15.value = '1.0'
    botapp_projectstepmodel_15.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-cnt > button'
    botapp_projectstepmodel_15.variable = False
    botapp_projectstepmodel_15.project = botapp_projectmodel_1
    botapp_projectstepmodel_15 = importer.save_or_locate(botapp_projectstepmodel_15)

    botapp_projectstepmodel_16 = OpenProjectStepModel()
    botapp_projectstepmodel_16.display_name = 'Csomag hozzáadása'
    botapp_projectstepmodel_16.order_index = 17
    botapp_projectstepmodel_16.action_type = 'clickAndWait'
    botapp_projectstepmodel_16.value = '1.0'
    botapp_projectstepmodel_16.html_query = 'body > div.FR > main > div.body-section > extras-panels > section > article > leaderboard > div > extras-card:nth-child(3) > ng-include > div > div.action > button.core-btn-primary.add'
    botapp_projectstepmodel_16.variable = False
    botapp_projectstepmodel_16.project = botapp_projectmodel_1
    botapp_projectstepmodel_16 = importer.save_or_locate(botapp_projectstepmodel_16)

    botapp_projectstepmodel_17 = OpenProjectStepModel()
    botapp_projectstepmodel_17.display_name = 'Csomag hozzáadása felugró'
    botapp_projectstepmodel_17.order_index = 18
    botapp_projectstepmodel_17.action_type = 'clickAndWait'
    botapp_projectstepmodel_17.value = '1.0'
    botapp_projectstepmodel_17.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div'
    botapp_projectstepmodel_17.variable = False
    botapp_projectstepmodel_17.project = botapp_projectmodel_1
    botapp_projectstepmodel_17 = importer.save_or_locate(botapp_projectstepmodel_17)

    botapp_projectstepmodel_18 = OpenProjectStepModel()
    botapp_projectstepmodel_18.display_name = 'Összeg mentése'
    botapp_projectstepmodel_18.order_index = 16
    botapp_projectstepmodel_18.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_18.value = 'lowest_price'
    botapp_projectstepmodel_18.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-total > trips-breakdown > div.breakdown > div > div.price-number.notranslate.short-price'
    botapp_projectstepmodel_18.variable = True
    botapp_projectstepmodel_18.project = botapp_projectmodel_1
    botapp_projectstepmodel_18 = importer.save_or_locate(botapp_projectstepmodel_18)

    botapp_projectstepmodel_19 = OpenProjectStepModel()
    botapp_projectstepmodel_19.display_name = 'Kisebb csomag súly'
    botapp_projectstepmodel_19.order_index = 19
    botapp_projectstepmodel_19.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_19.value = 'lower_bag_weight'
    botapp_projectstepmodel_19.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(1) > span.bag-item__weight'
    botapp_projectstepmodel_19.variable = True
    botapp_projectstepmodel_19.project = botapp_projectmodel_1
    botapp_projectstepmodel_19 = importer.save_or_locate(botapp_projectstepmodel_19)

    botapp_projectstepmodel_20 = OpenProjectStepModel()
    botapp_projectstepmodel_20.display_name = 'Kisebb csomag ár'
    botapp_projectstepmodel_20.order_index = 20
    botapp_projectstepmodel_20.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_20.value = 'lower_bag_price'
    botapp_projectstepmodel_20.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_20.variable = True
    botapp_projectstepmodel_20.project = botapp_projectmodel_1
    botapp_projectstepmodel_20 = importer.save_or_locate(botapp_projectstepmodel_20)

    botapp_projectstepmodel_21 = OpenProjectStepModel()
    botapp_projectstepmodel_21.display_name = 'Nagyobb csomag súly'
    botapp_projectstepmodel_21.order_index = 21
    botapp_projectstepmodel_21.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_21.value = 'larger_bag_weight'
    botapp_projectstepmodel_21.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__weight'
    botapp_projectstepmodel_21.variable = True
    botapp_projectstepmodel_21.project = botapp_projectmodel_1
    botapp_projectstepmodel_21 = importer.save_or_locate(botapp_projectstepmodel_21)

    botapp_projectstepmodel_22 = OpenProjectStepModel()
    botapp_projectstepmodel_22.display_name = 'Nagyobb csomag ár'
    botapp_projectstepmodel_22.order_index = 22
    botapp_projectstepmodel_22.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_22.value = 'larger_bag_price'
    botapp_projectstepmodel_22.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_22.variable = True
    botapp_projectstepmodel_22.project = botapp_projectmodel_1
    botapp_projectstepmodel_22 = importer.save_or_locate(botapp_projectstepmodel_22)

    botapp_projectstepmodel_23 = OpenProjectStepModel()
    botapp_projectstepmodel_23.display_name = 'Indulási állomás felugró megnyitása'
    botapp_projectstepmodel_23.order_index = 1
    botapp_projectstepmodel_23.action_type = 'clickAndWait'
    botapp_projectstepmodel_23.value = '1.0'
    botapp_projectstepmodel_23.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_23.variable = False
    botapp_projectstepmodel_23.project = botapp_projectmodel_2
    botapp_projectstepmodel_23 = importer.save_or_locate(botapp_projectstepmodel_23)

    botapp_projectstepmodel_24 = OpenProjectStepModel()
    botapp_projectstepmodel_24.display_name = 'Indulási ország kiválasztása'
    botapp_projectstepmodel_24.order_index = 2
    botapp_projectstepmodel_24.action_type = 'clickAndWait'
    botapp_projectstepmodel_24.value = '1.0'
    botapp_projectstepmodel_24.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div.core-list-item.core-list-item-rounded.clicked'
    botapp_projectstepmodel_24.variable = False
    botapp_projectstepmodel_24.project = botapp_projectmodel_2
    botapp_projectstepmodel_24 = importer.save_or_locate(botapp_projectstepmodel_24)

    botapp_projectstepmodel_25 = OpenProjectStepModel()
    botapp_projectstepmodel_25.display_name = 'Indulási repülőtér kiválasztása'
    botapp_projectstepmodel_25.order_index = 3
    botapp_projectstepmodel_25.action_type = 'clickAndWait'
    botapp_projectstepmodel_25.value = '1.0'
    botapp_projectstepmodel_25.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div.core-list-item.core-list-item-rounded.clicked > span'
    botapp_projectstepmodel_25.variable = False
    botapp_projectstepmodel_25.project = botapp_projectmodel_2
    botapp_projectstepmodel_25 = importer.save_or_locate(botapp_projectstepmodel_25)

    botapp_projectstepmodel_26 = OpenProjectStepModel()
    botapp_projectstepmodel_26.display_name = 'Érkezési állomás felugró megnyitása'
    botapp_projectstepmodel_26.order_index = 4
    botapp_projectstepmodel_26.action_type = 'clickAndWait'
    botapp_projectstepmodel_26.value = '1.0'
    botapp_projectstepmodel_26.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_26.variable = False
    botapp_projectstepmodel_26.project = botapp_projectmodel_2
    botapp_projectstepmodel_26 = importer.save_or_locate(botapp_projectstepmodel_26)

    botapp_projectstepmodel_27 = OpenProjectStepModel()
    botapp_projectstepmodel_27.display_name = 'Érkezési ország kiválasztása'
    botapp_projectstepmodel_27.order_index = 5
    botapp_projectstepmodel_27.action_type = 'clickAndWait'
    botapp_projectstepmodel_27.value = '1.0'
    botapp_projectstepmodel_27.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div:nth-child(4)'
    botapp_projectstepmodel_27.variable = False
    botapp_projectstepmodel_27.project = botapp_projectmodel_2
    botapp_projectstepmodel_27 = importer.save_or_locate(botapp_projectstepmodel_27)

    botapp_projectstepmodel_28 = OpenProjectStepModel()
    botapp_projectstepmodel_28.display_name = 'Érkezési repülőtér kiválasztása'
    botapp_projectstepmodel_28.order_index = 6
    botapp_projectstepmodel_28.action_type = 'clickAndWait'
    botapp_projectstepmodel_28.value = '1.0'
    botapp_projectstepmodel_28.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div:nth-child(3) > span'
    botapp_projectstepmodel_28.variable = False
    botapp_projectstepmodel_28.project = botapp_projectmodel_2
    botapp_projectstepmodel_28 = importer.save_or_locate(botapp_projectstepmodel_28)

    botapp_projectstepmodel_29 = OpenProjectStepModel()
    botapp_projectstepmodel_29.display_name = 'Utasok felugró kiválasztása'
    botapp_projectstepmodel_29.order_index = 7
    botapp_projectstepmodel_29.action_type = 'clickAndWait'
    botapp_projectstepmodel_29.value = '1.0'
    botapp_projectstepmodel_29.html_query = '#row-dates-pax > div.col-passengers > div:nth-child(2) > div:nth-child(5) > div > div.value'
    botapp_projectstepmodel_29.variable = False
    botapp_projectstepmodel_29.project = botapp_projectmodel_2
    botapp_projectstepmodel_29 = importer.save_or_locate(botapp_projectstepmodel_29)

    botapp_projectstepmodel_30 = OpenProjectStepModel()
    botapp_projectstepmodel_30.display_name = '1 (+1) utas hozzáadása'
    botapp_projectstepmodel_30.order_index = 8
    botapp_projectstepmodel_30.action_type = 'clickAndWait'
    botapp_projectstepmodel_30.value = '1.0'
    botapp_projectstepmodel_30.html_query = '#row-dates-pax > div.col-passengers > div.popup-passenger-input.opened > div > div > div.content > popup-content > div:nth-child(6) > div > div.details-controls > core-inc-dec > button.core-btn.inc.core-btn-wrap'
    botapp_projectstepmodel_30.variable = False
    botapp_projectstepmodel_30.project = botapp_projectmodel_2
    botapp_projectstepmodel_30 = importer.save_or_locate(botapp_projectstepmodel_30)

    botapp_projectstepmodel_31 = OpenProjectStepModel()
    botapp_projectstepmodel_31.display_name = 'Indulási időpont kiválasztása'
    botapp_projectstepmodel_31.order_index = 9
    botapp_projectstepmodel_31.action_type = 'clickAndWait'
    botapp_projectstepmodel_31.value = '1.0'
    botapp_projectstepmodel_31.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required > div.focused > div'
    botapp_projectstepmodel_31.variable = False
    botapp_projectstepmodel_31.project = botapp_projectmodel_2
    botapp_projectstepmodel_31 = importer.save_or_locate(botapp_projectstepmodel_31)

    botapp_projectstepmodel_32 = OpenProjectStepModel()
    botapp_projectstepmodel_32.display_name = 'Visszaút kiválasztása'
    botapp_projectstepmodel_32.order_index = 10
    botapp_projectstepmodel_32.action_type = 'clickAndWait'
    botapp_projectstepmodel_32.value = '1.0'
    botapp_projectstepmodel_32.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.core-date-range.popup-start-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.six-rows.scrollable > ul > li:nth-child(1) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_32.variable = False
    botapp_projectstepmodel_32.project = botapp_projectmodel_2
    botapp_projectstepmodel_32 = importer.save_or_locate(botapp_projectstepmodel_32)

    botapp_projectstepmodel_33 = OpenProjectStepModel()
    botapp_projectstepmodel_33.display_name = 'Indulásra kattintás'
    botapp_projectstepmodel_33.order_index = 11
    botapp_projectstepmodel_33.action_type = 'clickAndWait'
    botapp_projectstepmodel_33.value = '1.0'
    botapp_projectstepmodel_33.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-to > div > div.core-date-range.popup-end-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.scrollable.six-rows > ul > li:nth-child(2) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_33.variable = False
    botapp_projectstepmodel_33.project = botapp_projectmodel_2
    botapp_projectstepmodel_33 = importer.save_or_locate(botapp_projectstepmodel_33)

    botapp_projectstepmodel_34 = OpenProjectStepModel()
    botapp_projectstepmodel_34.display_name = 'Oda "összegtől" gomb megnyomása'
    botapp_projectstepmodel_34.order_index = 12
    botapp_projectstepmodel_34.action_type = 'clickAndWait'
    botapp_projectstepmodel_34.value = '1.0'
    botapp_projectstepmodel_34.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-right > button:nth-child(2)'
    botapp_projectstepmodel_34.variable = False
    botapp_projectstepmodel_34.project = botapp_projectmodel_2
    botapp_projectstepmodel_34 = importer.save_or_locate(botapp_projectstepmodel_34)

    botapp_projectstepmodel_35 = OpenProjectStepModel()
    botapp_projectstepmodel_35.display_name = 'Oda normál viteldíj beállítása'
    botapp_projectstepmodel_35.order_index = 13
    botapp_projectstepmodel_35.action_type = 'clickAndWait'
    botapp_projectstepmodel_35.value = '1.0'
    botapp_projectstepmodel_35.html_query = '#flight-FR\x07e 8415\x07e \x10 \x07e \x07e BUD\x07e 09\x02f 09\x02f 2017\x10 20\x03a 20\x07e CRL\x07e 09\x02f 09\x02f 2017\x10 22\x03a 25\x07e > div > div.flight-header__min-price.hide-mobile'
    botapp_projectstepmodel_35.variable = False
    botapp_projectstepmodel_35.project = botapp_projectmodel_2
    botapp_projectstepmodel_35 = importer.save_or_locate(botapp_projectstepmodel_35)

    botapp_projectstepmodel_36 = OpenProjectStepModel()
    botapp_projectstepmodel_36.display_name = 'Vissza "összegtől" gomb megnyomása'
    botapp_projectstepmodel_36.order_index = 14
    botapp_projectstepmodel_36.action_type = 'clickAndWait'
    botapp_projectstepmodel_36.value = '1.0'
    botapp_projectstepmodel_36.html_query = '#flight-FR\x07e 8416\x07e \x10 \x07e \x07e CRL\x07e 10\x02f 14\x02f 2017\x10 17\x03a 55\x07e BUD\x07e 10\x02f 14\x02f 2017\x10 19\x03a 55\x07e > div > div.flight-header__min-price.hide-mobile > flights-table-price > div > div.core-btn-primary'
    botapp_projectstepmodel_36.variable = False
    botapp_projectstepmodel_36.project = botapp_projectmodel_2
    botapp_projectstepmodel_36 = importer.save_or_locate(botapp_projectstepmodel_36)

    botapp_projectstepmodel_37 = OpenProjectStepModel()
    botapp_projectstepmodel_37.display_name = 'Folytatás gombra kattintés'
    botapp_projectstepmodel_37.order_index = 15
    botapp_projectstepmodel_37.action_type = 'clickAndWait'
    botapp_projectstepmodel_37.value = '1.0'
    botapp_projectstepmodel_37.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-cnt > button'
    botapp_projectstepmodel_37.variable = False
    botapp_projectstepmodel_37.project = botapp_projectmodel_2
    botapp_projectstepmodel_37 = importer.save_or_locate(botapp_projectstepmodel_37)

    botapp_projectstepmodel_38 = OpenProjectStepModel()
    botapp_projectstepmodel_38.display_name = 'Csomag hozzáadása'
    botapp_projectstepmodel_38.order_index = 17
    botapp_projectstepmodel_38.action_type = 'clickAndWait'
    botapp_projectstepmodel_38.value = '1.0'
    botapp_projectstepmodel_38.html_query = 'body > div.FR > main > div.body-section > extras-panels > section > article > leaderboard > div > extras-card:nth-child(3) > ng-include > div > div.action > button.core-btn-primary.add'
    botapp_projectstepmodel_38.variable = False
    botapp_projectstepmodel_38.project = botapp_projectmodel_2
    botapp_projectstepmodel_38 = importer.save_or_locate(botapp_projectstepmodel_38)

    botapp_projectstepmodel_39 = OpenProjectStepModel()
    botapp_projectstepmodel_39.display_name = 'Csomag hozzáadása felugró'
    botapp_projectstepmodel_39.order_index = 18
    botapp_projectstepmodel_39.action_type = 'clickAndWait'
    botapp_projectstepmodel_39.value = '1.0'
    botapp_projectstepmodel_39.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div'
    botapp_projectstepmodel_39.variable = False
    botapp_projectstepmodel_39.project = botapp_projectmodel_2
    botapp_projectstepmodel_39 = importer.save_or_locate(botapp_projectstepmodel_39)

    botapp_projectstepmodel_40 = OpenProjectStepModel()
    botapp_projectstepmodel_40.display_name = 'Összeg mentése'
    botapp_projectstepmodel_40.order_index = 16
    botapp_projectstepmodel_40.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_40.value = 'lowest_price'
    botapp_projectstepmodel_40.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-total > trips-breakdown > div.breakdown > div > div.price-number.notranslate.short-price'
    botapp_projectstepmodel_40.variable = True
    botapp_projectstepmodel_40.project = botapp_projectmodel_2
    botapp_projectstepmodel_40 = importer.save_or_locate(botapp_projectstepmodel_40)

    botapp_projectstepmodel_41 = OpenProjectStepModel()
    botapp_projectstepmodel_41.display_name = 'Kisebb csomag súly'
    botapp_projectstepmodel_41.order_index = 19
    botapp_projectstepmodel_41.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_41.value = 'lower_bag_weight'
    botapp_projectstepmodel_41.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(1) > span.bag-item__weight'
    botapp_projectstepmodel_41.variable = True
    botapp_projectstepmodel_41.project = botapp_projectmodel_2
    botapp_projectstepmodel_41 = importer.save_or_locate(botapp_projectstepmodel_41)

    botapp_projectstepmodel_42 = OpenProjectStepModel()
    botapp_projectstepmodel_42.display_name = 'Kisebb csomag ár'
    botapp_projectstepmodel_42.order_index = 20
    botapp_projectstepmodel_42.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_42.value = 'lower_bag_price'
    botapp_projectstepmodel_42.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_42.variable = True
    botapp_projectstepmodel_42.project = botapp_projectmodel_2
    botapp_projectstepmodel_42 = importer.save_or_locate(botapp_projectstepmodel_42)

    botapp_projectstepmodel_43 = OpenProjectStepModel()
    botapp_projectstepmodel_43.display_name = 'Nagyobb csomag súly'
    botapp_projectstepmodel_43.order_index = 21
    botapp_projectstepmodel_43.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_43.value = 'larger_bag_weight'
    botapp_projectstepmodel_43.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__weight'
    botapp_projectstepmodel_43.variable = True
    botapp_projectstepmodel_43.project = botapp_projectmodel_2
    botapp_projectstepmodel_43 = importer.save_or_locate(botapp_projectstepmodel_43)

    botapp_projectstepmodel_44 = OpenProjectStepModel()
    botapp_projectstepmodel_44.display_name = 'Nagyobb csomag ár'
    botapp_projectstepmodel_44.order_index = 22
    botapp_projectstepmodel_44.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_44.value = 'larger_bag_price'
    botapp_projectstepmodel_44.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_44.variable = True
    botapp_projectstepmodel_44.project = botapp_projectmodel_2
    botapp_projectstepmodel_44 = importer.save_or_locate(botapp_projectstepmodel_44)

    # Processing model: botapp.models.WaitProjectStepModel

    from botapp.models import WaitProjectStepModel

    botapp_projectstepmodel_1 = WaitProjectStepModel()
    botapp_projectstepmodel_1.display_name = 'Indulási állomás felugró megnyitása'
    botapp_projectstepmodel_1.order_index = 1
    botapp_projectstepmodel_1.action_type = 'clickAndWait'
    botapp_projectstepmodel_1.value = '1.0'
    botapp_projectstepmodel_1.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_1.variable = False
    botapp_projectstepmodel_1.project = botapp_projectmodel_1
    botapp_projectstepmodel_1 = importer.save_or_locate(botapp_projectstepmodel_1)

    botapp_projectstepmodel_2 = WaitProjectStepModel()
    botapp_projectstepmodel_2.display_name = 'Indulási ország kiválasztása'
    botapp_projectstepmodel_2.order_index = 2
    botapp_projectstepmodel_2.action_type = 'clickAndWait'
    botapp_projectstepmodel_2.value = '1.0'
    botapp_projectstepmodel_2.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div.core-list-item.core-list-item-rounded.clicked'
    botapp_projectstepmodel_2.variable = False
    botapp_projectstepmodel_2.project = botapp_projectmodel_1
    botapp_projectstepmodel_2 = importer.save_or_locate(botapp_projectstepmodel_2)

    botapp_projectstepmodel_3 = WaitProjectStepModel()
    botapp_projectstepmodel_3.display_name = 'Indulási repülőtér kiválasztása'
    botapp_projectstepmodel_3.order_index = 3
    botapp_projectstepmodel_3.action_type = 'clickAndWait'
    botapp_projectstepmodel_3.value = '1.0'
    botapp_projectstepmodel_3.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div.core-list-item.core-list-item-rounded.clicked > span'
    botapp_projectstepmodel_3.variable = False
    botapp_projectstepmodel_3.project = botapp_projectmodel_1
    botapp_projectstepmodel_3 = importer.save_or_locate(botapp_projectstepmodel_3)

    botapp_projectstepmodel_4 = WaitProjectStepModel()
    botapp_projectstepmodel_4.display_name = 'Érkezési állomás felugró megnyitása'
    botapp_projectstepmodel_4.order_index = 4
    botapp_projectstepmodel_4.action_type = 'clickAndWait'
    botapp_projectstepmodel_4.value = '1.0'
    botapp_projectstepmodel_4.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_4.variable = False
    botapp_projectstepmodel_4.project = botapp_projectmodel_1
    botapp_projectstepmodel_4 = importer.save_or_locate(botapp_projectstepmodel_4)

    botapp_projectstepmodel_5 = WaitProjectStepModel()
    botapp_projectstepmodel_5.display_name = 'Érkezési ország kiválasztása'
    botapp_projectstepmodel_5.order_index = 5
    botapp_projectstepmodel_5.action_type = 'clickAndWait'
    botapp_projectstepmodel_5.value = '1.0'
    botapp_projectstepmodel_5.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div:nth-child(4)'
    botapp_projectstepmodel_5.variable = False
    botapp_projectstepmodel_5.project = botapp_projectmodel_1
    botapp_projectstepmodel_5 = importer.save_or_locate(botapp_projectstepmodel_5)

    botapp_projectstepmodel_6 = WaitProjectStepModel()
    botapp_projectstepmodel_6.display_name = 'Érkezési repülőtér kiválasztása'
    botapp_projectstepmodel_6.order_index = 6
    botapp_projectstepmodel_6.action_type = 'clickAndWait'
    botapp_projectstepmodel_6.value = '1.0'
    botapp_projectstepmodel_6.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div:nth-child(3) > span'
    botapp_projectstepmodel_6.variable = False
    botapp_projectstepmodel_6.project = botapp_projectmodel_1
    botapp_projectstepmodel_6 = importer.save_or_locate(botapp_projectstepmodel_6)

    botapp_projectstepmodel_7 = WaitProjectStepModel()
    botapp_projectstepmodel_7.display_name = 'Utasok felugró kiválasztása'
    botapp_projectstepmodel_7.order_index = 7
    botapp_projectstepmodel_7.action_type = 'clickAndWait'
    botapp_projectstepmodel_7.value = '1.0'
    botapp_projectstepmodel_7.html_query = '#row-dates-pax > div.col-passengers > div:nth-child(2) > div:nth-child(5) > div > div.value'
    botapp_projectstepmodel_7.variable = False
    botapp_projectstepmodel_7.project = botapp_projectmodel_1
    botapp_projectstepmodel_7 = importer.save_or_locate(botapp_projectstepmodel_7)

    botapp_projectstepmodel_8 = WaitProjectStepModel()
    botapp_projectstepmodel_8.display_name = '1 (+1) utas hozzáadása'
    botapp_projectstepmodel_8.order_index = 8
    botapp_projectstepmodel_8.action_type = 'clickAndWait'
    botapp_projectstepmodel_8.value = '1.0'
    botapp_projectstepmodel_8.html_query = '#row-dates-pax > div.col-passengers > div.popup-passenger-input.opened > div > div > div.content > popup-content > div:nth-child(6) > div > div.details-controls > core-inc-dec > button.core-btn.inc.core-btn-wrap'
    botapp_projectstepmodel_8.variable = False
    botapp_projectstepmodel_8.project = botapp_projectmodel_1
    botapp_projectstepmodel_8 = importer.save_or_locate(botapp_projectstepmodel_8)

    botapp_projectstepmodel_9 = WaitProjectStepModel()
    botapp_projectstepmodel_9.display_name = 'Indulási időpont kiválasztása'
    botapp_projectstepmodel_9.order_index = 9
    botapp_projectstepmodel_9.action_type = 'clickAndWait'
    botapp_projectstepmodel_9.value = '1.0'
    botapp_projectstepmodel_9.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required > div.focused > div'
    botapp_projectstepmodel_9.variable = False
    botapp_projectstepmodel_9.project = botapp_projectmodel_1
    botapp_projectstepmodel_9 = importer.save_or_locate(botapp_projectstepmodel_9)

    botapp_projectstepmodel_10 = WaitProjectStepModel()
    botapp_projectstepmodel_10.display_name = 'Visszaút kiválasztása'
    botapp_projectstepmodel_10.order_index = 10
    botapp_projectstepmodel_10.action_type = 'clickAndWait'
    botapp_projectstepmodel_10.value = '1.0'
    botapp_projectstepmodel_10.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.core-date-range.popup-start-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.six-rows.scrollable > ul > li:nth-child(1) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_10.variable = False
    botapp_projectstepmodel_10.project = botapp_projectmodel_1
    botapp_projectstepmodel_10 = importer.save_or_locate(botapp_projectstepmodel_10)

    botapp_projectstepmodel_11 = WaitProjectStepModel()
    botapp_projectstepmodel_11.display_name = 'Indulásra kattintás'
    botapp_projectstepmodel_11.order_index = 11
    botapp_projectstepmodel_11.action_type = 'clickAndWait'
    botapp_projectstepmodel_11.value = '1.0'
    botapp_projectstepmodel_11.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-to > div > div.core-date-range.popup-end-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.scrollable.six-rows > ul > li:nth-child(2) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_11.variable = False
    botapp_projectstepmodel_11.project = botapp_projectmodel_1
    botapp_projectstepmodel_11 = importer.save_or_locate(botapp_projectstepmodel_11)

    botapp_projectstepmodel_12 = WaitProjectStepModel()
    botapp_projectstepmodel_12.display_name = 'Oda "összegtől" gomb megnyomása'
    botapp_projectstepmodel_12.order_index = 12
    botapp_projectstepmodel_12.action_type = 'clickAndWait'
    botapp_projectstepmodel_12.value = '1.0'
    botapp_projectstepmodel_12.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-right > button:nth-child(2)'
    botapp_projectstepmodel_12.variable = False
    botapp_projectstepmodel_12.project = botapp_projectmodel_1
    botapp_projectstepmodel_12 = importer.save_or_locate(botapp_projectstepmodel_12)

    botapp_projectstepmodel_13 = WaitProjectStepModel()
    botapp_projectstepmodel_13.display_name = 'Oda normál viteldíj beállítása'
    botapp_projectstepmodel_13.order_index = 13
    botapp_projectstepmodel_13.action_type = 'clickAndWait'
    botapp_projectstepmodel_13.value = '1.0'
    botapp_projectstepmodel_13.html_query = '#flight-FR\x07e 8415\x07e \x10 \x07e \x07e BUD\x07e 09\x02f 09\x02f 2017\x10 20\x03a 20\x07e CRL\x07e 09\x02f 09\x02f 2017\x10 22\x03a 25\x07e > div > div.flight-header__min-price.hide-mobile'
    botapp_projectstepmodel_13.variable = False
    botapp_projectstepmodel_13.project = botapp_projectmodel_1
    botapp_projectstepmodel_13 = importer.save_or_locate(botapp_projectstepmodel_13)

    botapp_projectstepmodel_14 = WaitProjectStepModel()
    botapp_projectstepmodel_14.display_name = 'Vissza "összegtől" gomb megnyomása'
    botapp_projectstepmodel_14.order_index = 14
    botapp_projectstepmodel_14.action_type = 'clickAndWait'
    botapp_projectstepmodel_14.value = '1.0'
    botapp_projectstepmodel_14.html_query = '#flight-FR\x07e 8416\x07e \x10 \x07e \x07e CRL\x07e 10\x02f 14\x02f 2017\x10 17\x03a 55\x07e BUD\x07e 10\x02f 14\x02f 2017\x10 19\x03a 55\x07e > div > div.flight-header__min-price.hide-mobile > flights-table-price > div > div.core-btn-primary'
    botapp_projectstepmodel_14.variable = False
    botapp_projectstepmodel_14.project = botapp_projectmodel_1
    botapp_projectstepmodel_14 = importer.save_or_locate(botapp_projectstepmodel_14)

    botapp_projectstepmodel_15 = WaitProjectStepModel()
    botapp_projectstepmodel_15.display_name = 'Folytatás gombra kattintés'
    botapp_projectstepmodel_15.order_index = 15
    botapp_projectstepmodel_15.action_type = 'clickAndWait'
    botapp_projectstepmodel_15.value = '1.0'
    botapp_projectstepmodel_15.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-cnt > button'
    botapp_projectstepmodel_15.variable = False
    botapp_projectstepmodel_15.project = botapp_projectmodel_1
    botapp_projectstepmodel_15 = importer.save_or_locate(botapp_projectstepmodel_15)

    botapp_projectstepmodel_16 = WaitProjectStepModel()
    botapp_projectstepmodel_16.display_name = 'Csomag hozzáadása'
    botapp_projectstepmodel_16.order_index = 17
    botapp_projectstepmodel_16.action_type = 'clickAndWait'
    botapp_projectstepmodel_16.value = '1.0'
    botapp_projectstepmodel_16.html_query = 'body > div.FR > main > div.body-section > extras-panels > section > article > leaderboard > div > extras-card:nth-child(3) > ng-include > div > div.action > button.core-btn-primary.add'
    botapp_projectstepmodel_16.variable = False
    botapp_projectstepmodel_16.project = botapp_projectmodel_1
    botapp_projectstepmodel_16 = importer.save_or_locate(botapp_projectstepmodel_16)

    botapp_projectstepmodel_17 = WaitProjectStepModel()
    botapp_projectstepmodel_17.display_name = 'Csomag hozzáadása felugró'
    botapp_projectstepmodel_17.order_index = 18
    botapp_projectstepmodel_17.action_type = 'clickAndWait'
    botapp_projectstepmodel_17.value = '1.0'
    botapp_projectstepmodel_17.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div'
    botapp_projectstepmodel_17.variable = False
    botapp_projectstepmodel_17.project = botapp_projectmodel_1
    botapp_projectstepmodel_17 = importer.save_or_locate(botapp_projectstepmodel_17)

    botapp_projectstepmodel_18 = WaitProjectStepModel()
    botapp_projectstepmodel_18.display_name = 'Összeg mentése'
    botapp_projectstepmodel_18.order_index = 16
    botapp_projectstepmodel_18.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_18.value = 'lowest_price'
    botapp_projectstepmodel_18.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-total > trips-breakdown > div.breakdown > div > div.price-number.notranslate.short-price'
    botapp_projectstepmodel_18.variable = True
    botapp_projectstepmodel_18.project = botapp_projectmodel_1
    botapp_projectstepmodel_18 = importer.save_or_locate(botapp_projectstepmodel_18)

    botapp_projectstepmodel_19 = WaitProjectStepModel()
    botapp_projectstepmodel_19.display_name = 'Kisebb csomag súly'
    botapp_projectstepmodel_19.order_index = 19
    botapp_projectstepmodel_19.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_19.value = 'lower_bag_weight'
    botapp_projectstepmodel_19.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(1) > span.bag-item__weight'
    botapp_projectstepmodel_19.variable = True
    botapp_projectstepmodel_19.project = botapp_projectmodel_1
    botapp_projectstepmodel_19 = importer.save_or_locate(botapp_projectstepmodel_19)

    botapp_projectstepmodel_20 = WaitProjectStepModel()
    botapp_projectstepmodel_20.display_name = 'Kisebb csomag ár'
    botapp_projectstepmodel_20.order_index = 20
    botapp_projectstepmodel_20.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_20.value = 'lower_bag_price'
    botapp_projectstepmodel_20.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_20.variable = True
    botapp_projectstepmodel_20.project = botapp_projectmodel_1
    botapp_projectstepmodel_20 = importer.save_or_locate(botapp_projectstepmodel_20)

    botapp_projectstepmodel_21 = WaitProjectStepModel()
    botapp_projectstepmodel_21.display_name = 'Nagyobb csomag súly'
    botapp_projectstepmodel_21.order_index = 21
    botapp_projectstepmodel_21.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_21.value = 'larger_bag_weight'
    botapp_projectstepmodel_21.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__weight'
    botapp_projectstepmodel_21.variable = True
    botapp_projectstepmodel_21.project = botapp_projectmodel_1
    botapp_projectstepmodel_21 = importer.save_or_locate(botapp_projectstepmodel_21)

    botapp_projectstepmodel_22 = WaitProjectStepModel()
    botapp_projectstepmodel_22.display_name = 'Nagyobb csomag ár'
    botapp_projectstepmodel_22.order_index = 22
    botapp_projectstepmodel_22.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_22.value = 'larger_bag_price'
    botapp_projectstepmodel_22.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_22.variable = True
    botapp_projectstepmodel_22.project = botapp_projectmodel_1
    botapp_projectstepmodel_22 = importer.save_or_locate(botapp_projectstepmodel_22)

    botapp_projectstepmodel_23 = WaitProjectStepModel()
    botapp_projectstepmodel_23.display_name = 'Indulási állomás felugró megnyitása'
    botapp_projectstepmodel_23.order_index = 1
    botapp_projectstepmodel_23.action_type = 'clickAndWait'
    botapp_projectstepmodel_23.value = '1.0'
    botapp_projectstepmodel_23.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_23.variable = False
    botapp_projectstepmodel_23.project = botapp_projectmodel_2
    botapp_projectstepmodel_23 = importer.save_or_locate(botapp_projectstepmodel_23)

    botapp_projectstepmodel_24 = WaitProjectStepModel()
    botapp_projectstepmodel_24.display_name = 'Indulási ország kiválasztása'
    botapp_projectstepmodel_24.order_index = 2
    botapp_projectstepmodel_24.action_type = 'clickAndWait'
    botapp_projectstepmodel_24.value = '1.0'
    botapp_projectstepmodel_24.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div.core-list-item.core-list-item-rounded.clicked'
    botapp_projectstepmodel_24.variable = False
    botapp_projectstepmodel_24.project = botapp_projectmodel_2
    botapp_projectstepmodel_24 = importer.save_or_locate(botapp_projectstepmodel_24)

    botapp_projectstepmodel_25 = WaitProjectStepModel()
    botapp_projectstepmodel_25.display_name = 'Indulási repülőtér kiválasztása'
    botapp_projectstepmodel_25.order_index = 3
    botapp_projectstepmodel_25.action_type = 'clickAndWait'
    botapp_projectstepmodel_25.value = '1.0'
    botapp_projectstepmodel_25.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div.core-list-item.core-list-item-rounded.clicked > span'
    botapp_projectstepmodel_25.variable = False
    botapp_projectstepmodel_25.project = botapp_projectmodel_2
    botapp_projectstepmodel_25 = importer.save_or_locate(botapp_projectstepmodel_25)

    botapp_projectstepmodel_26 = WaitProjectStepModel()
    botapp_projectstepmodel_26.display_name = 'Érkezési állomás felugró megnyitása'
    botapp_projectstepmodel_26.order_index = 4
    botapp_projectstepmodel_26.action_type = 'clickAndWait'
    botapp_projectstepmodel_26.value = '1.0'
    botapp_projectstepmodel_26.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_26.variable = False
    botapp_projectstepmodel_26.project = botapp_projectmodel_2
    botapp_projectstepmodel_26 = importer.save_or_locate(botapp_projectstepmodel_26)

    botapp_projectstepmodel_27 = WaitProjectStepModel()
    botapp_projectstepmodel_27.display_name = 'Érkezési ország kiválasztása'
    botapp_projectstepmodel_27.order_index = 5
    botapp_projectstepmodel_27.action_type = 'clickAndWait'
    botapp_projectstepmodel_27.value = '1.0'
    botapp_projectstepmodel_27.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div:nth-child(4)'
    botapp_projectstepmodel_27.variable = False
    botapp_projectstepmodel_27.project = botapp_projectmodel_2
    botapp_projectstepmodel_27 = importer.save_or_locate(botapp_projectstepmodel_27)

    botapp_projectstepmodel_28 = WaitProjectStepModel()
    botapp_projectstepmodel_28.display_name = 'Érkezési repülőtér kiválasztása'
    botapp_projectstepmodel_28.order_index = 6
    botapp_projectstepmodel_28.action_type = 'clickAndWait'
    botapp_projectstepmodel_28.value = '1.0'
    botapp_projectstepmodel_28.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div:nth-child(3) > span'
    botapp_projectstepmodel_28.variable = False
    botapp_projectstepmodel_28.project = botapp_projectmodel_2
    botapp_projectstepmodel_28 = importer.save_or_locate(botapp_projectstepmodel_28)

    botapp_projectstepmodel_29 = WaitProjectStepModel()
    botapp_projectstepmodel_29.display_name = 'Utasok felugró kiválasztása'
    botapp_projectstepmodel_29.order_index = 7
    botapp_projectstepmodel_29.action_type = 'clickAndWait'
    botapp_projectstepmodel_29.value = '1.0'
    botapp_projectstepmodel_29.html_query = '#row-dates-pax > div.col-passengers > div:nth-child(2) > div:nth-child(5) > div > div.value'
    botapp_projectstepmodel_29.variable = False
    botapp_projectstepmodel_29.project = botapp_projectmodel_2
    botapp_projectstepmodel_29 = importer.save_or_locate(botapp_projectstepmodel_29)

    botapp_projectstepmodel_30 = WaitProjectStepModel()
    botapp_projectstepmodel_30.display_name = '1 (+1) utas hozzáadása'
    botapp_projectstepmodel_30.order_index = 8
    botapp_projectstepmodel_30.action_type = 'clickAndWait'
    botapp_projectstepmodel_30.value = '1.0'
    botapp_projectstepmodel_30.html_query = '#row-dates-pax > div.col-passengers > div.popup-passenger-input.opened > div > div > div.content > popup-content > div:nth-child(6) > div > div.details-controls > core-inc-dec > button.core-btn.inc.core-btn-wrap'
    botapp_projectstepmodel_30.variable = False
    botapp_projectstepmodel_30.project = botapp_projectmodel_2
    botapp_projectstepmodel_30 = importer.save_or_locate(botapp_projectstepmodel_30)

    botapp_projectstepmodel_31 = WaitProjectStepModel()
    botapp_projectstepmodel_31.display_name = 'Indulási időpont kiválasztása'
    botapp_projectstepmodel_31.order_index = 9
    botapp_projectstepmodel_31.action_type = 'clickAndWait'
    botapp_projectstepmodel_31.value = '1.0'
    botapp_projectstepmodel_31.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required > div.focused > div'
    botapp_projectstepmodel_31.variable = False
    botapp_projectstepmodel_31.project = botapp_projectmodel_2
    botapp_projectstepmodel_31 = importer.save_or_locate(botapp_projectstepmodel_31)

    botapp_projectstepmodel_32 = WaitProjectStepModel()
    botapp_projectstepmodel_32.display_name = 'Visszaút kiválasztása'
    botapp_projectstepmodel_32.order_index = 10
    botapp_projectstepmodel_32.action_type = 'clickAndWait'
    botapp_projectstepmodel_32.value = '1.0'
    botapp_projectstepmodel_32.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.core-date-range.popup-start-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.six-rows.scrollable > ul > li:nth-child(1) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_32.variable = False
    botapp_projectstepmodel_32.project = botapp_projectmodel_2
    botapp_projectstepmodel_32 = importer.save_or_locate(botapp_projectstepmodel_32)

    botapp_projectstepmodel_33 = WaitProjectStepModel()
    botapp_projectstepmodel_33.display_name = 'Indulásra kattintás'
    botapp_projectstepmodel_33.order_index = 11
    botapp_projectstepmodel_33.action_type = 'clickAndWait'
    botapp_projectstepmodel_33.value = '1.0'
    botapp_projectstepmodel_33.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-to > div > div.core-date-range.popup-end-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.scrollable.six-rows > ul > li:nth-child(2) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_33.variable = False
    botapp_projectstepmodel_33.project = botapp_projectmodel_2
    botapp_projectstepmodel_33 = importer.save_or_locate(botapp_projectstepmodel_33)

    botapp_projectstepmodel_34 = WaitProjectStepModel()
    botapp_projectstepmodel_34.display_name = 'Oda "összegtől" gomb megnyomása'
    botapp_projectstepmodel_34.order_index = 12
    botapp_projectstepmodel_34.action_type = 'clickAndWait'
    botapp_projectstepmodel_34.value = '1.0'
    botapp_projectstepmodel_34.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-right > button:nth-child(2)'
    botapp_projectstepmodel_34.variable = False
    botapp_projectstepmodel_34.project = botapp_projectmodel_2
    botapp_projectstepmodel_34 = importer.save_or_locate(botapp_projectstepmodel_34)

    botapp_projectstepmodel_35 = WaitProjectStepModel()
    botapp_projectstepmodel_35.display_name = 'Oda normál viteldíj beállítása'
    botapp_projectstepmodel_35.order_index = 13
    botapp_projectstepmodel_35.action_type = 'clickAndWait'
    botapp_projectstepmodel_35.value = '1.0'
    botapp_projectstepmodel_35.html_query = '#flight-FR\x07e 8415\x07e \x10 \x07e \x07e BUD\x07e 09\x02f 09\x02f 2017\x10 20\x03a 20\x07e CRL\x07e 09\x02f 09\x02f 2017\x10 22\x03a 25\x07e > div > div.flight-header__min-price.hide-mobile'
    botapp_projectstepmodel_35.variable = False
    botapp_projectstepmodel_35.project = botapp_projectmodel_2
    botapp_projectstepmodel_35 = importer.save_or_locate(botapp_projectstepmodel_35)

    botapp_projectstepmodel_36 = WaitProjectStepModel()
    botapp_projectstepmodel_36.display_name = 'Vissza "összegtől" gomb megnyomása'
    botapp_projectstepmodel_36.order_index = 14
    botapp_projectstepmodel_36.action_type = 'clickAndWait'
    botapp_projectstepmodel_36.value = '1.0'
    botapp_projectstepmodel_36.html_query = '#flight-FR\x07e 8416\x07e \x10 \x07e \x07e CRL\x07e 10\x02f 14\x02f 2017\x10 17\x03a 55\x07e BUD\x07e 10\x02f 14\x02f 2017\x10 19\x03a 55\x07e > div > div.flight-header__min-price.hide-mobile > flights-table-price > div > div.core-btn-primary'
    botapp_projectstepmodel_36.variable = False
    botapp_projectstepmodel_36.project = botapp_projectmodel_2
    botapp_projectstepmodel_36 = importer.save_or_locate(botapp_projectstepmodel_36)

    botapp_projectstepmodel_37 = WaitProjectStepModel()
    botapp_projectstepmodel_37.display_name = 'Folytatás gombra kattintés'
    botapp_projectstepmodel_37.order_index = 15
    botapp_projectstepmodel_37.action_type = 'clickAndWait'
    botapp_projectstepmodel_37.value = '1.0'
    botapp_projectstepmodel_37.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-cnt > button'
    botapp_projectstepmodel_37.variable = False
    botapp_projectstepmodel_37.project = botapp_projectmodel_2
    botapp_projectstepmodel_37 = importer.save_or_locate(botapp_projectstepmodel_37)

    botapp_projectstepmodel_38 = WaitProjectStepModel()
    botapp_projectstepmodel_38.display_name = 'Csomag hozzáadása'
    botapp_projectstepmodel_38.order_index = 17
    botapp_projectstepmodel_38.action_type = 'clickAndWait'
    botapp_projectstepmodel_38.value = '1.0'
    botapp_projectstepmodel_38.html_query = 'body > div.FR > main > div.body-section > extras-panels > section > article > leaderboard > div > extras-card:nth-child(3) > ng-include > div > div.action > button.core-btn-primary.add'
    botapp_projectstepmodel_38.variable = False
    botapp_projectstepmodel_38.project = botapp_projectmodel_2
    botapp_projectstepmodel_38 = importer.save_or_locate(botapp_projectstepmodel_38)

    botapp_projectstepmodel_39 = WaitProjectStepModel()
    botapp_projectstepmodel_39.display_name = 'Csomag hozzáadása felugró'
    botapp_projectstepmodel_39.order_index = 18
    botapp_projectstepmodel_39.action_type = 'clickAndWait'
    botapp_projectstepmodel_39.value = '1.0'
    botapp_projectstepmodel_39.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div'
    botapp_projectstepmodel_39.variable = False
    botapp_projectstepmodel_39.project = botapp_projectmodel_2
    botapp_projectstepmodel_39 = importer.save_or_locate(botapp_projectstepmodel_39)

    botapp_projectstepmodel_40 = WaitProjectStepModel()
    botapp_projectstepmodel_40.display_name = 'Összeg mentése'
    botapp_projectstepmodel_40.order_index = 16
    botapp_projectstepmodel_40.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_40.value = 'lowest_price'
    botapp_projectstepmodel_40.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-total > trips-breakdown > div.breakdown > div > div.price-number.notranslate.short-price'
    botapp_projectstepmodel_40.variable = True
    botapp_projectstepmodel_40.project = botapp_projectmodel_2
    botapp_projectstepmodel_40 = importer.save_or_locate(botapp_projectstepmodel_40)

    botapp_projectstepmodel_41 = WaitProjectStepModel()
    botapp_projectstepmodel_41.display_name = 'Kisebb csomag súly'
    botapp_projectstepmodel_41.order_index = 19
    botapp_projectstepmodel_41.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_41.value = 'lower_bag_weight'
    botapp_projectstepmodel_41.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(1) > span.bag-item__weight'
    botapp_projectstepmodel_41.variable = True
    botapp_projectstepmodel_41.project = botapp_projectmodel_2
    botapp_projectstepmodel_41 = importer.save_or_locate(botapp_projectstepmodel_41)

    botapp_projectstepmodel_42 = WaitProjectStepModel()
    botapp_projectstepmodel_42.display_name = 'Kisebb csomag ár'
    botapp_projectstepmodel_42.order_index = 20
    botapp_projectstepmodel_42.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_42.value = 'lower_bag_price'
    botapp_projectstepmodel_42.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_42.variable = True
    botapp_projectstepmodel_42.project = botapp_projectmodel_2
    botapp_projectstepmodel_42 = importer.save_or_locate(botapp_projectstepmodel_42)

    botapp_projectstepmodel_43 = WaitProjectStepModel()
    botapp_projectstepmodel_43.display_name = 'Nagyobb csomag súly'
    botapp_projectstepmodel_43.order_index = 21
    botapp_projectstepmodel_43.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_43.value = 'larger_bag_weight'
    botapp_projectstepmodel_43.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__weight'
    botapp_projectstepmodel_43.variable = True
    botapp_projectstepmodel_43.project = botapp_projectmodel_2
    botapp_projectstepmodel_43 = importer.save_or_locate(botapp_projectstepmodel_43)

    botapp_projectstepmodel_44 = WaitProjectStepModel()
    botapp_projectstepmodel_44.display_name = 'Nagyobb csomag ár'
    botapp_projectstepmodel_44.order_index = 22
    botapp_projectstepmodel_44.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_44.value = 'larger_bag_price'
    botapp_projectstepmodel_44.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_44.variable = True
    botapp_projectstepmodel_44.project = botapp_projectmodel_2
    botapp_projectstepmodel_44 = importer.save_or_locate(botapp_projectstepmodel_44)

    # Processing model: botapp.models.WriteProjectStepModel

    from botapp.models import WriteProjectStepModel

    botapp_projectstepmodel_1 = WriteProjectStepModel()
    botapp_projectstepmodel_1.display_name = 'Indulási állomás felugró megnyitása'
    botapp_projectstepmodel_1.order_index = 1
    botapp_projectstepmodel_1.action_type = 'clickAndWait'
    botapp_projectstepmodel_1.value = '1.0'
    botapp_projectstepmodel_1.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_1.variable = False
    botapp_projectstepmodel_1.project = botapp_projectmodel_1
    botapp_projectstepmodel_1 = importer.save_or_locate(botapp_projectstepmodel_1)

    botapp_projectstepmodel_2 = WriteProjectStepModel()
    botapp_projectstepmodel_2.display_name = 'Indulási ország kiválasztása'
    botapp_projectstepmodel_2.order_index = 2
    botapp_projectstepmodel_2.action_type = 'clickAndWait'
    botapp_projectstepmodel_2.value = '1.0'
    botapp_projectstepmodel_2.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div.core-list-item.core-list-item-rounded.clicked'
    botapp_projectstepmodel_2.variable = False
    botapp_projectstepmodel_2.project = botapp_projectmodel_1
    botapp_projectstepmodel_2 = importer.save_or_locate(botapp_projectstepmodel_2)

    botapp_projectstepmodel_3 = WriteProjectStepModel()
    botapp_projectstepmodel_3.display_name = 'Indulási repülőtér kiválasztása'
    botapp_projectstepmodel_3.order_index = 3
    botapp_projectstepmodel_3.action_type = 'clickAndWait'
    botapp_projectstepmodel_3.value = '1.0'
    botapp_projectstepmodel_3.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div.core-list-item.core-list-item-rounded.clicked > span'
    botapp_projectstepmodel_3.variable = False
    botapp_projectstepmodel_3.project = botapp_projectmodel_1
    botapp_projectstepmodel_3 = importer.save_or_locate(botapp_projectstepmodel_3)

    botapp_projectstepmodel_4 = WriteProjectStepModel()
    botapp_projectstepmodel_4.display_name = 'Érkezési állomás felugró megnyitása'
    botapp_projectstepmodel_4.order_index = 4
    botapp_projectstepmodel_4.action_type = 'clickAndWait'
    botapp_projectstepmodel_4.value = '1.0'
    botapp_projectstepmodel_4.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_4.variable = False
    botapp_projectstepmodel_4.project = botapp_projectmodel_1
    botapp_projectstepmodel_4 = importer.save_or_locate(botapp_projectstepmodel_4)

    botapp_projectstepmodel_5 = WriteProjectStepModel()
    botapp_projectstepmodel_5.display_name = 'Érkezési ország kiválasztása'
    botapp_projectstepmodel_5.order_index = 5
    botapp_projectstepmodel_5.action_type = 'clickAndWait'
    botapp_projectstepmodel_5.value = '1.0'
    botapp_projectstepmodel_5.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div:nth-child(4)'
    botapp_projectstepmodel_5.variable = False
    botapp_projectstepmodel_5.project = botapp_projectmodel_1
    botapp_projectstepmodel_5 = importer.save_or_locate(botapp_projectstepmodel_5)

    botapp_projectstepmodel_6 = WriteProjectStepModel()
    botapp_projectstepmodel_6.display_name = 'Érkezési repülőtér kiválasztása'
    botapp_projectstepmodel_6.order_index = 6
    botapp_projectstepmodel_6.action_type = 'clickAndWait'
    botapp_projectstepmodel_6.value = '1.0'
    botapp_projectstepmodel_6.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div:nth-child(3) > span'
    botapp_projectstepmodel_6.variable = False
    botapp_projectstepmodel_6.project = botapp_projectmodel_1
    botapp_projectstepmodel_6 = importer.save_or_locate(botapp_projectstepmodel_6)

    botapp_projectstepmodel_7 = WriteProjectStepModel()
    botapp_projectstepmodel_7.display_name = 'Utasok felugró kiválasztása'
    botapp_projectstepmodel_7.order_index = 7
    botapp_projectstepmodel_7.action_type = 'clickAndWait'
    botapp_projectstepmodel_7.value = '1.0'
    botapp_projectstepmodel_7.html_query = '#row-dates-pax > div.col-passengers > div:nth-child(2) > div:nth-child(5) > div > div.value'
    botapp_projectstepmodel_7.variable = False
    botapp_projectstepmodel_7.project = botapp_projectmodel_1
    botapp_projectstepmodel_7 = importer.save_or_locate(botapp_projectstepmodel_7)

    botapp_projectstepmodel_8 = WriteProjectStepModel()
    botapp_projectstepmodel_8.display_name = '1 (+1) utas hozzáadása'
    botapp_projectstepmodel_8.order_index = 8
    botapp_projectstepmodel_8.action_type = 'clickAndWait'
    botapp_projectstepmodel_8.value = '1.0'
    botapp_projectstepmodel_8.html_query = '#row-dates-pax > div.col-passengers > div.popup-passenger-input.opened > div > div > div.content > popup-content > div:nth-child(6) > div > div.details-controls > core-inc-dec > button.core-btn.inc.core-btn-wrap'
    botapp_projectstepmodel_8.variable = False
    botapp_projectstepmodel_8.project = botapp_projectmodel_1
    botapp_projectstepmodel_8 = importer.save_or_locate(botapp_projectstepmodel_8)

    botapp_projectstepmodel_9 = WriteProjectStepModel()
    botapp_projectstepmodel_9.display_name = 'Indulási időpont kiválasztása'
    botapp_projectstepmodel_9.order_index = 9
    botapp_projectstepmodel_9.action_type = 'clickAndWait'
    botapp_projectstepmodel_9.value = '1.0'
    botapp_projectstepmodel_9.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required > div.focused > div'
    botapp_projectstepmodel_9.variable = False
    botapp_projectstepmodel_9.project = botapp_projectmodel_1
    botapp_projectstepmodel_9 = importer.save_or_locate(botapp_projectstepmodel_9)

    botapp_projectstepmodel_10 = WriteProjectStepModel()
    botapp_projectstepmodel_10.display_name = 'Visszaút kiválasztása'
    botapp_projectstepmodel_10.order_index = 10
    botapp_projectstepmodel_10.action_type = 'clickAndWait'
    botapp_projectstepmodel_10.value = '1.0'
    botapp_projectstepmodel_10.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.core-date-range.popup-start-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.six-rows.scrollable > ul > li:nth-child(1) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_10.variable = False
    botapp_projectstepmodel_10.project = botapp_projectmodel_1
    botapp_projectstepmodel_10 = importer.save_or_locate(botapp_projectstepmodel_10)

    botapp_projectstepmodel_11 = WriteProjectStepModel()
    botapp_projectstepmodel_11.display_name = 'Indulásra kattintás'
    botapp_projectstepmodel_11.order_index = 11
    botapp_projectstepmodel_11.action_type = 'clickAndWait'
    botapp_projectstepmodel_11.value = '1.0'
    botapp_projectstepmodel_11.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-to > div > div.core-date-range.popup-end-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.scrollable.six-rows > ul > li:nth-child(2) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_11.variable = False
    botapp_projectstepmodel_11.project = botapp_projectmodel_1
    botapp_projectstepmodel_11 = importer.save_or_locate(botapp_projectstepmodel_11)

    botapp_projectstepmodel_12 = WriteProjectStepModel()
    botapp_projectstepmodel_12.display_name = 'Oda "összegtől" gomb megnyomása'
    botapp_projectstepmodel_12.order_index = 12
    botapp_projectstepmodel_12.action_type = 'clickAndWait'
    botapp_projectstepmodel_12.value = '1.0'
    botapp_projectstepmodel_12.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-right > button:nth-child(2)'
    botapp_projectstepmodel_12.variable = False
    botapp_projectstepmodel_12.project = botapp_projectmodel_1
    botapp_projectstepmodel_12 = importer.save_or_locate(botapp_projectstepmodel_12)

    botapp_projectstepmodel_13 = WriteProjectStepModel()
    botapp_projectstepmodel_13.display_name = 'Oda normál viteldíj beállítása'
    botapp_projectstepmodel_13.order_index = 13
    botapp_projectstepmodel_13.action_type = 'clickAndWait'
    botapp_projectstepmodel_13.value = '1.0'
    botapp_projectstepmodel_13.html_query = '#flight-FR\x07e 8415\x07e \x10 \x07e \x07e BUD\x07e 09\x02f 09\x02f 2017\x10 20\x03a 20\x07e CRL\x07e 09\x02f 09\x02f 2017\x10 22\x03a 25\x07e > div > div.flight-header__min-price.hide-mobile'
    botapp_projectstepmodel_13.variable = False
    botapp_projectstepmodel_13.project = botapp_projectmodel_1
    botapp_projectstepmodel_13 = importer.save_or_locate(botapp_projectstepmodel_13)

    botapp_projectstepmodel_14 = WriteProjectStepModel()
    botapp_projectstepmodel_14.display_name = 'Vissza "összegtől" gomb megnyomása'
    botapp_projectstepmodel_14.order_index = 14
    botapp_projectstepmodel_14.action_type = 'clickAndWait'
    botapp_projectstepmodel_14.value = '1.0'
    botapp_projectstepmodel_14.html_query = '#flight-FR\x07e 8416\x07e \x10 \x07e \x07e CRL\x07e 10\x02f 14\x02f 2017\x10 17\x03a 55\x07e BUD\x07e 10\x02f 14\x02f 2017\x10 19\x03a 55\x07e > div > div.flight-header__min-price.hide-mobile > flights-table-price > div > div.core-btn-primary'
    botapp_projectstepmodel_14.variable = False
    botapp_projectstepmodel_14.project = botapp_projectmodel_1
    botapp_projectstepmodel_14 = importer.save_or_locate(botapp_projectstepmodel_14)

    botapp_projectstepmodel_15 = WriteProjectStepModel()
    botapp_projectstepmodel_15.display_name = 'Folytatás gombra kattintés'
    botapp_projectstepmodel_15.order_index = 15
    botapp_projectstepmodel_15.action_type = 'clickAndWait'
    botapp_projectstepmodel_15.value = '1.0'
    botapp_projectstepmodel_15.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-cnt > button'
    botapp_projectstepmodel_15.variable = False
    botapp_projectstepmodel_15.project = botapp_projectmodel_1
    botapp_projectstepmodel_15 = importer.save_or_locate(botapp_projectstepmodel_15)

    botapp_projectstepmodel_16 = WriteProjectStepModel()
    botapp_projectstepmodel_16.display_name = 'Csomag hozzáadása'
    botapp_projectstepmodel_16.order_index = 17
    botapp_projectstepmodel_16.action_type = 'clickAndWait'
    botapp_projectstepmodel_16.value = '1.0'
    botapp_projectstepmodel_16.html_query = 'body > div.FR > main > div.body-section > extras-panels > section > article > leaderboard > div > extras-card:nth-child(3) > ng-include > div > div.action > button.core-btn-primary.add'
    botapp_projectstepmodel_16.variable = False
    botapp_projectstepmodel_16.project = botapp_projectmodel_1
    botapp_projectstepmodel_16 = importer.save_or_locate(botapp_projectstepmodel_16)

    botapp_projectstepmodel_17 = WriteProjectStepModel()
    botapp_projectstepmodel_17.display_name = 'Csomag hozzáadása felugró'
    botapp_projectstepmodel_17.order_index = 18
    botapp_projectstepmodel_17.action_type = 'clickAndWait'
    botapp_projectstepmodel_17.value = '1.0'
    botapp_projectstepmodel_17.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div'
    botapp_projectstepmodel_17.variable = False
    botapp_projectstepmodel_17.project = botapp_projectmodel_1
    botapp_projectstepmodel_17 = importer.save_or_locate(botapp_projectstepmodel_17)

    botapp_projectstepmodel_18 = WriteProjectStepModel()
    botapp_projectstepmodel_18.display_name = 'Összeg mentése'
    botapp_projectstepmodel_18.order_index = 16
    botapp_projectstepmodel_18.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_18.value = 'lowest_price'
    botapp_projectstepmodel_18.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-total > trips-breakdown > div.breakdown > div > div.price-number.notranslate.short-price'
    botapp_projectstepmodel_18.variable = True
    botapp_projectstepmodel_18.project = botapp_projectmodel_1
    botapp_projectstepmodel_18 = importer.save_or_locate(botapp_projectstepmodel_18)

    botapp_projectstepmodel_19 = WriteProjectStepModel()
    botapp_projectstepmodel_19.display_name = 'Kisebb csomag súly'
    botapp_projectstepmodel_19.order_index = 19
    botapp_projectstepmodel_19.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_19.value = 'lower_bag_weight'
    botapp_projectstepmodel_19.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(1) > span.bag-item__weight'
    botapp_projectstepmodel_19.variable = True
    botapp_projectstepmodel_19.project = botapp_projectmodel_1
    botapp_projectstepmodel_19 = importer.save_or_locate(botapp_projectstepmodel_19)

    botapp_projectstepmodel_20 = WriteProjectStepModel()
    botapp_projectstepmodel_20.display_name = 'Kisebb csomag ár'
    botapp_projectstepmodel_20.order_index = 20
    botapp_projectstepmodel_20.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_20.value = 'lower_bag_price'
    botapp_projectstepmodel_20.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_20.variable = True
    botapp_projectstepmodel_20.project = botapp_projectmodel_1
    botapp_projectstepmodel_20 = importer.save_or_locate(botapp_projectstepmodel_20)

    botapp_projectstepmodel_21 = WriteProjectStepModel()
    botapp_projectstepmodel_21.display_name = 'Nagyobb csomag súly'
    botapp_projectstepmodel_21.order_index = 21
    botapp_projectstepmodel_21.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_21.value = 'larger_bag_weight'
    botapp_projectstepmodel_21.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__weight'
    botapp_projectstepmodel_21.variable = True
    botapp_projectstepmodel_21.project = botapp_projectmodel_1
    botapp_projectstepmodel_21 = importer.save_or_locate(botapp_projectstepmodel_21)

    botapp_projectstepmodel_22 = WriteProjectStepModel()
    botapp_projectstepmodel_22.display_name = 'Nagyobb csomag ár'
    botapp_projectstepmodel_22.order_index = 22
    botapp_projectstepmodel_22.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_22.value = 'larger_bag_price'
    botapp_projectstepmodel_22.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_22.variable = True
    botapp_projectstepmodel_22.project = botapp_projectmodel_1
    botapp_projectstepmodel_22 = importer.save_or_locate(botapp_projectstepmodel_22)

    botapp_projectstepmodel_23 = WriteProjectStepModel()
    botapp_projectstepmodel_23.display_name = 'Indulási állomás felugró megnyitása'
    botapp_projectstepmodel_23.order_index = 1
    botapp_projectstepmodel_23.action_type = 'clickAndWait'
    botapp_projectstepmodel_23.value = '1.0'
    botapp_projectstepmodel_23.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_23.variable = False
    botapp_projectstepmodel_23.project = botapp_projectmodel_2
    botapp_projectstepmodel_23 = importer.save_or_locate(botapp_projectstepmodel_23)

    botapp_projectstepmodel_24 = WriteProjectStepModel()
    botapp_projectstepmodel_24.display_name = 'Indulási ország kiválasztása'
    botapp_projectstepmodel_24.order_index = 2
    botapp_projectstepmodel_24.action_type = 'clickAndWait'
    botapp_projectstepmodel_24.value = '1.0'
    botapp_projectstepmodel_24.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div.core-list-item.core-list-item-rounded.clicked'
    botapp_projectstepmodel_24.variable = False
    botapp_projectstepmodel_24.project = botapp_projectmodel_2
    botapp_projectstepmodel_24 = importer.save_or_locate(botapp_projectstepmodel_24)

    botapp_projectstepmodel_25 = WriteProjectStepModel()
    botapp_projectstepmodel_25.display_name = 'Indulási repülőtér kiválasztása'
    botapp_projectstepmodel_25.order_index = 3
    botapp_projectstepmodel_25.action_type = 'clickAndWait'
    botapp_projectstepmodel_25.value = '1.0'
    botapp_projectstepmodel_25.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div.core-list-item.core-list-item-rounded.clicked > span'
    botapp_projectstepmodel_25.variable = False
    botapp_projectstepmodel_25.project = botapp_projectmodel_2
    botapp_projectstepmodel_25 = importer.save_or_locate(botapp_projectstepmodel_25)

    botapp_projectstepmodel_26 = WriteProjectStepModel()
    botapp_projectstepmodel_26.display_name = 'Érkezési állomás felugró megnyitása'
    botapp_projectstepmodel_26.order_index = 4
    botapp_projectstepmodel_26.action_type = 'clickAndWait'
    botapp_projectstepmodel_26.value = '1.0'
    botapp_projectstepmodel_26.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_26.variable = False
    botapp_projectstepmodel_26.project = botapp_projectmodel_2
    botapp_projectstepmodel_26 = importer.save_or_locate(botapp_projectstepmodel_26)

    botapp_projectstepmodel_27 = WriteProjectStepModel()
    botapp_projectstepmodel_27.display_name = 'Érkezési ország kiválasztása'
    botapp_projectstepmodel_27.order_index = 5
    botapp_projectstepmodel_27.action_type = 'clickAndWait'
    botapp_projectstepmodel_27.value = '1.0'
    botapp_projectstepmodel_27.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div:nth-child(4)'
    botapp_projectstepmodel_27.variable = False
    botapp_projectstepmodel_27.project = botapp_projectmodel_2
    botapp_projectstepmodel_27 = importer.save_or_locate(botapp_projectstepmodel_27)

    botapp_projectstepmodel_28 = WriteProjectStepModel()
    botapp_projectstepmodel_28.display_name = 'Érkezési repülőtér kiválasztása'
    botapp_projectstepmodel_28.order_index = 6
    botapp_projectstepmodel_28.action_type = 'clickAndWait'
    botapp_projectstepmodel_28.value = '1.0'
    botapp_projectstepmodel_28.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div:nth-child(3) > span'
    botapp_projectstepmodel_28.variable = False
    botapp_projectstepmodel_28.project = botapp_projectmodel_2
    botapp_projectstepmodel_28 = importer.save_or_locate(botapp_projectstepmodel_28)

    botapp_projectstepmodel_29 = WriteProjectStepModel()
    botapp_projectstepmodel_29.display_name = 'Utasok felugró kiválasztása'
    botapp_projectstepmodel_29.order_index = 7
    botapp_projectstepmodel_29.action_type = 'clickAndWait'
    botapp_projectstepmodel_29.value = '1.0'
    botapp_projectstepmodel_29.html_query = '#row-dates-pax > div.col-passengers > div:nth-child(2) > div:nth-child(5) > div > div.value'
    botapp_projectstepmodel_29.variable = False
    botapp_projectstepmodel_29.project = botapp_projectmodel_2
    botapp_projectstepmodel_29 = importer.save_or_locate(botapp_projectstepmodel_29)

    botapp_projectstepmodel_30 = WriteProjectStepModel()
    botapp_projectstepmodel_30.display_name = '1 (+1) utas hozzáadása'
    botapp_projectstepmodel_30.order_index = 8
    botapp_projectstepmodel_30.action_type = 'clickAndWait'
    botapp_projectstepmodel_30.value = '1.0'
    botapp_projectstepmodel_30.html_query = '#row-dates-pax > div.col-passengers > div.popup-passenger-input.opened > div > div > div.content > popup-content > div:nth-child(6) > div > div.details-controls > core-inc-dec > button.core-btn.inc.core-btn-wrap'
    botapp_projectstepmodel_30.variable = False
    botapp_projectstepmodel_30.project = botapp_projectmodel_2
    botapp_projectstepmodel_30 = importer.save_or_locate(botapp_projectstepmodel_30)

    botapp_projectstepmodel_31 = WriteProjectStepModel()
    botapp_projectstepmodel_31.display_name = 'Indulási időpont kiválasztása'
    botapp_projectstepmodel_31.order_index = 9
    botapp_projectstepmodel_31.action_type = 'clickAndWait'
    botapp_projectstepmodel_31.value = '1.0'
    botapp_projectstepmodel_31.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required > div.focused > div'
    botapp_projectstepmodel_31.variable = False
    botapp_projectstepmodel_31.project = botapp_projectmodel_2
    botapp_projectstepmodel_31 = importer.save_or_locate(botapp_projectstepmodel_31)

    botapp_projectstepmodel_32 = WriteProjectStepModel()
    botapp_projectstepmodel_32.display_name = 'Visszaút kiválasztása'
    botapp_projectstepmodel_32.order_index = 10
    botapp_projectstepmodel_32.action_type = 'clickAndWait'
    botapp_projectstepmodel_32.value = '1.0'
    botapp_projectstepmodel_32.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.core-date-range.popup-start-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.six-rows.scrollable > ul > li:nth-child(1) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_32.variable = False
    botapp_projectstepmodel_32.project = botapp_projectmodel_2
    botapp_projectstepmodel_32 = importer.save_or_locate(botapp_projectstepmodel_32)

    botapp_projectstepmodel_33 = WriteProjectStepModel()
    botapp_projectstepmodel_33.display_name = 'Indulásra kattintás'
    botapp_projectstepmodel_33.order_index = 11
    botapp_projectstepmodel_33.action_type = 'clickAndWait'
    botapp_projectstepmodel_33.value = '1.0'
    botapp_projectstepmodel_33.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-to > div > div.core-date-range.popup-end-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.scrollable.six-rows > ul > li:nth-child(2) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_33.variable = False
    botapp_projectstepmodel_33.project = botapp_projectmodel_2
    botapp_projectstepmodel_33 = importer.save_or_locate(botapp_projectstepmodel_33)

    botapp_projectstepmodel_34 = WriteProjectStepModel()
    botapp_projectstepmodel_34.display_name = 'Oda "összegtől" gomb megnyomása'
    botapp_projectstepmodel_34.order_index = 12
    botapp_projectstepmodel_34.action_type = 'clickAndWait'
    botapp_projectstepmodel_34.value = '1.0'
    botapp_projectstepmodel_34.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-right > button:nth-child(2)'
    botapp_projectstepmodel_34.variable = False
    botapp_projectstepmodel_34.project = botapp_projectmodel_2
    botapp_projectstepmodel_34 = importer.save_or_locate(botapp_projectstepmodel_34)

    botapp_projectstepmodel_35 = WriteProjectStepModel()
    botapp_projectstepmodel_35.display_name = 'Oda normál viteldíj beállítása'
    botapp_projectstepmodel_35.order_index = 13
    botapp_projectstepmodel_35.action_type = 'clickAndWait'
    botapp_projectstepmodel_35.value = '1.0'
    botapp_projectstepmodel_35.html_query = '#flight-FR\x07e 8415\x07e \x10 \x07e \x07e BUD\x07e 09\x02f 09\x02f 2017\x10 20\x03a 20\x07e CRL\x07e 09\x02f 09\x02f 2017\x10 22\x03a 25\x07e > div > div.flight-header__min-price.hide-mobile'
    botapp_projectstepmodel_35.variable = False
    botapp_projectstepmodel_35.project = botapp_projectmodel_2
    botapp_projectstepmodel_35 = importer.save_or_locate(botapp_projectstepmodel_35)

    botapp_projectstepmodel_36 = WriteProjectStepModel()
    botapp_projectstepmodel_36.display_name = 'Vissza "összegtől" gomb megnyomása'
    botapp_projectstepmodel_36.order_index = 14
    botapp_projectstepmodel_36.action_type = 'clickAndWait'
    botapp_projectstepmodel_36.value = '1.0'
    botapp_projectstepmodel_36.html_query = '#flight-FR\x07e 8416\x07e \x10 \x07e \x07e CRL\x07e 10\x02f 14\x02f 2017\x10 17\x03a 55\x07e BUD\x07e 10\x02f 14\x02f 2017\x10 19\x03a 55\x07e > div > div.flight-header__min-price.hide-mobile > flights-table-price > div > div.core-btn-primary'
    botapp_projectstepmodel_36.variable = False
    botapp_projectstepmodel_36.project = botapp_projectmodel_2
    botapp_projectstepmodel_36 = importer.save_or_locate(botapp_projectstepmodel_36)

    botapp_projectstepmodel_37 = WriteProjectStepModel()
    botapp_projectstepmodel_37.display_name = 'Folytatás gombra kattintés'
    botapp_projectstepmodel_37.order_index = 15
    botapp_projectstepmodel_37.action_type = 'clickAndWait'
    botapp_projectstepmodel_37.value = '1.0'
    botapp_projectstepmodel_37.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-cnt > button'
    botapp_projectstepmodel_37.variable = False
    botapp_projectstepmodel_37.project = botapp_projectmodel_2
    botapp_projectstepmodel_37 = importer.save_or_locate(botapp_projectstepmodel_37)

    botapp_projectstepmodel_38 = WriteProjectStepModel()
    botapp_projectstepmodel_38.display_name = 'Csomag hozzáadása'
    botapp_projectstepmodel_38.order_index = 17
    botapp_projectstepmodel_38.action_type = 'clickAndWait'
    botapp_projectstepmodel_38.value = '1.0'
    botapp_projectstepmodel_38.html_query = 'body > div.FR > main > div.body-section > extras-panels > section > article > leaderboard > div > extras-card:nth-child(3) > ng-include > div > div.action > button.core-btn-primary.add'
    botapp_projectstepmodel_38.variable = False
    botapp_projectstepmodel_38.project = botapp_projectmodel_2
    botapp_projectstepmodel_38 = importer.save_or_locate(botapp_projectstepmodel_38)

    botapp_projectstepmodel_39 = WriteProjectStepModel()
    botapp_projectstepmodel_39.display_name = 'Csomag hozzáadása felugró'
    botapp_projectstepmodel_39.order_index = 18
    botapp_projectstepmodel_39.action_type = 'clickAndWait'
    botapp_projectstepmodel_39.value = '1.0'
    botapp_projectstepmodel_39.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div'
    botapp_projectstepmodel_39.variable = False
    botapp_projectstepmodel_39.project = botapp_projectmodel_2
    botapp_projectstepmodel_39 = importer.save_or_locate(botapp_projectstepmodel_39)

    botapp_projectstepmodel_40 = WriteProjectStepModel()
    botapp_projectstepmodel_40.display_name = 'Összeg mentése'
    botapp_projectstepmodel_40.order_index = 16
    botapp_projectstepmodel_40.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_40.value = 'lowest_price'
    botapp_projectstepmodel_40.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-total > trips-breakdown > div.breakdown > div > div.price-number.notranslate.short-price'
    botapp_projectstepmodel_40.variable = True
    botapp_projectstepmodel_40.project = botapp_projectmodel_2
    botapp_projectstepmodel_40 = importer.save_or_locate(botapp_projectstepmodel_40)

    botapp_projectstepmodel_41 = WriteProjectStepModel()
    botapp_projectstepmodel_41.display_name = 'Kisebb csomag súly'
    botapp_projectstepmodel_41.order_index = 19
    botapp_projectstepmodel_41.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_41.value = 'lower_bag_weight'
    botapp_projectstepmodel_41.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(1) > span.bag-item__weight'
    botapp_projectstepmodel_41.variable = True
    botapp_projectstepmodel_41.project = botapp_projectmodel_2
    botapp_projectstepmodel_41 = importer.save_or_locate(botapp_projectstepmodel_41)

    botapp_projectstepmodel_42 = WriteProjectStepModel()
    botapp_projectstepmodel_42.display_name = 'Kisebb csomag ár'
    botapp_projectstepmodel_42.order_index = 20
    botapp_projectstepmodel_42.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_42.value = 'lower_bag_price'
    botapp_projectstepmodel_42.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_42.variable = True
    botapp_projectstepmodel_42.project = botapp_projectmodel_2
    botapp_projectstepmodel_42 = importer.save_or_locate(botapp_projectstepmodel_42)

    botapp_projectstepmodel_43 = WriteProjectStepModel()
    botapp_projectstepmodel_43.display_name = 'Nagyobb csomag súly'
    botapp_projectstepmodel_43.order_index = 21
    botapp_projectstepmodel_43.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_43.value = 'larger_bag_weight'
    botapp_projectstepmodel_43.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__weight'
    botapp_projectstepmodel_43.variable = True
    botapp_projectstepmodel_43.project = botapp_projectmodel_2
    botapp_projectstepmodel_43 = importer.save_or_locate(botapp_projectstepmodel_43)

    botapp_projectstepmodel_44 = WriteProjectStepModel()
    botapp_projectstepmodel_44.display_name = 'Nagyobb csomag ár'
    botapp_projectstepmodel_44.order_index = 22
    botapp_projectstepmodel_44.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_44.value = 'larger_bag_price'
    botapp_projectstepmodel_44.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_44.variable = True
    botapp_projectstepmodel_44.project = botapp_projectmodel_2
    botapp_projectstepmodel_44 = importer.save_or_locate(botapp_projectstepmodel_44)

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

    botapp_projectstepmodel_18 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_18.display_name = 'Összeg mentése'
    botapp_projectstepmodel_18.order_index = 16
    botapp_projectstepmodel_18.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_18.value = 'lowest_price'
    botapp_projectstepmodel_18.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-total > trips-breakdown > div.breakdown > div > div.price-number.notranslate.short-price'
    botapp_projectstepmodel_18.variable = True
    botapp_projectstepmodel_18.project = botapp_projectmodel_1
    botapp_projectstepmodel_18 = importer.save_or_locate(botapp_projectstepmodel_18)

    botapp_projectstepmodel_19 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_19.display_name = 'Kisebb csomag súly'
    botapp_projectstepmodel_19.order_index = 19
    botapp_projectstepmodel_19.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_19.value = 'lower_bag_weight'
    botapp_projectstepmodel_19.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(1) > span.bag-item__weight'
    botapp_projectstepmodel_19.variable = True
    botapp_projectstepmodel_19.project = botapp_projectmodel_1
    botapp_projectstepmodel_19 = importer.save_or_locate(botapp_projectstepmodel_19)

    botapp_projectstepmodel_20 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_20.display_name = 'Kisebb csomag ár'
    botapp_projectstepmodel_20.order_index = 20
    botapp_projectstepmodel_20.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_20.value = 'lower_bag_price'
    botapp_projectstepmodel_20.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_20.variable = True
    botapp_projectstepmodel_20.project = botapp_projectmodel_1
    botapp_projectstepmodel_20 = importer.save_or_locate(botapp_projectstepmodel_20)

    botapp_projectstepmodel_21 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_21.display_name = 'Nagyobb csomag súly'
    botapp_projectstepmodel_21.order_index = 21
    botapp_projectstepmodel_21.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_21.value = 'larger_bag_weight'
    botapp_projectstepmodel_21.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__weight'
    botapp_projectstepmodel_21.variable = True
    botapp_projectstepmodel_21.project = botapp_projectmodel_1
    botapp_projectstepmodel_21 = importer.save_or_locate(botapp_projectstepmodel_21)

    botapp_projectstepmodel_22 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_22.display_name = 'Nagyobb csomag ár'
    botapp_projectstepmodel_22.order_index = 22
    botapp_projectstepmodel_22.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_22.value = 'larger_bag_price'
    botapp_projectstepmodel_22.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_22.variable = True
    botapp_projectstepmodel_22.project = botapp_projectmodel_1
    botapp_projectstepmodel_22 = importer.save_or_locate(botapp_projectstepmodel_22)

    botapp_projectstepmodel_23 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_23.display_name = 'Indulási állomás felugró megnyitása'
    botapp_projectstepmodel_23.order_index = 1
    botapp_projectstepmodel_23.action_type = 'clickAndWait'
    botapp_projectstepmodel_23.value = '1.0'
    botapp_projectstepmodel_23.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_23.variable = False
    botapp_projectstepmodel_23.project = botapp_projectmodel_2
    botapp_projectstepmodel_23 = importer.save_or_locate(botapp_projectstepmodel_23)

    botapp_projectstepmodel_24 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_24.display_name = 'Indulási ország kiválasztása'
    botapp_projectstepmodel_24.order_index = 2
    botapp_projectstepmodel_24.action_type = 'clickAndWait'
    botapp_projectstepmodel_24.value = '1.0'
    botapp_projectstepmodel_24.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div.core-list-item.core-list-item-rounded.clicked'
    botapp_projectstepmodel_24.variable = False
    botapp_projectstepmodel_24.project = botapp_projectmodel_2
    botapp_projectstepmodel_24 = importer.save_or_locate(botapp_projectstepmodel_24)

    botapp_projectstepmodel_25 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_25.display_name = 'Indulási repülőtér kiválasztása'
    botapp_projectstepmodel_25.order_index = 3
    botapp_projectstepmodel_25.action_type = 'clickAndWait'
    botapp_projectstepmodel_25.value = '1.0'
    botapp_projectstepmodel_25.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div.core-list-item.core-list-item-rounded.clicked > span'
    botapp_projectstepmodel_25.variable = False
    botapp_projectstepmodel_25.project = botapp_projectmodel_2
    botapp_projectstepmodel_25 = importer.save_or_locate(botapp_projectstepmodel_25)

    botapp_projectstepmodel_26 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_26.display_name = 'Érkezési állomás felugró megnyitása'
    botapp_projectstepmodel_26.order_index = 4
    botapp_projectstepmodel_26.action_type = 'clickAndWait'
    botapp_projectstepmodel_26.value = '1.0'
    botapp_projectstepmodel_26.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_26.variable = False
    botapp_projectstepmodel_26.project = botapp_projectmodel_2
    botapp_projectstepmodel_26 = importer.save_or_locate(botapp_projectstepmodel_26)

    botapp_projectstepmodel_27 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_27.display_name = 'Érkezési ország kiválasztása'
    botapp_projectstepmodel_27.order_index = 5
    botapp_projectstepmodel_27.action_type = 'clickAndWait'
    botapp_projectstepmodel_27.value = '1.0'
    botapp_projectstepmodel_27.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div:nth-child(4)'
    botapp_projectstepmodel_27.variable = False
    botapp_projectstepmodel_27.project = botapp_projectmodel_2
    botapp_projectstepmodel_27 = importer.save_or_locate(botapp_projectstepmodel_27)

    botapp_projectstepmodel_28 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_28.display_name = 'Érkezési repülőtér kiválasztása'
    botapp_projectstepmodel_28.order_index = 6
    botapp_projectstepmodel_28.action_type = 'clickAndWait'
    botapp_projectstepmodel_28.value = '1.0'
    botapp_projectstepmodel_28.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div:nth-child(3) > span'
    botapp_projectstepmodel_28.variable = False
    botapp_projectstepmodel_28.project = botapp_projectmodel_2
    botapp_projectstepmodel_28 = importer.save_or_locate(botapp_projectstepmodel_28)

    botapp_projectstepmodel_29 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_29.display_name = 'Utasok felugró kiválasztása'
    botapp_projectstepmodel_29.order_index = 7
    botapp_projectstepmodel_29.action_type = 'clickAndWait'
    botapp_projectstepmodel_29.value = '1.0'
    botapp_projectstepmodel_29.html_query = '#row-dates-pax > div.col-passengers > div:nth-child(2) > div:nth-child(5) > div > div.value'
    botapp_projectstepmodel_29.variable = False
    botapp_projectstepmodel_29.project = botapp_projectmodel_2
    botapp_projectstepmodel_29 = importer.save_or_locate(botapp_projectstepmodel_29)

    botapp_projectstepmodel_30 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_30.display_name = '1 (+1) utas hozzáadása'
    botapp_projectstepmodel_30.order_index = 8
    botapp_projectstepmodel_30.action_type = 'clickAndWait'
    botapp_projectstepmodel_30.value = '1.0'
    botapp_projectstepmodel_30.html_query = '#row-dates-pax > div.col-passengers > div.popup-passenger-input.opened > div > div > div.content > popup-content > div:nth-child(6) > div > div.details-controls > core-inc-dec > button.core-btn.inc.core-btn-wrap'
    botapp_projectstepmodel_30.variable = False
    botapp_projectstepmodel_30.project = botapp_projectmodel_2
    botapp_projectstepmodel_30 = importer.save_or_locate(botapp_projectstepmodel_30)

    botapp_projectstepmodel_31 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_31.display_name = 'Indulási időpont kiválasztása'
    botapp_projectstepmodel_31.order_index = 9
    botapp_projectstepmodel_31.action_type = 'clickAndWait'
    botapp_projectstepmodel_31.value = '1.0'
    botapp_projectstepmodel_31.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required > div.focused > div'
    botapp_projectstepmodel_31.variable = False
    botapp_projectstepmodel_31.project = botapp_projectmodel_2
    botapp_projectstepmodel_31 = importer.save_or_locate(botapp_projectstepmodel_31)

    botapp_projectstepmodel_32 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_32.display_name = 'Visszaút kiválasztása'
    botapp_projectstepmodel_32.order_index = 10
    botapp_projectstepmodel_32.action_type = 'clickAndWait'
    botapp_projectstepmodel_32.value = '1.0'
    botapp_projectstepmodel_32.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.core-date-range.popup-start-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.six-rows.scrollable > ul > li:nth-child(1) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_32.variable = False
    botapp_projectstepmodel_32.project = botapp_projectmodel_2
    botapp_projectstepmodel_32 = importer.save_or_locate(botapp_projectstepmodel_32)

    botapp_projectstepmodel_33 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_33.display_name = 'Indulásra kattintás'
    botapp_projectstepmodel_33.order_index = 11
    botapp_projectstepmodel_33.action_type = 'clickAndWait'
    botapp_projectstepmodel_33.value = '1.0'
    botapp_projectstepmodel_33.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-to > div > div.core-date-range.popup-end-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.scrollable.six-rows > ul > li:nth-child(2) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_33.variable = False
    botapp_projectstepmodel_33.project = botapp_projectmodel_2
    botapp_projectstepmodel_33 = importer.save_or_locate(botapp_projectstepmodel_33)

    botapp_projectstepmodel_34 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_34.display_name = 'Oda "összegtől" gomb megnyomása'
    botapp_projectstepmodel_34.order_index = 12
    botapp_projectstepmodel_34.action_type = 'clickAndWait'
    botapp_projectstepmodel_34.value = '1.0'
    botapp_projectstepmodel_34.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-right > button:nth-child(2)'
    botapp_projectstepmodel_34.variable = False
    botapp_projectstepmodel_34.project = botapp_projectmodel_2
    botapp_projectstepmodel_34 = importer.save_or_locate(botapp_projectstepmodel_34)

    botapp_projectstepmodel_35 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_35.display_name = 'Oda normál viteldíj beállítása'
    botapp_projectstepmodel_35.order_index = 13
    botapp_projectstepmodel_35.action_type = 'clickAndWait'
    botapp_projectstepmodel_35.value = '1.0'
    botapp_projectstepmodel_35.html_query = '#flight-FR\x07e 8415\x07e \x10 \x07e \x07e BUD\x07e 09\x02f 09\x02f 2017\x10 20\x03a 20\x07e CRL\x07e 09\x02f 09\x02f 2017\x10 22\x03a 25\x07e > div > div.flight-header__min-price.hide-mobile'
    botapp_projectstepmodel_35.variable = False
    botapp_projectstepmodel_35.project = botapp_projectmodel_2
    botapp_projectstepmodel_35 = importer.save_or_locate(botapp_projectstepmodel_35)

    botapp_projectstepmodel_36 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_36.display_name = 'Vissza "összegtől" gomb megnyomása'
    botapp_projectstepmodel_36.order_index = 14
    botapp_projectstepmodel_36.action_type = 'clickAndWait'
    botapp_projectstepmodel_36.value = '1.0'
    botapp_projectstepmodel_36.html_query = '#flight-FR\x07e 8416\x07e \x10 \x07e \x07e CRL\x07e 10\x02f 14\x02f 2017\x10 17\x03a 55\x07e BUD\x07e 10\x02f 14\x02f 2017\x10 19\x03a 55\x07e > div > div.flight-header__min-price.hide-mobile > flights-table-price > div > div.core-btn-primary'
    botapp_projectstepmodel_36.variable = False
    botapp_projectstepmodel_36.project = botapp_projectmodel_2
    botapp_projectstepmodel_36 = importer.save_or_locate(botapp_projectstepmodel_36)

    botapp_projectstepmodel_37 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_37.display_name = 'Folytatás gombra kattintés'
    botapp_projectstepmodel_37.order_index = 15
    botapp_projectstepmodel_37.action_type = 'clickAndWait'
    botapp_projectstepmodel_37.value = '1.0'
    botapp_projectstepmodel_37.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-cnt > button'
    botapp_projectstepmodel_37.variable = False
    botapp_projectstepmodel_37.project = botapp_projectmodel_2
    botapp_projectstepmodel_37 = importer.save_or_locate(botapp_projectstepmodel_37)

    botapp_projectstepmodel_38 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_38.display_name = 'Csomag hozzáadása'
    botapp_projectstepmodel_38.order_index = 17
    botapp_projectstepmodel_38.action_type = 'clickAndWait'
    botapp_projectstepmodel_38.value = '1.0'
    botapp_projectstepmodel_38.html_query = 'body > div.FR > main > div.body-section > extras-panels > section > article > leaderboard > div > extras-card:nth-child(3) > ng-include > div > div.action > button.core-btn-primary.add'
    botapp_projectstepmodel_38.variable = False
    botapp_projectstepmodel_38.project = botapp_projectmodel_2
    botapp_projectstepmodel_38 = importer.save_or_locate(botapp_projectstepmodel_38)

    botapp_projectstepmodel_39 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_39.display_name = 'Csomag hozzáadása felugró'
    botapp_projectstepmodel_39.order_index = 18
    botapp_projectstepmodel_39.action_type = 'clickAndWait'
    botapp_projectstepmodel_39.value = '1.0'
    botapp_projectstepmodel_39.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div'
    botapp_projectstepmodel_39.variable = False
    botapp_projectstepmodel_39.project = botapp_projectmodel_2
    botapp_projectstepmodel_39 = importer.save_or_locate(botapp_projectstepmodel_39)

    botapp_projectstepmodel_40 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_40.display_name = 'Összeg mentése'
    botapp_projectstepmodel_40.order_index = 16
    botapp_projectstepmodel_40.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_40.value = 'lowest_price'
    botapp_projectstepmodel_40.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-total > trips-breakdown > div.breakdown > div > div.price-number.notranslate.short-price'
    botapp_projectstepmodel_40.variable = True
    botapp_projectstepmodel_40.project = botapp_projectmodel_2
    botapp_projectstepmodel_40 = importer.save_or_locate(botapp_projectstepmodel_40)

    botapp_projectstepmodel_41 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_41.display_name = 'Kisebb csomag súly'
    botapp_projectstepmodel_41.order_index = 19
    botapp_projectstepmodel_41.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_41.value = 'lower_bag_weight'
    botapp_projectstepmodel_41.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(1) > span.bag-item__weight'
    botapp_projectstepmodel_41.variable = True
    botapp_projectstepmodel_41.project = botapp_projectmodel_2
    botapp_projectstepmodel_41 = importer.save_or_locate(botapp_projectstepmodel_41)

    botapp_projectstepmodel_42 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_42.display_name = 'Kisebb csomag ár'
    botapp_projectstepmodel_42.order_index = 20
    botapp_projectstepmodel_42.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_42.value = 'lower_bag_price'
    botapp_projectstepmodel_42.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_42.variable = True
    botapp_projectstepmodel_42.project = botapp_projectmodel_2
    botapp_projectstepmodel_42 = importer.save_or_locate(botapp_projectstepmodel_42)

    botapp_projectstepmodel_43 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_43.display_name = 'Nagyobb csomag súly'
    botapp_projectstepmodel_43.order_index = 21
    botapp_projectstepmodel_43.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_43.value = 'larger_bag_weight'
    botapp_projectstepmodel_43.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__weight'
    botapp_projectstepmodel_43.variable = True
    botapp_projectstepmodel_43.project = botapp_projectmodel_2
    botapp_projectstepmodel_43 = importer.save_or_locate(botapp_projectstepmodel_43)

    botapp_projectstepmodel_44 = ClickAndWaitProjectStepModel()
    botapp_projectstepmodel_44.display_name = 'Nagyobb csomag ár'
    botapp_projectstepmodel_44.order_index = 22
    botapp_projectstepmodel_44.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_44.value = 'larger_bag_price'
    botapp_projectstepmodel_44.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_44.variable = True
    botapp_projectstepmodel_44.project = botapp_projectmodel_2
    botapp_projectstepmodel_44 = importer.save_or_locate(botapp_projectstepmodel_44)

    # Processing model: botapp.models.StoreSelectedValueProjectStepModel

    from botapp.models import StoreSelectedValueProjectStepModel

    botapp_projectstepmodel_1 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_1.display_name = 'Indulási állomás felugró megnyitása'
    botapp_projectstepmodel_1.order_index = 1
    botapp_projectstepmodel_1.action_type = 'clickAndWait'
    botapp_projectstepmodel_1.value = '1.0'
    botapp_projectstepmodel_1.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_1.variable = False
    botapp_projectstepmodel_1.project = botapp_projectmodel_1
    botapp_projectstepmodel_1 = importer.save_or_locate(botapp_projectstepmodel_1)

    botapp_projectstepmodel_2 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_2.display_name = 'Indulási ország kiválasztása'
    botapp_projectstepmodel_2.order_index = 2
    botapp_projectstepmodel_2.action_type = 'clickAndWait'
    botapp_projectstepmodel_2.value = '1.0'
    botapp_projectstepmodel_2.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div.core-list-item.core-list-item-rounded.clicked'
    botapp_projectstepmodel_2.variable = False
    botapp_projectstepmodel_2.project = botapp_projectmodel_1
    botapp_projectstepmodel_2 = importer.save_or_locate(botapp_projectstepmodel_2)

    botapp_projectstepmodel_3 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_3.display_name = 'Indulási repülőtér kiválasztása'
    botapp_projectstepmodel_3.order_index = 3
    botapp_projectstepmodel_3.action_type = 'clickAndWait'
    botapp_projectstepmodel_3.value = '1.0'
    botapp_projectstepmodel_3.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div.core-list-item.core-list-item-rounded.clicked > span'
    botapp_projectstepmodel_3.variable = False
    botapp_projectstepmodel_3.project = botapp_projectmodel_1
    botapp_projectstepmodel_3 = importer.save_or_locate(botapp_projectstepmodel_3)

    botapp_projectstepmodel_4 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_4.display_name = 'Érkezési állomás felugró megnyitása'
    botapp_projectstepmodel_4.order_index = 4
    botapp_projectstepmodel_4.action_type = 'clickAndWait'
    botapp_projectstepmodel_4.value = '1.0'
    botapp_projectstepmodel_4.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_4.variable = False
    botapp_projectstepmodel_4.project = botapp_projectmodel_1
    botapp_projectstepmodel_4 = importer.save_or_locate(botapp_projectstepmodel_4)

    botapp_projectstepmodel_5 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_5.display_name = 'Érkezési ország kiválasztása'
    botapp_projectstepmodel_5.order_index = 5
    botapp_projectstepmodel_5.action_type = 'clickAndWait'
    botapp_projectstepmodel_5.value = '1.0'
    botapp_projectstepmodel_5.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div:nth-child(4)'
    botapp_projectstepmodel_5.variable = False
    botapp_projectstepmodel_5.project = botapp_projectmodel_1
    botapp_projectstepmodel_5 = importer.save_or_locate(botapp_projectstepmodel_5)

    botapp_projectstepmodel_6 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_6.display_name = 'Érkezési repülőtér kiválasztása'
    botapp_projectstepmodel_6.order_index = 6
    botapp_projectstepmodel_6.action_type = 'clickAndWait'
    botapp_projectstepmodel_6.value = '1.0'
    botapp_projectstepmodel_6.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div:nth-child(3) > span'
    botapp_projectstepmodel_6.variable = False
    botapp_projectstepmodel_6.project = botapp_projectmodel_1
    botapp_projectstepmodel_6 = importer.save_or_locate(botapp_projectstepmodel_6)

    botapp_projectstepmodel_7 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_7.display_name = 'Utasok felugró kiválasztása'
    botapp_projectstepmodel_7.order_index = 7
    botapp_projectstepmodel_7.action_type = 'clickAndWait'
    botapp_projectstepmodel_7.value = '1.0'
    botapp_projectstepmodel_7.html_query = '#row-dates-pax > div.col-passengers > div:nth-child(2) > div:nth-child(5) > div > div.value'
    botapp_projectstepmodel_7.variable = False
    botapp_projectstepmodel_7.project = botapp_projectmodel_1
    botapp_projectstepmodel_7 = importer.save_or_locate(botapp_projectstepmodel_7)

    botapp_projectstepmodel_8 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_8.display_name = '1 (+1) utas hozzáadása'
    botapp_projectstepmodel_8.order_index = 8
    botapp_projectstepmodel_8.action_type = 'clickAndWait'
    botapp_projectstepmodel_8.value = '1.0'
    botapp_projectstepmodel_8.html_query = '#row-dates-pax > div.col-passengers > div.popup-passenger-input.opened > div > div > div.content > popup-content > div:nth-child(6) > div > div.details-controls > core-inc-dec > button.core-btn.inc.core-btn-wrap'
    botapp_projectstepmodel_8.variable = False
    botapp_projectstepmodel_8.project = botapp_projectmodel_1
    botapp_projectstepmodel_8 = importer.save_or_locate(botapp_projectstepmodel_8)

    botapp_projectstepmodel_9 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_9.display_name = 'Indulási időpont kiválasztása'
    botapp_projectstepmodel_9.order_index = 9
    botapp_projectstepmodel_9.action_type = 'clickAndWait'
    botapp_projectstepmodel_9.value = '1.0'
    botapp_projectstepmodel_9.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required > div.focused > div'
    botapp_projectstepmodel_9.variable = False
    botapp_projectstepmodel_9.project = botapp_projectmodel_1
    botapp_projectstepmodel_9 = importer.save_or_locate(botapp_projectstepmodel_9)

    botapp_projectstepmodel_10 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_10.display_name = 'Visszaút kiválasztása'
    botapp_projectstepmodel_10.order_index = 10
    botapp_projectstepmodel_10.action_type = 'clickAndWait'
    botapp_projectstepmodel_10.value = '1.0'
    botapp_projectstepmodel_10.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.core-date-range.popup-start-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.six-rows.scrollable > ul > li:nth-child(1) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_10.variable = False
    botapp_projectstepmodel_10.project = botapp_projectmodel_1
    botapp_projectstepmodel_10 = importer.save_or_locate(botapp_projectstepmodel_10)

    botapp_projectstepmodel_11 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_11.display_name = 'Indulásra kattintás'
    botapp_projectstepmodel_11.order_index = 11
    botapp_projectstepmodel_11.action_type = 'clickAndWait'
    botapp_projectstepmodel_11.value = '1.0'
    botapp_projectstepmodel_11.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-to > div > div.core-date-range.popup-end-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.scrollable.six-rows > ul > li:nth-child(2) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_11.variable = False
    botapp_projectstepmodel_11.project = botapp_projectmodel_1
    botapp_projectstepmodel_11 = importer.save_or_locate(botapp_projectstepmodel_11)

    botapp_projectstepmodel_12 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_12.display_name = 'Oda "összegtől" gomb megnyomása'
    botapp_projectstepmodel_12.order_index = 12
    botapp_projectstepmodel_12.action_type = 'clickAndWait'
    botapp_projectstepmodel_12.value = '1.0'
    botapp_projectstepmodel_12.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-right > button:nth-child(2)'
    botapp_projectstepmodel_12.variable = False
    botapp_projectstepmodel_12.project = botapp_projectmodel_1
    botapp_projectstepmodel_12 = importer.save_or_locate(botapp_projectstepmodel_12)

    botapp_projectstepmodel_13 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_13.display_name = 'Oda normál viteldíj beállítása'
    botapp_projectstepmodel_13.order_index = 13
    botapp_projectstepmodel_13.action_type = 'clickAndWait'
    botapp_projectstepmodel_13.value = '1.0'
    botapp_projectstepmodel_13.html_query = '#flight-FR\x07e 8415\x07e \x10 \x07e \x07e BUD\x07e 09\x02f 09\x02f 2017\x10 20\x03a 20\x07e CRL\x07e 09\x02f 09\x02f 2017\x10 22\x03a 25\x07e > div > div.flight-header__min-price.hide-mobile'
    botapp_projectstepmodel_13.variable = False
    botapp_projectstepmodel_13.project = botapp_projectmodel_1
    botapp_projectstepmodel_13 = importer.save_or_locate(botapp_projectstepmodel_13)

    botapp_projectstepmodel_14 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_14.display_name = 'Vissza "összegtől" gomb megnyomása'
    botapp_projectstepmodel_14.order_index = 14
    botapp_projectstepmodel_14.action_type = 'clickAndWait'
    botapp_projectstepmodel_14.value = '1.0'
    botapp_projectstepmodel_14.html_query = '#flight-FR\x07e 8416\x07e \x10 \x07e \x07e CRL\x07e 10\x02f 14\x02f 2017\x10 17\x03a 55\x07e BUD\x07e 10\x02f 14\x02f 2017\x10 19\x03a 55\x07e > div > div.flight-header__min-price.hide-mobile > flights-table-price > div > div.core-btn-primary'
    botapp_projectstepmodel_14.variable = False
    botapp_projectstepmodel_14.project = botapp_projectmodel_1
    botapp_projectstepmodel_14 = importer.save_or_locate(botapp_projectstepmodel_14)

    botapp_projectstepmodel_15 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_15.display_name = 'Folytatás gombra kattintés'
    botapp_projectstepmodel_15.order_index = 15
    botapp_projectstepmodel_15.action_type = 'clickAndWait'
    botapp_projectstepmodel_15.value = '1.0'
    botapp_projectstepmodel_15.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-cnt > button'
    botapp_projectstepmodel_15.variable = False
    botapp_projectstepmodel_15.project = botapp_projectmodel_1
    botapp_projectstepmodel_15 = importer.save_or_locate(botapp_projectstepmodel_15)

    botapp_projectstepmodel_16 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_16.display_name = 'Csomag hozzáadása'
    botapp_projectstepmodel_16.order_index = 17
    botapp_projectstepmodel_16.action_type = 'clickAndWait'
    botapp_projectstepmodel_16.value = '1.0'
    botapp_projectstepmodel_16.html_query = 'body > div.FR > main > div.body-section > extras-panels > section > article > leaderboard > div > extras-card:nth-child(3) > ng-include > div > div.action > button.core-btn-primary.add'
    botapp_projectstepmodel_16.variable = False
    botapp_projectstepmodel_16.project = botapp_projectmodel_1
    botapp_projectstepmodel_16 = importer.save_or_locate(botapp_projectstepmodel_16)

    botapp_projectstepmodel_17 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_17.display_name = 'Csomag hozzáadása felugró'
    botapp_projectstepmodel_17.order_index = 18
    botapp_projectstepmodel_17.action_type = 'clickAndWait'
    botapp_projectstepmodel_17.value = '1.0'
    botapp_projectstepmodel_17.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div'
    botapp_projectstepmodel_17.variable = False
    botapp_projectstepmodel_17.project = botapp_projectmodel_1
    botapp_projectstepmodel_17 = importer.save_or_locate(botapp_projectstepmodel_17)

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

    botapp_projectstepmodel_23 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_23.display_name = 'Indulási állomás felugró megnyitása'
    botapp_projectstepmodel_23.order_index = 1
    botapp_projectstepmodel_23.action_type = 'clickAndWait'
    botapp_projectstepmodel_23.value = '1.0'
    botapp_projectstepmodel_23.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_23.variable = False
    botapp_projectstepmodel_23.project = botapp_projectmodel_2
    botapp_projectstepmodel_23 = importer.save_or_locate(botapp_projectstepmodel_23)

    botapp_projectstepmodel_24 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_24.display_name = 'Indulási ország kiválasztása'
    botapp_projectstepmodel_24.order_index = 2
    botapp_projectstepmodel_24.action_type = 'clickAndWait'
    botapp_projectstepmodel_24.value = '1.0'
    botapp_projectstepmodel_24.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div.core-list-item.core-list-item-rounded.clicked'
    botapp_projectstepmodel_24.variable = False
    botapp_projectstepmodel_24.project = botapp_projectmodel_2
    botapp_projectstepmodel_24 = importer.save_or_locate(botapp_projectstepmodel_24)

    botapp_projectstepmodel_25 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_25.display_name = 'Indulási repülőtér kiválasztása'
    botapp_projectstepmodel_25.order_index = 3
    botapp_projectstepmodel_25.action_type = 'clickAndWait'
    botapp_projectstepmodel_25.value = '1.0'
    botapp_projectstepmodel_25.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div.core-list-item.core-list-item-rounded.clicked > span'
    botapp_projectstepmodel_25.variable = False
    botapp_projectstepmodel_25.project = botapp_projectmodel_2
    botapp_projectstepmodel_25 = importer.save_or_locate(botapp_projectstepmodel_25)

    botapp_projectstepmodel_26 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_26.display_name = 'Érkezési állomás felugró megnyitása'
    botapp_projectstepmodel_26.order_index = 4
    botapp_projectstepmodel_26.action_type = 'clickAndWait'
    botapp_projectstepmodel_26.value = '1.0'
    botapp_projectstepmodel_26.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input'
    botapp_projectstepmodel_26.variable = False
    botapp_projectstepmodel_26.project = botapp_projectmodel_2
    botapp_projectstepmodel_26 = importer.save_or_locate(botapp_projectstepmodel_26)

    botapp_projectstepmodel_27 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_27.display_name = 'Érkezési ország kiválasztása'
    botapp_projectstepmodel_27.order_index = 5
    botapp_projectstepmodel_27.action_type = 'clickAndWait'
    botapp_projectstepmodel_27.value = '1.0'
    botapp_projectstepmodel_27.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div:nth-child(4)'
    botapp_projectstepmodel_27.variable = False
    botapp_projectstepmodel_27.project = botapp_projectmodel_2
    botapp_projectstepmodel_27 = importer.save_or_locate(botapp_projectstepmodel_27)

    botapp_projectstepmodel_28 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_28.display_name = 'Érkezési repülőtér kiválasztása'
    botapp_projectstepmodel_28.order_index = 6
    botapp_projectstepmodel_28.action_type = 'clickAndWait'
    botapp_projectstepmodel_28.value = '1.0'
    botapp_projectstepmodel_28.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div:nth-child(3) > span'
    botapp_projectstepmodel_28.variable = False
    botapp_projectstepmodel_28.project = botapp_projectmodel_2
    botapp_projectstepmodel_28 = importer.save_or_locate(botapp_projectstepmodel_28)

    botapp_projectstepmodel_29 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_29.display_name = 'Utasok felugró kiválasztása'
    botapp_projectstepmodel_29.order_index = 7
    botapp_projectstepmodel_29.action_type = 'clickAndWait'
    botapp_projectstepmodel_29.value = '1.0'
    botapp_projectstepmodel_29.html_query = '#row-dates-pax > div.col-passengers > div:nth-child(2) > div:nth-child(5) > div > div.value'
    botapp_projectstepmodel_29.variable = False
    botapp_projectstepmodel_29.project = botapp_projectmodel_2
    botapp_projectstepmodel_29 = importer.save_or_locate(botapp_projectstepmodel_29)

    botapp_projectstepmodel_30 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_30.display_name = '1 (+1) utas hozzáadása'
    botapp_projectstepmodel_30.order_index = 8
    botapp_projectstepmodel_30.action_type = 'clickAndWait'
    botapp_projectstepmodel_30.value = '1.0'
    botapp_projectstepmodel_30.html_query = '#row-dates-pax > div.col-passengers > div.popup-passenger-input.opened > div > div > div.content > popup-content > div:nth-child(6) > div > div.details-controls > core-inc-dec > button.core-btn.inc.core-btn-wrap'
    botapp_projectstepmodel_30.variable = False
    botapp_projectstepmodel_30.project = botapp_projectmodel_2
    botapp_projectstepmodel_30 = importer.save_or_locate(botapp_projectstepmodel_30)

    botapp_projectstepmodel_31 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_31.display_name = 'Indulási időpont kiválasztása'
    botapp_projectstepmodel_31.order_index = 9
    botapp_projectstepmodel_31.action_type = 'clickAndWait'
    botapp_projectstepmodel_31.value = '1.0'
    botapp_projectstepmodel_31.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required > div.focused > div'
    botapp_projectstepmodel_31.variable = False
    botapp_projectstepmodel_31.project = botapp_projectmodel_2
    botapp_projectstepmodel_31 = importer.save_or_locate(botapp_projectstepmodel_31)

    botapp_projectstepmodel_32 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_32.display_name = 'Visszaút kiválasztása'
    botapp_projectstepmodel_32.order_index = 10
    botapp_projectstepmodel_32.action_type = 'clickAndWait'
    botapp_projectstepmodel_32.value = '1.0'
    botapp_projectstepmodel_32.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.core-date-range.popup-start-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.six-rows.scrollable > ul > li:nth-child(1) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_32.variable = False
    botapp_projectstepmodel_32.project = botapp_projectmodel_2
    botapp_projectstepmodel_32 = importer.save_or_locate(botapp_projectstepmodel_32)

    botapp_projectstepmodel_33 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_33.display_name = 'Indulásra kattintás'
    botapp_projectstepmodel_33.order_index = 11
    botapp_projectstepmodel_33.action_type = 'clickAndWait'
    botapp_projectstepmodel_33.value = '1.0'
    botapp_projectstepmodel_33.html_query = '#row-dates-pax > div:nth-child(1) > div > div.container-to > div > div.core-date-range.popup-end-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.scrollable.six-rows > ul > li:nth-child(2) > ul.days > li:nth-child(20) > span'
    botapp_projectstepmodel_33.variable = False
    botapp_projectstepmodel_33.project = botapp_projectmodel_2
    botapp_projectstepmodel_33 = importer.save_or_locate(botapp_projectstepmodel_33)

    botapp_projectstepmodel_34 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_34.display_name = 'Oda "összegtől" gomb megnyomása'
    botapp_projectstepmodel_34.order_index = 12
    botapp_projectstepmodel_34.action_type = 'clickAndWait'
    botapp_projectstepmodel_34.value = '1.0'
    botapp_projectstepmodel_34.html_query = '#search-container > div:nth-child(1) > div > form > div.col-flight-search-right > button:nth-child(2)'
    botapp_projectstepmodel_34.variable = False
    botapp_projectstepmodel_34.project = botapp_projectmodel_2
    botapp_projectstepmodel_34 = importer.save_or_locate(botapp_projectstepmodel_34)

    botapp_projectstepmodel_35 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_35.display_name = 'Oda normál viteldíj beállítása'
    botapp_projectstepmodel_35.order_index = 13
    botapp_projectstepmodel_35.action_type = 'clickAndWait'
    botapp_projectstepmodel_35.value = '1.0'
    botapp_projectstepmodel_35.html_query = '#flight-FR\x07e 8415\x07e \x10 \x07e \x07e BUD\x07e 09\x02f 09\x02f 2017\x10 20\x03a 20\x07e CRL\x07e 09\x02f 09\x02f 2017\x10 22\x03a 25\x07e > div > div.flight-header__min-price.hide-mobile'
    botapp_projectstepmodel_35.variable = False
    botapp_projectstepmodel_35.project = botapp_projectmodel_2
    botapp_projectstepmodel_35 = importer.save_or_locate(botapp_projectstepmodel_35)

    botapp_projectstepmodel_36 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_36.display_name = 'Vissza "összegtől" gomb megnyomása'
    botapp_projectstepmodel_36.order_index = 14
    botapp_projectstepmodel_36.action_type = 'clickAndWait'
    botapp_projectstepmodel_36.value = '1.0'
    botapp_projectstepmodel_36.html_query = '#flight-FR\x07e 8416\x07e \x10 \x07e \x07e CRL\x07e 10\x02f 14\x02f 2017\x10 17\x03a 55\x07e BUD\x07e 10\x02f 14\x02f 2017\x10 19\x03a 55\x07e > div > div.flight-header__min-price.hide-mobile > flights-table-price > div > div.core-btn-primary'
    botapp_projectstepmodel_36.variable = False
    botapp_projectstepmodel_36.project = botapp_projectmodel_2
    botapp_projectstepmodel_36 = importer.save_or_locate(botapp_projectstepmodel_36)

    botapp_projectstepmodel_37 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_37.display_name = 'Folytatás gombra kattintés'
    botapp_projectstepmodel_37.order_index = 15
    botapp_projectstepmodel_37.action_type = 'clickAndWait'
    botapp_projectstepmodel_37.value = '1.0'
    botapp_projectstepmodel_37.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-cnt > button'
    botapp_projectstepmodel_37.variable = False
    botapp_projectstepmodel_37.project = botapp_projectmodel_2
    botapp_projectstepmodel_37 = importer.save_or_locate(botapp_projectstepmodel_37)

    botapp_projectstepmodel_38 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_38.display_name = 'Csomag hozzáadása'
    botapp_projectstepmodel_38.order_index = 17
    botapp_projectstepmodel_38.action_type = 'clickAndWait'
    botapp_projectstepmodel_38.value = '1.0'
    botapp_projectstepmodel_38.html_query = 'body > div.FR > main > div.body-section > extras-panels > section > article > leaderboard > div > extras-card:nth-child(3) > ng-include > div > div.action > button.core-btn-primary.add'
    botapp_projectstepmodel_38.variable = False
    botapp_projectstepmodel_38.project = botapp_projectmodel_2
    botapp_projectstepmodel_38 = importer.save_or_locate(botapp_projectstepmodel_38)

    botapp_projectstepmodel_39 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_39.display_name = 'Csomag hozzáadása felugró'
    botapp_projectstepmodel_39.order_index = 18
    botapp_projectstepmodel_39.action_type = 'clickAndWait'
    botapp_projectstepmodel_39.value = '1.0'
    botapp_projectstepmodel_39.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div'
    botapp_projectstepmodel_39.variable = False
    botapp_projectstepmodel_39.project = botapp_projectmodel_2
    botapp_projectstepmodel_39 = importer.save_or_locate(botapp_projectstepmodel_39)

    botapp_projectstepmodel_40 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_40.display_name = 'Összeg mentése'
    botapp_projectstepmodel_40.order_index = 16
    botapp_projectstepmodel_40.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_40.value = 'lowest_price'
    botapp_projectstepmodel_40.html_query = '#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-total > trips-breakdown > div.breakdown > div > div.price-number.notranslate.short-price'
    botapp_projectstepmodel_40.variable = True
    botapp_projectstepmodel_40.project = botapp_projectmodel_2
    botapp_projectstepmodel_40 = importer.save_or_locate(botapp_projectstepmodel_40)

    botapp_projectstepmodel_41 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_41.display_name = 'Kisebb csomag súly'
    botapp_projectstepmodel_41.order_index = 19
    botapp_projectstepmodel_41.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_41.value = 'lower_bag_weight'
    botapp_projectstepmodel_41.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(1) > span.bag-item__weight'
    botapp_projectstepmodel_41.variable = True
    botapp_projectstepmodel_41.project = botapp_projectmodel_2
    botapp_projectstepmodel_41 = importer.save_or_locate(botapp_projectstepmodel_41)

    botapp_projectstepmodel_42 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_42.display_name = 'Kisebb csomag ár'
    botapp_projectstepmodel_42.order_index = 20
    botapp_projectstepmodel_42.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_42.value = 'lower_bag_price'
    botapp_projectstepmodel_42.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_42.variable = True
    botapp_projectstepmodel_42.project = botapp_projectmodel_2
    botapp_projectstepmodel_42 = importer.save_or_locate(botapp_projectstepmodel_42)

    botapp_projectstepmodel_43 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_43.display_name = 'Nagyobb csomag súly'
    botapp_projectstepmodel_43.order_index = 21
    botapp_projectstepmodel_43.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_43.value = 'larger_bag_weight'
    botapp_projectstepmodel_43.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__weight'
    botapp_projectstepmodel_43.variable = True
    botapp_projectstepmodel_43.project = botapp_projectmodel_2
    botapp_projectstepmodel_43 = importer.save_or_locate(botapp_projectstepmodel_43)

    botapp_projectstepmodel_44 = StoreSelectedValueProjectStepModel()
    botapp_projectstepmodel_44.display_name = 'Nagyobb csomag ár'
    botapp_projectstepmodel_44.order_index = 22
    botapp_projectstepmodel_44.action_type = 'storeSelectedValue'
    botapp_projectstepmodel_44.value = 'larger_bag_price'
    botapp_projectstepmodel_44.html_query = '#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price'
    botapp_projectstepmodel_44.variable = True
    botapp_projectstepmodel_44.project = botapp_projectmodel_2
    botapp_projectstepmodel_44 = importer.save_or_locate(botapp_projectstepmodel_44)

    # Processing model: botapp.models.JobModel

    from botapp.models import JobModel

    botapp_jobmodel_1 = JobModel()
    botapp_jobmodel_1.project = botapp_projectmodel_2
    botapp_jobmodel_1.scrapy_job = '0f048622968311e78a7eb0359f60a621'
    botapp_jobmodel_1.state = 'pending'
    botapp_jobmodel_1.created = dateutil.parser.parse("2017-09-10T23:52:09.505171+00:00")
    botapp_jobmodel_1 = importer.save_or_locate(botapp_jobmodel_1)

    botapp_jobmodel_2 = JobModel()
    botapp_jobmodel_2.project = botapp_projectmodel_1
    botapp_jobmodel_2.scrapy_job = '44c0835e968511e78a7eb0359f60a621'
    botapp_jobmodel_2.state = 'pending'
    botapp_jobmodel_2.created = dateutil.parser.parse("2017-09-11T00:07:58.648729+00:00")
    botapp_jobmodel_2 = importer.save_or_locate(botapp_jobmodel_2)

    botapp_jobmodel_3 = JobModel()
    botapp_jobmodel_3.project = botapp_projectmodel_1
    botapp_jobmodel_3.scrapy_job = 'e5992dd2968811e78a7eb0359f60a621'
    botapp_jobmodel_3.state = 'pending'
    botapp_jobmodel_3.created = dateutil.parser.parse("2017-09-11T00:33:56.990271+00:00")
    botapp_jobmodel_3 = importer.save_or_locate(botapp_jobmodel_3)

