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
# ./manage.py dumpscript auth
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

    # Processing model: django.contrib.auth.models.Permission

    from django.contrib.auth.models import Permission

    auth_permission_1 = Permission()
    auth_permission_1.name = 'Can add log entry'
    auth_permission_1.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_1.codename = 'add_logentry'
    auth_permission_1 = importer.save_or_locate(auth_permission_1)

    auth_permission_2 = Permission()
    auth_permission_2.name = 'Can change log entry'
    auth_permission_2.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_2.codename = 'change_logentry'
    auth_permission_2 = importer.save_or_locate(auth_permission_2)

    auth_permission_3 = Permission()
    auth_permission_3.name = 'Can delete log entry'
    auth_permission_3.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_3.codename = 'delete_logentry'
    auth_permission_3 = importer.save_or_locate(auth_permission_3)

    auth_permission_4 = Permission()
    auth_permission_4.name = 'Can add group'
    auth_permission_4.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_4.codename = 'add_group'
    auth_permission_4 = importer.save_or_locate(auth_permission_4)

    auth_permission_5 = Permission()
    auth_permission_5.name = 'Can change group'
    auth_permission_5.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_5.codename = 'change_group'
    auth_permission_5 = importer.save_or_locate(auth_permission_5)

    auth_permission_6 = Permission()
    auth_permission_6.name = 'Can delete group'
    auth_permission_6.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_6.codename = 'delete_group'
    auth_permission_6 = importer.save_or_locate(auth_permission_6)

    auth_permission_7 = Permission()
    auth_permission_7.name = 'Can add permission'
    auth_permission_7.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_7.codename = 'add_permission'
    auth_permission_7 = importer.save_or_locate(auth_permission_7)

    auth_permission_8 = Permission()
    auth_permission_8.name = 'Can change permission'
    auth_permission_8.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_8.codename = 'change_permission'
    auth_permission_8 = importer.save_or_locate(auth_permission_8)

    auth_permission_9 = Permission()
    auth_permission_9.name = 'Can delete permission'
    auth_permission_9.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_9.codename = 'delete_permission'
    auth_permission_9 = importer.save_or_locate(auth_permission_9)

    auth_permission_10 = Permission()
    auth_permission_10.name = 'Can add user'
    auth_permission_10.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_10.codename = 'add_user'
    auth_permission_10 = importer.save_or_locate(auth_permission_10)

    auth_permission_11 = Permission()
    auth_permission_11.name = 'Can change user'
    auth_permission_11.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_11.codename = 'change_user'
    auth_permission_11 = importer.save_or_locate(auth_permission_11)

    auth_permission_12 = Permission()
    auth_permission_12.name = 'Can delete user'
    auth_permission_12.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_12.codename = 'delete_user'
    auth_permission_12 = importer.save_or_locate(auth_permission_12)

    auth_permission_13 = Permission()
    auth_permission_13.name = 'Can add job model'
    auth_permission_13.content_type = ContentType.objects.get(app_label="botapp", model="jobmodel")
    auth_permission_13.codename = 'add_jobmodel'
    auth_permission_13 = importer.save_or_locate(auth_permission_13)

    auth_permission_14 = Permission()
    auth_permission_14.name = 'Can change job model'
    auth_permission_14.content_type = ContentType.objects.get(app_label="botapp", model="jobmodel")
    auth_permission_14.codename = 'change_jobmodel'
    auth_permission_14 = importer.save_or_locate(auth_permission_14)

    auth_permission_15 = Permission()
    auth_permission_15.name = 'Can delete job model'
    auth_permission_15.content_type = ContentType.objects.get(app_label="botapp", model="jobmodel")
    auth_permission_15.codename = 'delete_jobmodel'
    auth_permission_15 = importer.save_or_locate(auth_permission_15)

    auth_permission_16 = Permission()
    auth_permission_16.name = 'Can add project'
    auth_permission_16.content_type = ContentType.objects.get(app_label="botapp", model="projectmodel")
    auth_permission_16.codename = 'add_projectmodel'
    auth_permission_16 = importer.save_or_locate(auth_permission_16)

    auth_permission_17 = Permission()
    auth_permission_17.name = 'Can change project'
    auth_permission_17.content_type = ContentType.objects.get(app_label="botapp", model="projectmodel")
    auth_permission_17.codename = 'change_projectmodel'
    auth_permission_17 = importer.save_or_locate(auth_permission_17)

    auth_permission_18 = Permission()
    auth_permission_18.name = 'Can delete project'
    auth_permission_18.content_type = ContentType.objects.get(app_label="botapp", model="projectmodel")
    auth_permission_18.codename = 'delete_projectmodel'
    auth_permission_18 = importer.save_or_locate(auth_permission_18)

    auth_permission_19 = Permission()
    auth_permission_19.name = 'Can add click and wait project step model'
    auth_permission_19.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_19.codename = 'add_clickandwaitprojectstepmodel'
    auth_permission_19 = importer.save_or_locate(auth_permission_19)

    auth_permission_20 = Permission()
    auth_permission_20.name = 'Can add click project step model'
    auth_permission_20.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_20.codename = 'add_clickprojectstepmodel'
    auth_permission_20 = importer.save_or_locate(auth_permission_20)

    auth_permission_21 = Permission()
    auth_permission_21.name = 'Can add open project step model'
    auth_permission_21.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_21.codename = 'add_openprojectstepmodel'
    auth_permission_21 = importer.save_or_locate(auth_permission_21)

    auth_permission_22 = Permission()
    auth_permission_22.name = 'Can add project step model'
    auth_permission_22.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_22.codename = 'add_projectstepmodel'
    auth_permission_22 = importer.save_or_locate(auth_permission_22)

    auth_permission_23 = Permission()
    auth_permission_23.name = 'Can add store selected value project step model'
    auth_permission_23.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_23.codename = 'add_storeselectedvalueprojectstepmodel'
    auth_permission_23 = importer.save_or_locate(auth_permission_23)

    auth_permission_24 = Permission()
    auth_permission_24.name = 'Can add wait project step model'
    auth_permission_24.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_24.codename = 'add_waitprojectstepmodel'
    auth_permission_24 = importer.save_or_locate(auth_permission_24)

    auth_permission_25 = Permission()
    auth_permission_25.name = 'Can add write project step model'
    auth_permission_25.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_25.codename = 'add_writeprojectstepmodel'
    auth_permission_25 = importer.save_or_locate(auth_permission_25)

    auth_permission_26 = Permission()
    auth_permission_26.name = 'Can change click and wait project step model'
    auth_permission_26.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_26.codename = 'change_clickandwaitprojectstepmodel'
    auth_permission_26 = importer.save_or_locate(auth_permission_26)

    auth_permission_27 = Permission()
    auth_permission_27.name = 'Can change click project step model'
    auth_permission_27.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_27.codename = 'change_clickprojectstepmodel'
    auth_permission_27 = importer.save_or_locate(auth_permission_27)

    auth_permission_28 = Permission()
    auth_permission_28.name = 'Can change open project step model'
    auth_permission_28.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_28.codename = 'change_openprojectstepmodel'
    auth_permission_28 = importer.save_or_locate(auth_permission_28)

    auth_permission_29 = Permission()
    auth_permission_29.name = 'Can change project step model'
    auth_permission_29.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_29.codename = 'change_projectstepmodel'
    auth_permission_29 = importer.save_or_locate(auth_permission_29)

    auth_permission_30 = Permission()
    auth_permission_30.name = 'Can change store selected value project step model'
    auth_permission_30.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_30.codename = 'change_storeselectedvalueprojectstepmodel'
    auth_permission_30 = importer.save_or_locate(auth_permission_30)

    auth_permission_31 = Permission()
    auth_permission_31.name = 'Can change wait project step model'
    auth_permission_31.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_31.codename = 'change_waitprojectstepmodel'
    auth_permission_31 = importer.save_or_locate(auth_permission_31)

    auth_permission_32 = Permission()
    auth_permission_32.name = 'Can change write project step model'
    auth_permission_32.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_32.codename = 'change_writeprojectstepmodel'
    auth_permission_32 = importer.save_or_locate(auth_permission_32)

    auth_permission_33 = Permission()
    auth_permission_33.name = 'Can delete click and wait project step model'
    auth_permission_33.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_33.codename = 'delete_clickandwaitprojectstepmodel'
    auth_permission_33 = importer.save_or_locate(auth_permission_33)

    auth_permission_34 = Permission()
    auth_permission_34.name = 'Can delete click project step model'
    auth_permission_34.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_34.codename = 'delete_clickprojectstepmodel'
    auth_permission_34 = importer.save_or_locate(auth_permission_34)

    auth_permission_35 = Permission()
    auth_permission_35.name = 'Can delete open project step model'
    auth_permission_35.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_35.codename = 'delete_openprojectstepmodel'
    auth_permission_35 = importer.save_or_locate(auth_permission_35)

    auth_permission_36 = Permission()
    auth_permission_36.name = 'Can delete project step model'
    auth_permission_36.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_36.codename = 'delete_projectstepmodel'
    auth_permission_36 = importer.save_or_locate(auth_permission_36)

    auth_permission_37 = Permission()
    auth_permission_37.name = 'Can delete store selected value project step model'
    auth_permission_37.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_37.codename = 'delete_storeselectedvalueprojectstepmodel'
    auth_permission_37 = importer.save_or_locate(auth_permission_37)

    auth_permission_38 = Permission()
    auth_permission_38.name = 'Can delete wait project step model'
    auth_permission_38.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_38.codename = 'delete_waitprojectstepmodel'
    auth_permission_38 = importer.save_or_locate(auth_permission_38)

    auth_permission_39 = Permission()
    auth_permission_39.name = 'Can delete write project step model'
    auth_permission_39.content_type = ContentType.objects.get(app_label="botapp", model="projectstepmodel")
    auth_permission_39.codename = 'delete_writeprojectstepmodel'
    auth_permission_39 = importer.save_or_locate(auth_permission_39)

    auth_permission_40 = Permission()
    auth_permission_40.name = 'Can add content type'
    auth_permission_40.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_40.codename = 'add_contenttype'
    auth_permission_40 = importer.save_or_locate(auth_permission_40)

    auth_permission_41 = Permission()
    auth_permission_41.name = 'Can change content type'
    auth_permission_41.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_41.codename = 'change_contenttype'
    auth_permission_41 = importer.save_or_locate(auth_permission_41)

    auth_permission_42 = Permission()
    auth_permission_42.name = 'Can delete content type'
    auth_permission_42.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_42.codename = 'delete_contenttype'
    auth_permission_42 = importer.save_or_locate(auth_permission_42)

    auth_permission_43 = Permission()
    auth_permission_43.name = 'Can add flight price model'
    auth_permission_43.content_type = ContentType.objects.get(app_label="datastore", model="flightpricemodel")
    auth_permission_43.codename = 'add_flightpricemodel'
    auth_permission_43 = importer.save_or_locate(auth_permission_43)

    auth_permission_44 = Permission()
    auth_permission_44.name = 'Can change flight price model'
    auth_permission_44.content_type = ContentType.objects.get(app_label="datastore", model="flightpricemodel")
    auth_permission_44.codename = 'change_flightpricemodel'
    auth_permission_44 = importer.save_or_locate(auth_permission_44)

    auth_permission_45 = Permission()
    auth_permission_45.name = 'Can delete flight price model'
    auth_permission_45.content_type = ContentType.objects.get(app_label="datastore", model="flightpricemodel")
    auth_permission_45.codename = 'delete_flightpricemodel'
    auth_permission_45 = importer.save_or_locate(auth_permission_45)

    auth_permission_46 = Permission()
    auth_permission_46.name = 'Can add journey model'
    auth_permission_46.content_type = ContentType.objects.get(app_label="datastore", model="journeymodel")
    auth_permission_46.codename = 'add_journeymodel'
    auth_permission_46 = importer.save_or_locate(auth_permission_46)

    auth_permission_47 = Permission()
    auth_permission_47.name = 'Can change journey model'
    auth_permission_47.content_type = ContentType.objects.get(app_label="datastore", model="journeymodel")
    auth_permission_47.codename = 'change_journeymodel'
    auth_permission_47 = importer.save_or_locate(auth_permission_47)

    auth_permission_48 = Permission()
    auth_permission_48.name = 'Can delete journey model'
    auth_permission_48.content_type = ContentType.objects.get(app_label="datastore", model="journeymodel")
    auth_permission_48.codename = 'delete_journeymodel'
    auth_permission_48 = importer.save_or_locate(auth_permission_48)

    auth_permission_49 = Permission()
    auth_permission_49.name = 'Can add price per person model'
    auth_permission_49.content_type = ContentType.objects.get(app_label="datastore", model="priceperpersonmodel")
    auth_permission_49.codename = 'add_priceperpersonmodel'
    auth_permission_49 = importer.save_or_locate(auth_permission_49)

    auth_permission_50 = Permission()
    auth_permission_50.name = 'Can change price per person model'
    auth_permission_50.content_type = ContentType.objects.get(app_label="datastore", model="priceperpersonmodel")
    auth_permission_50.codename = 'change_priceperpersonmodel'
    auth_permission_50 = importer.save_or_locate(auth_permission_50)

    auth_permission_51 = Permission()
    auth_permission_51.name = 'Can delete price per person model'
    auth_permission_51.content_type = ContentType.objects.get(app_label="datastore", model="priceperpersonmodel")
    auth_permission_51.codename = 'delete_priceperpersonmodel'
    auth_permission_51 = importer.save_or_locate(auth_permission_51)

    auth_permission_52 = Permission()
    auth_permission_52.name = 'Can add reservation model'
    auth_permission_52.content_type = ContentType.objects.get(app_label="datastore", model="reservationmodel")
    auth_permission_52.codename = 'add_reservationmodel'
    auth_permission_52 = importer.save_or_locate(auth_permission_52)

    auth_permission_53 = Permission()
    auth_permission_53.name = 'Can change reservation model'
    auth_permission_53.content_type = ContentType.objects.get(app_label="datastore", model="reservationmodel")
    auth_permission_53.codename = 'change_reservationmodel'
    auth_permission_53 = importer.save_or_locate(auth_permission_53)

    auth_permission_54 = Permission()
    auth_permission_54.name = 'Can delete reservation model'
    auth_permission_54.content_type = ContentType.objects.get(app_label="datastore", model="reservationmodel")
    auth_permission_54.codename = 'delete_reservationmodel'
    auth_permission_54 = importer.save_or_locate(auth_permission_54)

    auth_permission_55 = Permission()
    auth_permission_55.name = 'Can add route model'
    auth_permission_55.content_type = ContentType.objects.get(app_label="datastore", model="routemodel")
    auth_permission_55.codename = 'add_routemodel'
    auth_permission_55 = importer.save_or_locate(auth_permission_55)

    auth_permission_56 = Permission()
    auth_permission_56.name = 'Can change route model'
    auth_permission_56.content_type = ContentType.objects.get(app_label="datastore", model="routemodel")
    auth_permission_56.codename = 'change_routemodel'
    auth_permission_56 = importer.save_or_locate(auth_permission_56)

    auth_permission_57 = Permission()
    auth_permission_57.name = 'Can delete route model'
    auth_permission_57.content_type = ContentType.objects.get(app_label="datastore", model="routemodel")
    auth_permission_57.codename = 'delete_routemodel'
    auth_permission_57 = importer.save_or_locate(auth_permission_57)

    auth_permission_58 = Permission()
    auth_permission_58.name = 'Can add checker'
    auth_permission_58.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="checker")
    auth_permission_58.codename = 'add_checker'
    auth_permission_58 = importer.save_or_locate(auth_permission_58)

    auth_permission_59 = Permission()
    auth_permission_59.name = 'Can change checker'
    auth_permission_59.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="checker")
    auth_permission_59.codename = 'change_checker'
    auth_permission_59 = importer.save_or_locate(auth_permission_59)

    auth_permission_60 = Permission()
    auth_permission_60.name = 'Can delete checker'
    auth_permission_60.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="checker")
    auth_permission_60.codename = 'delete_checker'
    auth_permission_60 = importer.save_or_locate(auth_permission_60)

    auth_permission_61 = Permission()
    auth_permission_61.name = 'Can add log'
    auth_permission_61.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="log")
    auth_permission_61.codename = 'add_log'
    auth_permission_61 = importer.save_or_locate(auth_permission_61)

    auth_permission_62 = Permission()
    auth_permission_62.name = 'Can change log'
    auth_permission_62.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="log")
    auth_permission_62.codename = 'change_log'
    auth_permission_62 = importer.save_or_locate(auth_permission_62)

    auth_permission_63 = Permission()
    auth_permission_63.name = 'Can delete log'
    auth_permission_63.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="log")
    auth_permission_63.codename = 'delete_log'
    auth_permission_63 = importer.save_or_locate(auth_permission_63)

    auth_permission_64 = Permission()
    auth_permission_64.name = 'Can add log marker'
    auth_permission_64.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="logmarker")
    auth_permission_64.codename = 'add_logmarker'
    auth_permission_64 = importer.save_or_locate(auth_permission_64)

    auth_permission_65 = Permission()
    auth_permission_65.name = 'Can change log marker'
    auth_permission_65.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="logmarker")
    auth_permission_65.codename = 'change_logmarker'
    auth_permission_65 = importer.save_or_locate(auth_permission_65)

    auth_permission_66 = Permission()
    auth_permission_66.name = 'Can delete log marker'
    auth_permission_66.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="logmarker")
    auth_permission_66.codename = 'delete_logmarker'
    auth_permission_66 = importer.save_or_locate(auth_permission_66)

    auth_permission_67 = Permission()
    auth_permission_67.name = 'Can add request page type'
    auth_permission_67.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="requestpagetype")
    auth_permission_67.codename = 'add_requestpagetype'
    auth_permission_67 = importer.save_or_locate(auth_permission_67)

    auth_permission_68 = Permission()
    auth_permission_68.name = 'Can change request page type'
    auth_permission_68.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="requestpagetype")
    auth_permission_68.codename = 'change_requestpagetype'
    auth_permission_68 = importer.save_or_locate(auth_permission_68)

    auth_permission_69 = Permission()
    auth_permission_69.name = 'Can delete request page type'
    auth_permission_69.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="requestpagetype")
    auth_permission_69.codename = 'delete_requestpagetype'
    auth_permission_69 = importer.save_or_locate(auth_permission_69)

    auth_permission_70 = Permission()
    auth_permission_70.name = 'Can add scheduler runtime'
    auth_permission_70.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="schedulerruntime")
    auth_permission_70.codename = 'add_schedulerruntime'
    auth_permission_70 = importer.save_or_locate(auth_permission_70)

    auth_permission_71 = Permission()
    auth_permission_71.name = 'Can change scheduler runtime'
    auth_permission_71.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="schedulerruntime")
    auth_permission_71.codename = 'change_schedulerruntime'
    auth_permission_71 = importer.save_or_locate(auth_permission_71)

    auth_permission_72 = Permission()
    auth_permission_72.name = 'Can delete scheduler runtime'
    auth_permission_72.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="schedulerruntime")
    auth_permission_72.codename = 'delete_schedulerruntime'
    auth_permission_72 = importer.save_or_locate(auth_permission_72)

    auth_permission_73 = Permission()
    auth_permission_73.name = 'Can add scraped obj attr'
    auth_permission_73.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="scrapedobjattr")
    auth_permission_73.codename = 'add_scrapedobjattr'
    auth_permission_73 = importer.save_or_locate(auth_permission_73)

    auth_permission_74 = Permission()
    auth_permission_74.name = 'Can change scraped obj attr'
    auth_permission_74.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="scrapedobjattr")
    auth_permission_74.codename = 'change_scrapedobjattr'
    auth_permission_74 = importer.save_or_locate(auth_permission_74)

    auth_permission_75 = Permission()
    auth_permission_75.name = 'Can delete scraped obj attr'
    auth_permission_75.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="scrapedobjattr")
    auth_permission_75.codename = 'delete_scrapedobjattr'
    auth_permission_75 = importer.save_or_locate(auth_permission_75)

    auth_permission_76 = Permission()
    auth_permission_76.name = 'Can add Scraped object class'
    auth_permission_76.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="scrapedobjclass")
    auth_permission_76.codename = 'add_scrapedobjclass'
    auth_permission_76 = importer.save_or_locate(auth_permission_76)

    auth_permission_77 = Permission()
    auth_permission_77.name = 'Can change Scraped object class'
    auth_permission_77.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="scrapedobjclass")
    auth_permission_77.codename = 'change_scrapedobjclass'
    auth_permission_77 = importer.save_or_locate(auth_permission_77)

    auth_permission_78 = Permission()
    auth_permission_78.name = 'Can delete Scraped object class'
    auth_permission_78.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="scrapedobjclass")
    auth_permission_78.codename = 'delete_scrapedobjclass'
    auth_permission_78 = importer.save_or_locate(auth_permission_78)

    auth_permission_79 = Permission()
    auth_permission_79.name = 'Can add scraper'
    auth_permission_79.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="scraper")
    auth_permission_79.codename = 'add_scraper'
    auth_permission_79 = importer.save_or_locate(auth_permission_79)

    auth_permission_80 = Permission()
    auth_permission_80.name = 'Can change scraper'
    auth_permission_80.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="scraper")
    auth_permission_80.codename = 'change_scraper'
    auth_permission_80 = importer.save_or_locate(auth_permission_80)

    auth_permission_81 = Permission()
    auth_permission_81.name = 'Can delete scraper'
    auth_permission_81.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="scraper")
    auth_permission_81.codename = 'delete_scraper'
    auth_permission_81 = importer.save_or_locate(auth_permission_81)

    auth_permission_82 = Permission()
    auth_permission_82.name = 'Can add scraper elem'
    auth_permission_82.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="scraperelem")
    auth_permission_82.codename = 'add_scraperelem'
    auth_permission_82 = importer.save_or_locate(auth_permission_82)

    auth_permission_83 = Permission()
    auth_permission_83.name = 'Can change scraper elem'
    auth_permission_83.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="scraperelem")
    auth_permission_83.codename = 'change_scraperelem'
    auth_permission_83 = importer.save_or_locate(auth_permission_83)

    auth_permission_84 = Permission()
    auth_permission_84.name = 'Can delete scraper elem'
    auth_permission_84.content_type = ContentType.objects.get(app_label="dynamic_scraper", model="scraperelem")
    auth_permission_84.codename = 'delete_scraperelem'
    auth_permission_84 = importer.save_or_locate(auth_permission_84)

    auth_permission_85 = Permission()
    auth_permission_85.name = 'Can add module'
    auth_permission_85.content_type = ContentType.objects.get(app_label="frontend", model="module")
    auth_permission_85.codename = 'add_module'
    auth_permission_85 = importer.save_or_locate(auth_permission_85)

    auth_permission_86 = Permission()
    auth_permission_86.name = 'Can change module'
    auth_permission_86.content_type = ContentType.objects.get(app_label="frontend", model="module")
    auth_permission_86.codename = 'change_module'
    auth_permission_86 = importer.save_or_locate(auth_permission_86)

    auth_permission_87 = Permission()
    auth_permission_87.name = 'Can delete module'
    auth_permission_87.content_type = ContentType.objects.get(app_label="frontend", model="module")
    auth_permission_87.codename = 'delete_module'
    auth_permission_87 = importer.save_or_locate(auth_permission_87)

    auth_permission_88 = Permission()
    auth_permission_88.name = 'Can add airport model'
    auth_permission_88.content_type = ContentType.objects.get(app_label="mdm", model="airportmodel")
    auth_permission_88.codename = 'add_airportmodel'
    auth_permission_88 = importer.save_or_locate(auth_permission_88)

    auth_permission_89 = Permission()
    auth_permission_89.name = 'Can change airport model'
    auth_permission_89.content_type = ContentType.objects.get(app_label="mdm", model="airportmodel")
    auth_permission_89.codename = 'change_airportmodel'
    auth_permission_89 = importer.save_or_locate(auth_permission_89)

    auth_permission_90 = Permission()
    auth_permission_90.name = 'Can delete airport model'
    auth_permission_90.content_type = ContentType.objects.get(app_label="mdm", model="airportmodel")
    auth_permission_90.codename = 'delete_airportmodel'
    auth_permission_90 = importer.save_or_locate(auth_permission_90)

    auth_permission_91 = Permission()
    auth_permission_91.name = 'Can add bag type model'
    auth_permission_91.content_type = ContentType.objects.get(app_label="mdm", model="bagtypemodel")
    auth_permission_91.codename = 'add_bagtypemodel'
    auth_permission_91 = importer.save_or_locate(auth_permission_91)

    auth_permission_92 = Permission()
    auth_permission_92.name = 'Can change bag type model'
    auth_permission_92.content_type = ContentType.objects.get(app_label="mdm", model="bagtypemodel")
    auth_permission_92.codename = 'change_bagtypemodel'
    auth_permission_92 = importer.save_or_locate(auth_permission_92)

    auth_permission_93 = Permission()
    auth_permission_93.name = 'Can delete bag type model'
    auth_permission_93.content_type = ContentType.objects.get(app_label="mdm", model="bagtypemodel")
    auth_permission_93.codename = 'delete_bagtypemodel'
    auth_permission_93 = importer.save_or_locate(auth_permission_93)

    auth_permission_94 = Permission()
    auth_permission_94.name = 'Can add board model'
    auth_permission_94.content_type = ContentType.objects.get(app_label="mdm", model="boardmodel")
    auth_permission_94.codename = 'add_boardmodel'
    auth_permission_94 = importer.save_or_locate(auth_permission_94)

    auth_permission_95 = Permission()
    auth_permission_95.name = 'Can change board model'
    auth_permission_95.content_type = ContentType.objects.get(app_label="mdm", model="boardmodel")
    auth_permission_95.codename = 'change_boardmodel'
    auth_permission_95 = importer.save_or_locate(auth_permission_95)

    auth_permission_96 = Permission()
    auth_permission_96.name = 'Can delete board model'
    auth_permission_96.content_type = ContentType.objects.get(app_label="mdm", model="boardmodel")
    auth_permission_96.codename = 'delete_boardmodel'
    auth_permission_96 = importer.save_or_locate(auth_permission_96)

    auth_permission_97 = Permission()
    auth_permission_97.name = 'Can add entity model'
    auth_permission_97.content_type = ContentType.objects.get(app_label="mdm", model="entitymodel")
    auth_permission_97.codename = 'add_entitymodel'
    auth_permission_97 = importer.save_or_locate(auth_permission_97)

    auth_permission_98 = Permission()
    auth_permission_98.name = 'Can change entity model'
    auth_permission_98.content_type = ContentType.objects.get(app_label="mdm", model="entitymodel")
    auth_permission_98.codename = 'change_entitymodel'
    auth_permission_98 = importer.save_or_locate(auth_permission_98)

    auth_permission_99 = Permission()
    auth_permission_99.name = 'Can delete entity model'
    auth_permission_99.content_type = ContentType.objects.get(app_label="mdm", model="entitymodel")
    auth_permission_99.codename = 'delete_entitymodel'
    auth_permission_99 = importer.save_or_locate(auth_permission_99)

    auth_permission_100 = Permission()
    auth_permission_100.name = 'Can add flight provider model'
    auth_permission_100.content_type = ContentType.objects.get(app_label="mdm", model="flightprovidermodel")
    auth_permission_100.codename = 'add_flightprovidermodel'
    auth_permission_100 = importer.save_or_locate(auth_permission_100)

    auth_permission_101 = Permission()
    auth_permission_101.name = 'Can change flight provider model'
    auth_permission_101.content_type = ContentType.objects.get(app_label="mdm", model="flightprovidermodel")
    auth_permission_101.codename = 'change_flightprovidermodel'
    auth_permission_101 = importer.save_or_locate(auth_permission_101)

    auth_permission_102 = Permission()
    auth_permission_102.name = 'Can delete flight provider model'
    auth_permission_102.content_type = ContentType.objects.get(app_label="mdm", model="flightprovidermodel")
    auth_permission_102.codename = 'delete_flightprovidermodel'
    auth_permission_102 = importer.save_or_locate(auth_permission_102)

    auth_permission_103 = Permission()
    auth_permission_103.name = 'Can add hotel model'
    auth_permission_103.content_type = ContentType.objects.get(app_label="mdm", model="hotelmodel")
    auth_permission_103.codename = 'add_hotelmodel'
    auth_permission_103 = importer.save_or_locate(auth_permission_103)

    auth_permission_104 = Permission()
    auth_permission_104.name = 'Can change hotel model'
    auth_permission_104.content_type = ContentType.objects.get(app_label="mdm", model="hotelmodel")
    auth_permission_104.codename = 'change_hotelmodel'
    auth_permission_104 = importer.save_or_locate(auth_permission_104)

    auth_permission_105 = Permission()
    auth_permission_105.name = 'Can delete hotel model'
    auth_permission_105.content_type = ContentType.objects.get(app_label="mdm", model="hotelmodel")
    auth_permission_105.codename = 'delete_hotelmodel'
    auth_permission_105 = importer.save_or_locate(auth_permission_105)

    auth_permission_106 = Permission()
    auth_permission_106.name = 'Can add market model'
    auth_permission_106.content_type = ContentType.objects.get(app_label="mdm", model="marketmodel")
    auth_permission_106.codename = 'add_marketmodel'
    auth_permission_106 = importer.save_or_locate(auth_permission_106)

    auth_permission_107 = Permission()
    auth_permission_107.name = 'Can change market model'
    auth_permission_107.content_type = ContentType.objects.get(app_label="mdm", model="marketmodel")
    auth_permission_107.codename = 'change_marketmodel'
    auth_permission_107 = importer.save_or_locate(auth_permission_107)

    auth_permission_108 = Permission()
    auth_permission_108.name = 'Can delete market model'
    auth_permission_108.content_type = ContentType.objects.get(app_label="mdm", model="marketmodel")
    auth_permission_108.codename = 'delete_marketmodel'
    auth_permission_108 = importer.save_or_locate(auth_permission_108)

    auth_permission_109 = Permission()
    auth_permission_109.name = 'Can add room type model'
    auth_permission_109.content_type = ContentType.objects.get(app_label="mdm", model="roomtypemodel")
    auth_permission_109.codename = 'add_roomtypemodel'
    auth_permission_109 = importer.save_or_locate(auth_permission_109)

    auth_permission_110 = Permission()
    auth_permission_110.name = 'Can change room type model'
    auth_permission_110.content_type = ContentType.objects.get(app_label="mdm", model="roomtypemodel")
    auth_permission_110.codename = 'change_roomtypemodel'
    auth_permission_110 = importer.save_or_locate(auth_permission_110)

    auth_permission_111 = Permission()
    auth_permission_111.name = 'Can delete room type model'
    auth_permission_111.content_type = ContentType.objects.get(app_label="mdm", model="roomtypemodel")
    auth_permission_111.codename = 'delete_roomtypemodel'
    auth_permission_111 = importer.save_or_locate(auth_permission_111)

    auth_permission_112 = Permission()
    auth_permission_112.name = 'Can add supplier model'
    auth_permission_112.content_type = ContentType.objects.get(app_label="mdm", model="suppliermodel")
    auth_permission_112.codename = 'add_suppliermodel'
    auth_permission_112 = importer.save_or_locate(auth_permission_112)

    auth_permission_113 = Permission()
    auth_permission_113.name = 'Can change supplier model'
    auth_permission_113.content_type = ContentType.objects.get(app_label="mdm", model="suppliermodel")
    auth_permission_113.codename = 'change_suppliermodel'
    auth_permission_113 = importer.save_or_locate(auth_permission_113)

    auth_permission_114 = Permission()
    auth_permission_114.name = 'Can delete supplier model'
    auth_permission_114.content_type = ContentType.objects.get(app_label="mdm", model="suppliermodel")
    auth_permission_114.codename = 'delete_suppliermodel'
    auth_permission_114 = importer.save_or_locate(auth_permission_114)

    auth_permission_115 = Permission()
    auth_permission_115.name = 'Can add display field'
    auth_permission_115.content_type = ContentType.objects.get(app_label="report_builder", model="displayfield")
    auth_permission_115.codename = 'add_displayfield'
    auth_permission_115 = importer.save_or_locate(auth_permission_115)

    auth_permission_116 = Permission()
    auth_permission_116.name = 'Can change display field'
    auth_permission_116.content_type = ContentType.objects.get(app_label="report_builder", model="displayfield")
    auth_permission_116.codename = 'change_displayfield'
    auth_permission_116 = importer.save_or_locate(auth_permission_116)

    auth_permission_117 = Permission()
    auth_permission_117.name = 'Can delete display field'
    auth_permission_117.content_type = ContentType.objects.get(app_label="report_builder", model="displayfield")
    auth_permission_117.codename = 'delete_displayfield'
    auth_permission_117 = importer.save_or_locate(auth_permission_117)

    auth_permission_118 = Permission()
    auth_permission_118.name = 'Can add filter field'
    auth_permission_118.content_type = ContentType.objects.get(app_label="report_builder", model="filterfield")
    auth_permission_118.codename = 'add_filterfield'
    auth_permission_118 = importer.save_or_locate(auth_permission_118)

    auth_permission_119 = Permission()
    auth_permission_119.name = 'Can change filter field'
    auth_permission_119.content_type = ContentType.objects.get(app_label="report_builder", model="filterfield")
    auth_permission_119.codename = 'change_filterfield'
    auth_permission_119 = importer.save_or_locate(auth_permission_119)

    auth_permission_120 = Permission()
    auth_permission_120.name = 'Can delete filter field'
    auth_permission_120.content_type = ContentType.objects.get(app_label="report_builder", model="filterfield")
    auth_permission_120.codename = 'delete_filterfield'
    auth_permission_120 = importer.save_or_locate(auth_permission_120)

    auth_permission_121 = Permission()
    auth_permission_121.name = 'Can add format'
    auth_permission_121.content_type = ContentType.objects.get(app_label="report_builder", model="format")
    auth_permission_121.codename = 'add_format'
    auth_permission_121 = importer.save_or_locate(auth_permission_121)

    auth_permission_122 = Permission()
    auth_permission_122.name = 'Can change format'
    auth_permission_122.content_type = ContentType.objects.get(app_label="report_builder", model="format")
    auth_permission_122.codename = 'change_format'
    auth_permission_122 = importer.save_or_locate(auth_permission_122)

    auth_permission_123 = Permission()
    auth_permission_123.name = 'Can delete format'
    auth_permission_123.content_type = ContentType.objects.get(app_label="report_builder", model="format")
    auth_permission_123.codename = 'delete_format'
    auth_permission_123 = importer.save_or_locate(auth_permission_123)

    auth_permission_124 = Permission()
    auth_permission_124.name = 'Can add report'
    auth_permission_124.content_type = ContentType.objects.get(app_label="report_builder", model="report")
    auth_permission_124.codename = 'add_report'
    auth_permission_124 = importer.save_or_locate(auth_permission_124)

    auth_permission_125 = Permission()
    auth_permission_125.name = 'Can change report'
    auth_permission_125.content_type = ContentType.objects.get(app_label="report_builder", model="report")
    auth_permission_125.codename = 'change_report'
    auth_permission_125 = importer.save_or_locate(auth_permission_125)

    auth_permission_126 = Permission()
    auth_permission_126.name = 'Can delete report'
    auth_permission_126.content_type = ContentType.objects.get(app_label="report_builder", model="report")
    auth_permission_126.codename = 'delete_report'
    auth_permission_126 = importer.save_or_locate(auth_permission_126)

    auth_permission_127 = Permission()
    auth_permission_127.name = 'Can add my model'
    auth_permission_127.content_type = ContentType.objects.get(app_label="reportsapp", model="mymodel")
    auth_permission_127.codename = 'add_mymodel'
    auth_permission_127 = importer.save_or_locate(auth_permission_127)

    auth_permission_128 = Permission()
    auth_permission_128.name = 'Can change my model'
    auth_permission_128.content_type = ContentType.objects.get(app_label="reportsapp", model="mymodel")
    auth_permission_128.codename = 'change_mymodel'
    auth_permission_128 = importer.save_or_locate(auth_permission_128)

    auth_permission_129 = Permission()
    auth_permission_129.name = 'Can delete my model'
    auth_permission_129.content_type = ContentType.objects.get(app_label="reportsapp", model="mymodel")
    auth_permission_129.codename = 'delete_mymodel'
    auth_permission_129 = importer.save_or_locate(auth_permission_129)

    auth_permission_130 = Permission()
    auth_permission_130.name = 'Can add report model'
    auth_permission_130.content_type = ContentType.objects.get(app_label="reportsapp", model="reportmodel")
    auth_permission_130.codename = 'add_reportmodel'
    auth_permission_130 = importer.save_or_locate(auth_permission_130)

    auth_permission_131 = Permission()
    auth_permission_131.name = 'Can change report model'
    auth_permission_131.content_type = ContentType.objects.get(app_label="reportsapp", model="reportmodel")
    auth_permission_131.codename = 'change_reportmodel'
    auth_permission_131 = importer.save_or_locate(auth_permission_131)

    auth_permission_132 = Permission()
    auth_permission_132.name = 'Can delete report model'
    auth_permission_132.content_type = ContentType.objects.get(app_label="reportsapp", model="reportmodel")
    auth_permission_132.codename = 'delete_reportmodel'
    auth_permission_132 = importer.save_or_locate(auth_permission_132)

    auth_permission_133 = Permission()
    auth_permission_133.name = 'Can add session'
    auth_permission_133.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_133.codename = 'add_session'
    auth_permission_133 = importer.save_or_locate(auth_permission_133)

    auth_permission_134 = Permission()
    auth_permission_134.name = 'Can change session'
    auth_permission_134.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_134.codename = 'change_session'
    auth_permission_134 = importer.save_or_locate(auth_permission_134)

    auth_permission_135 = Permission()
    auth_permission_135.name = 'Can delete session'
    auth_permission_135.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_135.codename = 'delete_session'
    auth_permission_135 = importer.save_or_locate(auth_permission_135)

    # Processing model: django.contrib.auth.models.Group

    from django.contrib.auth.models import Group


    # Processing model: django.contrib.auth.models.User

    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.password = 'pbkdf2_sha256$36000$DaY6zYgiiRQ7$EBLvV7KOwD4/wQOJWJRmRMge+WlVkJB5ZewrFzmYctE='
    auth_user_1.last_login = None
    auth_user_1.is_superuser = True
    auth_user_1.username = 'lordoftheflies'
    auth_user_1.first_name = ''
    auth_user_1.last_name = ''
    auth_user_1.email = 'laszlo.hegedus@cherubits.hu'
    auth_user_1.is_staff = True
    auth_user_1.is_active = True
    auth_user_1.date_joined = dateutil.parser.parse("2017-09-10T22:46:45.942555+00:00")
    auth_user_1 = importer.save_or_locate(auth_user_1)

