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
# ../manage.py dumpscript auth
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
    auth_permission_1.name = 'Can add email address'
    auth_permission_1.content_type = ContentType.objects.get(app_label="account", model="emailaddress")
    auth_permission_1.codename = 'add_emailaddress'
    auth_permission_1 = importer.save_or_locate(auth_permission_1)

    auth_permission_2 = Permission()
    auth_permission_2.name = 'Can change email address'
    auth_permission_2.content_type = ContentType.objects.get(app_label="account", model="emailaddress")
    auth_permission_2.codename = 'change_emailaddress'
    auth_permission_2 = importer.save_or_locate(auth_permission_2)

    auth_permission_3 = Permission()
    auth_permission_3.name = 'Can delete email address'
    auth_permission_3.content_type = ContentType.objects.get(app_label="account", model="emailaddress")
    auth_permission_3.codename = 'delete_emailaddress'
    auth_permission_3 = importer.save_or_locate(auth_permission_3)

    auth_permission_4 = Permission()
    auth_permission_4.name = 'Can view email address'
    auth_permission_4.content_type = ContentType.objects.get(app_label="account", model="emailaddress")
    auth_permission_4.codename = 'view_emailaddress'
    auth_permission_4 = importer.save_or_locate(auth_permission_4)

    auth_permission_5 = Permission()
    auth_permission_5.name = 'Can add email confirmation'
    auth_permission_5.content_type = ContentType.objects.get(app_label="account", model="emailconfirmation")
    auth_permission_5.codename = 'add_emailconfirmation'
    auth_permission_5 = importer.save_or_locate(auth_permission_5)

    auth_permission_6 = Permission()
    auth_permission_6.name = 'Can change email confirmation'
    auth_permission_6.content_type = ContentType.objects.get(app_label="account", model="emailconfirmation")
    auth_permission_6.codename = 'change_emailconfirmation'
    auth_permission_6 = importer.save_or_locate(auth_permission_6)

    auth_permission_7 = Permission()
    auth_permission_7.name = 'Can delete email confirmation'
    auth_permission_7.content_type = ContentType.objects.get(app_label="account", model="emailconfirmation")
    auth_permission_7.codename = 'delete_emailconfirmation'
    auth_permission_7 = importer.save_or_locate(auth_permission_7)

    auth_permission_8 = Permission()
    auth_permission_8.name = 'Can view email confirmation'
    auth_permission_8.content_type = ContentType.objects.get(app_label="account", model="emailconfirmation")
    auth_permission_8.codename = 'view_emailconfirmation'
    auth_permission_8 = importer.save_or_locate(auth_permission_8)

    auth_permission_9 = Permission()
    auth_permission_9.name = 'Can add log entry'
    auth_permission_9.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_9.codename = 'add_logentry'
    auth_permission_9 = importer.save_or_locate(auth_permission_9)

    auth_permission_10 = Permission()
    auth_permission_10.name = 'Can change log entry'
    auth_permission_10.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_10.codename = 'change_logentry'
    auth_permission_10 = importer.save_or_locate(auth_permission_10)

    auth_permission_11 = Permission()
    auth_permission_11.name = 'Can delete log entry'
    auth_permission_11.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_11.codename = 'delete_logentry'
    auth_permission_11 = importer.save_or_locate(auth_permission_11)

    auth_permission_12 = Permission()
    auth_permission_12.name = 'Can view log entry'
    auth_permission_12.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_12.codename = 'view_logentry'
    auth_permission_12 = importer.save_or_locate(auth_permission_12)

    auth_permission_13 = Permission()
    auth_permission_13.name = 'Can add social account'
    auth_permission_13.content_type = ContentType.objects.get(app_label="allauth", model="socialaccount")
    auth_permission_13.codename = 'add_socialaccount'
    auth_permission_13 = importer.save_or_locate(auth_permission_13)

    auth_permission_14 = Permission()
    auth_permission_14.name = 'Can change social account'
    auth_permission_14.content_type = ContentType.objects.get(app_label="allauth", model="socialaccount")
    auth_permission_14.codename = 'change_socialaccount'
    auth_permission_14 = importer.save_or_locate(auth_permission_14)

    auth_permission_15 = Permission()
    auth_permission_15.name = 'Can delete social account'
    auth_permission_15.content_type = ContentType.objects.get(app_label="allauth", model="socialaccount")
    auth_permission_15.codename = 'delete_socialaccount'
    auth_permission_15 = importer.save_or_locate(auth_permission_15)

    auth_permission_16 = Permission()
    auth_permission_16.name = 'Can view social account'
    auth_permission_16.content_type = ContentType.objects.get(app_label="allauth", model="socialaccount")
    auth_permission_16.codename = 'view_socialaccount'
    auth_permission_16 = importer.save_or_locate(auth_permission_16)

    auth_permission_17 = Permission()
    auth_permission_17.name = 'Can add social application'
    auth_permission_17.content_type = ContentType.objects.get(app_label="allauth", model="socialapp")
    auth_permission_17.codename = 'add_socialapp'
    auth_permission_17 = importer.save_or_locate(auth_permission_17)

    auth_permission_18 = Permission()
    auth_permission_18.name = 'Can change social application'
    auth_permission_18.content_type = ContentType.objects.get(app_label="allauth", model="socialapp")
    auth_permission_18.codename = 'change_socialapp'
    auth_permission_18 = importer.save_or_locate(auth_permission_18)

    auth_permission_19 = Permission()
    auth_permission_19.name = 'Can delete social application'
    auth_permission_19.content_type = ContentType.objects.get(app_label="allauth", model="socialapp")
    auth_permission_19.codename = 'delete_socialapp'
    auth_permission_19 = importer.save_or_locate(auth_permission_19)

    auth_permission_20 = Permission()
    auth_permission_20.name = 'Can view social application'
    auth_permission_20.content_type = ContentType.objects.get(app_label="allauth", model="socialapp")
    auth_permission_20.codename = 'view_socialapp'
    auth_permission_20 = importer.save_or_locate(auth_permission_20)

    auth_permission_21 = Permission()
    auth_permission_21.name = 'Can add social application token'
    auth_permission_21.content_type = ContentType.objects.get(app_label="allauth", model="socialtoken")
    auth_permission_21.codename = 'add_socialtoken'
    auth_permission_21 = importer.save_or_locate(auth_permission_21)

    auth_permission_22 = Permission()
    auth_permission_22.name = 'Can change social application token'
    auth_permission_22.content_type = ContentType.objects.get(app_label="allauth", model="socialtoken")
    auth_permission_22.codename = 'change_socialtoken'
    auth_permission_22 = importer.save_or_locate(auth_permission_22)

    auth_permission_23 = Permission()
    auth_permission_23.name = 'Can delete social application token'
    auth_permission_23.content_type = ContentType.objects.get(app_label="allauth", model="socialtoken")
    auth_permission_23.codename = 'delete_socialtoken'
    auth_permission_23 = importer.save_or_locate(auth_permission_23)

    auth_permission_24 = Permission()
    auth_permission_24.name = 'Can view social application token'
    auth_permission_24.content_type = ContentType.objects.get(app_label="allauth", model="socialtoken")
    auth_permission_24.codename = 'view_socialtoken'
    auth_permission_24 = importer.save_or_locate(auth_permission_24)

    auth_permission_25 = Permission()
    auth_permission_25.name = 'Can add group'
    auth_permission_25.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_25.codename = 'add_group'
    auth_permission_25 = importer.save_or_locate(auth_permission_25)

    auth_permission_26 = Permission()
    auth_permission_26.name = 'Can change group'
    auth_permission_26.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_26.codename = 'change_group'
    auth_permission_26 = importer.save_or_locate(auth_permission_26)

    auth_permission_27 = Permission()
    auth_permission_27.name = 'Can delete group'
    auth_permission_27.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_27.codename = 'delete_group'
    auth_permission_27 = importer.save_or_locate(auth_permission_27)

    auth_permission_28 = Permission()
    auth_permission_28.name = 'Can view group'
    auth_permission_28.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_28.codename = 'view_group'
    auth_permission_28 = importer.save_or_locate(auth_permission_28)

    auth_permission_29 = Permission()
    auth_permission_29.name = 'Can add permission'
    auth_permission_29.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_29.codename = 'add_permission'
    auth_permission_29 = importer.save_or_locate(auth_permission_29)

    auth_permission_30 = Permission()
    auth_permission_30.name = 'Can change permission'
    auth_permission_30.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_30.codename = 'change_permission'
    auth_permission_30 = importer.save_or_locate(auth_permission_30)

    auth_permission_31 = Permission()
    auth_permission_31.name = 'Can delete permission'
    auth_permission_31.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_31.codename = 'delete_permission'
    auth_permission_31 = importer.save_or_locate(auth_permission_31)

    auth_permission_32 = Permission()
    auth_permission_32.name = 'Can view permission'
    auth_permission_32.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_32.codename = 'view_permission'
    auth_permission_32 = importer.save_or_locate(auth_permission_32)

    auth_permission_33 = Permission()
    auth_permission_33.name = 'Can add user'
    auth_permission_33.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_33.codename = 'add_user'
    auth_permission_33 = importer.save_or_locate(auth_permission_33)

    auth_permission_34 = Permission()
    auth_permission_34.name = 'Can change user'
    auth_permission_34.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_34.codename = 'change_user'
    auth_permission_34 = importer.save_or_locate(auth_permission_34)

    auth_permission_35 = Permission()
    auth_permission_35.name = 'Can delete user'
    auth_permission_35.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_35.codename = 'delete_user'
    auth_permission_35 = importer.save_or_locate(auth_permission_35)

    auth_permission_36 = Permission()
    auth_permission_36.name = 'Can view user'
    auth_permission_36.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_36.codename = 'view_user'
    auth_permission_36 = importer.save_or_locate(auth_permission_36)

    auth_permission_37 = Permission()
    auth_permission_37.name = 'Can add Token'
    auth_permission_37.content_type = ContentType.objects.get(app_label="authtoken", model="token")
    auth_permission_37.codename = 'add_token'
    auth_permission_37 = importer.save_or_locate(auth_permission_37)

    auth_permission_38 = Permission()
    auth_permission_38.name = 'Can change Token'
    auth_permission_38.content_type = ContentType.objects.get(app_label="authtoken", model="token")
    auth_permission_38.codename = 'change_token'
    auth_permission_38 = importer.save_or_locate(auth_permission_38)

    auth_permission_39 = Permission()
    auth_permission_39.name = 'Can delete Token'
    auth_permission_39.content_type = ContentType.objects.get(app_label="authtoken", model="token")
    auth_permission_39.codename = 'delete_token'
    auth_permission_39 = importer.save_or_locate(auth_permission_39)

    auth_permission_40 = Permission()
    auth_permission_40.name = 'Can view Token'
    auth_permission_40.content_type = ContentType.objects.get(app_label="authtoken", model="token")
    auth_permission_40.codename = 'view_token'
    auth_permission_40 = importer.save_or_locate(auth_permission_40)

    auth_permission_41 = Permission()
    auth_permission_41.name = 'Can add content type'
    auth_permission_41.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_41.codename = 'add_contenttype'
    auth_permission_41 = importer.save_or_locate(auth_permission_41)

    auth_permission_42 = Permission()
    auth_permission_42.name = 'Can change content type'
    auth_permission_42.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_42.codename = 'change_contenttype'
    auth_permission_42 = importer.save_or_locate(auth_permission_42)

    auth_permission_43 = Permission()
    auth_permission_43.name = 'Can delete content type'
    auth_permission_43.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_43.codename = 'delete_contenttype'
    auth_permission_43 = importer.save_or_locate(auth_permission_43)

    auth_permission_44 = Permission()
    auth_permission_44.name = 'Can view content type'
    auth_permission_44.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_44.codename = 'view_contenttype'
    auth_permission_44 = importer.save_or_locate(auth_permission_44)

    auth_permission_45 = Permission()
    auth_permission_45.name = 'Can add Dataset'
    auth_permission_45.content_type = ContentType.objects.get(app_label="datastore", model="datasetmodel")
    auth_permission_45.codename = 'add_datasetmodel'
    auth_permission_45 = importer.save_or_locate(auth_permission_45)

    auth_permission_46 = Permission()
    auth_permission_46.name = 'Can change Dataset'
    auth_permission_46.content_type = ContentType.objects.get(app_label="datastore", model="datasetmodel")
    auth_permission_46.codename = 'change_datasetmodel'
    auth_permission_46 = importer.save_or_locate(auth_permission_46)

    auth_permission_47 = Permission()
    auth_permission_47.name = 'Can delete Dataset'
    auth_permission_47.content_type = ContentType.objects.get(app_label="datastore", model="datasetmodel")
    auth_permission_47.codename = 'delete_datasetmodel'
    auth_permission_47 = importer.save_or_locate(auth_permission_47)

    auth_permission_48 = Permission()
    auth_permission_48.name = 'Can view Dataset'
    auth_permission_48.content_type = ContentType.objects.get(app_label="datastore", model="datasetmodel")
    auth_permission_48.codename = 'view_datasetmodel'
    auth_permission_48 = importer.save_or_locate(auth_permission_48)

    auth_permission_49 = Permission()
    auth_permission_49.name = 'Can add Entry'
    auth_permission_49.content_type = ContentType.objects.get(app_label="datastore", model="entrymodel")
    auth_permission_49.codename = 'add_entrymodel'
    auth_permission_49 = importer.save_or_locate(auth_permission_49)

    auth_permission_50 = Permission()
    auth_permission_50.name = 'Can change Entry'
    auth_permission_50.content_type = ContentType.objects.get(app_label="datastore", model="entrymodel")
    auth_permission_50.codename = 'change_entrymodel'
    auth_permission_50 = importer.save_or_locate(auth_permission_50)

    auth_permission_51 = Permission()
    auth_permission_51.name = 'Can delete Entry'
    auth_permission_51.content_type = ContentType.objects.get(app_label="datastore", model="entrymodel")
    auth_permission_51.codename = 'delete_entrymodel'
    auth_permission_51 = importer.save_or_locate(auth_permission_51)

    auth_permission_52 = Permission()
    auth_permission_52.name = 'Can view Entry'
    auth_permission_52.content_type = ContentType.objects.get(app_label="datastore", model="entrymodel")
    auth_permission_52.codename = 'view_entrymodel'
    auth_permission_52 = importer.save_or_locate(auth_permission_52)

    auth_permission_53 = Permission()
    auth_permission_53.name = 'Can add schema model'
    auth_permission_53.content_type = ContentType.objects.get(app_label="datastore", model="schemamodel")
    auth_permission_53.codename = 'add_schemamodel'
    auth_permission_53 = importer.save_or_locate(auth_permission_53)

    auth_permission_54 = Permission()
    auth_permission_54.name = 'Can change schema model'
    auth_permission_54.content_type = ContentType.objects.get(app_label="datastore", model="schemamodel")
    auth_permission_54.codename = 'change_schemamodel'
    auth_permission_54 = importer.save_or_locate(auth_permission_54)

    auth_permission_55 = Permission()
    auth_permission_55.name = 'Can delete schema model'
    auth_permission_55.content_type = ContentType.objects.get(app_label="datastore", model="schemamodel")
    auth_permission_55.codename = 'delete_schemamodel'
    auth_permission_55 = importer.save_or_locate(auth_permission_55)

    auth_permission_56 = Permission()
    auth_permission_56.name = 'Can view schema model'
    auth_permission_56.content_type = ContentType.objects.get(app_label="datastore", model="schemamodel")
    auth_permission_56.codename = 'view_schemamodel'
    auth_permission_56 = importer.save_or_locate(auth_permission_56)

    auth_permission_57 = Permission()
    auth_permission_57.name = 'Can add Argument'
    auth_permission_57.content_type = ContentType.objects.get(app_label="engine", model="argumentmodel")
    auth_permission_57.codename = 'add_argumentmodel'
    auth_permission_57 = importer.save_or_locate(auth_permission_57)

    auth_permission_58 = Permission()
    auth_permission_58.name = 'Can change Argument'
    auth_permission_58.content_type = ContentType.objects.get(app_label="engine", model="argumentmodel")
    auth_permission_58.codename = 'change_argumentmodel'
    auth_permission_58 = importer.save_or_locate(auth_permission_58)

    auth_permission_59 = Permission()
    auth_permission_59.name = 'Can delete Argument'
    auth_permission_59.content_type = ContentType.objects.get(app_label="engine", model="argumentmodel")
    auth_permission_59.codename = 'delete_argumentmodel'
    auth_permission_59 = importer.save_or_locate(auth_permission_59)

    auth_permission_60 = Permission()
    auth_permission_60.name = 'Can view Argument'
    auth_permission_60.content_type = ContentType.objects.get(app_label="engine", model="argumentmodel")
    auth_permission_60.codename = 'view_argumentmodel'
    auth_permission_60 = importer.save_or_locate(auth_permission_60)

    auth_permission_61 = Permission()
    auth_permission_61.name = 'Can add execution model'
    auth_permission_61.content_type = ContentType.objects.get(app_label="engine", model="executionmodel")
    auth_permission_61.codename = 'add_executionmodel'
    auth_permission_61 = importer.save_or_locate(auth_permission_61)

    auth_permission_62 = Permission()
    auth_permission_62.name = 'Can change execution model'
    auth_permission_62.content_type = ContentType.objects.get(app_label="engine", model="executionmodel")
    auth_permission_62.codename = 'change_executionmodel'
    auth_permission_62 = importer.save_or_locate(auth_permission_62)

    auth_permission_63 = Permission()
    auth_permission_63.name = 'Can delete execution model'
    auth_permission_63.content_type = ContentType.objects.get(app_label="engine", model="executionmodel")
    auth_permission_63.codename = 'delete_executionmodel'
    auth_permission_63 = importer.save_or_locate(auth_permission_63)

    auth_permission_64 = Permission()
    auth_permission_64.name = 'Can view execution model'
    auth_permission_64.content_type = ContentType.objects.get(app_label="engine", model="executionmodel")
    auth_permission_64.codename = 'view_executionmodel'
    auth_permission_64 = importer.save_or_locate(auth_permission_64)

    auth_permission_65 = Permission()
    auth_permission_65.name = 'Can add Process'
    auth_permission_65.content_type = ContentType.objects.get(app_label="engine", model="processmodel")
    auth_permission_65.codename = 'add_processmodel'
    auth_permission_65 = importer.save_or_locate(auth_permission_65)

    auth_permission_66 = Permission()
    auth_permission_66.name = 'Can change Process'
    auth_permission_66.content_type = ContentType.objects.get(app_label="engine", model="processmodel")
    auth_permission_66.codename = 'change_processmodel'
    auth_permission_66 = importer.save_or_locate(auth_permission_66)

    auth_permission_67 = Permission()
    auth_permission_67.name = 'Can delete Process'
    auth_permission_67.content_type = ContentType.objects.get(app_label="engine", model="processmodel")
    auth_permission_67.codename = 'delete_processmodel'
    auth_permission_67 = importer.save_or_locate(auth_permission_67)

    auth_permission_68 = Permission()
    auth_permission_68.name = 'Can view Process'
    auth_permission_68.content_type = ContentType.objects.get(app_label="engine", model="processmodel")
    auth_permission_68.codename = 'view_processmodel'
    auth_permission_68 = importer.save_or_locate(auth_permission_68)

    auth_permission_69 = Permission()
    auth_permission_69.name = 'Can add Airport'
    auth_permission_69.content_type = ContentType.objects.get(app_label="mdm", model="airportmodel")
    auth_permission_69.codename = 'add_airportmodel'
    auth_permission_69 = importer.save_or_locate(auth_permission_69)

    auth_permission_70 = Permission()
    auth_permission_70.name = 'Can change Airport'
    auth_permission_70.content_type = ContentType.objects.get(app_label="mdm", model="airportmodel")
    auth_permission_70.codename = 'change_airportmodel'
    auth_permission_70 = importer.save_or_locate(auth_permission_70)

    auth_permission_71 = Permission()
    auth_permission_71.name = 'Can delete Airport'
    auth_permission_71.content_type = ContentType.objects.get(app_label="mdm", model="airportmodel")
    auth_permission_71.codename = 'delete_airportmodel'
    auth_permission_71 = importer.save_or_locate(auth_permission_71)

    auth_permission_72 = Permission()
    auth_permission_72.name = 'Can view Airport'
    auth_permission_72.content_type = ContentType.objects.get(app_label="mdm", model="airportmodel")
    auth_permission_72.codename = 'view_airportmodel'
    auth_permission_72 = importer.save_or_locate(auth_permission_72)

    auth_permission_73 = Permission()
    auth_permission_73.name = 'Can add Bagtype'
    auth_permission_73.content_type = ContentType.objects.get(app_label="mdm", model="bagtypemodel")
    auth_permission_73.codename = 'add_bagtypemodel'
    auth_permission_73 = importer.save_or_locate(auth_permission_73)

    auth_permission_74 = Permission()
    auth_permission_74.name = 'Can change Bagtype'
    auth_permission_74.content_type = ContentType.objects.get(app_label="mdm", model="bagtypemodel")
    auth_permission_74.codename = 'change_bagtypemodel'
    auth_permission_74 = importer.save_or_locate(auth_permission_74)

    auth_permission_75 = Permission()
    auth_permission_75.name = 'Can delete Bagtype'
    auth_permission_75.content_type = ContentType.objects.get(app_label="mdm", model="bagtypemodel")
    auth_permission_75.codename = 'delete_bagtypemodel'
    auth_permission_75 = importer.save_or_locate(auth_permission_75)

    auth_permission_76 = Permission()
    auth_permission_76.name = 'Can view Bagtype'
    auth_permission_76.content_type = ContentType.objects.get(app_label="mdm", model="bagtypemodel")
    auth_permission_76.codename = 'view_bagtypemodel'
    auth_permission_76 = importer.save_or_locate(auth_permission_76)

    auth_permission_77 = Permission()
    auth_permission_77.name = 'Can add Board'
    auth_permission_77.content_type = ContentType.objects.get(app_label="mdm", model="boardmodel")
    auth_permission_77.codename = 'add_boardmodel'
    auth_permission_77 = importer.save_or_locate(auth_permission_77)

    auth_permission_78 = Permission()
    auth_permission_78.name = 'Can change Board'
    auth_permission_78.content_type = ContentType.objects.get(app_label="mdm", model="boardmodel")
    auth_permission_78.codename = 'change_boardmodel'
    auth_permission_78 = importer.save_or_locate(auth_permission_78)

    auth_permission_79 = Permission()
    auth_permission_79.name = 'Can delete Board'
    auth_permission_79.content_type = ContentType.objects.get(app_label="mdm", model="boardmodel")
    auth_permission_79.codename = 'delete_boardmodel'
    auth_permission_79 = importer.save_or_locate(auth_permission_79)

    auth_permission_80 = Permission()
    auth_permission_80.name = 'Can view Board'
    auth_permission_80.content_type = ContentType.objects.get(app_label="mdm", model="boardmodel")
    auth_permission_80.codename = 'view_boardmodel'
    auth_permission_80 = importer.save_or_locate(auth_permission_80)

    auth_permission_81 = Permission()
    auth_permission_81.name = 'Can add Flight provider'
    auth_permission_81.content_type = ContentType.objects.get(app_label="mdm", model="flightprovidermodel")
    auth_permission_81.codename = 'add_flightprovidermodel'
    auth_permission_81 = importer.save_or_locate(auth_permission_81)

    auth_permission_82 = Permission()
    auth_permission_82.name = 'Can change Flight provider'
    auth_permission_82.content_type = ContentType.objects.get(app_label="mdm", model="flightprovidermodel")
    auth_permission_82.codename = 'change_flightprovidermodel'
    auth_permission_82 = importer.save_or_locate(auth_permission_82)

    auth_permission_83 = Permission()
    auth_permission_83.name = 'Can delete Flight provider'
    auth_permission_83.content_type = ContentType.objects.get(app_label="mdm", model="flightprovidermodel")
    auth_permission_83.codename = 'delete_flightprovidermodel'
    auth_permission_83 = importer.save_or_locate(auth_permission_83)

    auth_permission_84 = Permission()
    auth_permission_84.name = 'Can view Flight provider'
    auth_permission_84.content_type = ContentType.objects.get(app_label="mdm", model="flightprovidermodel")
    auth_permission_84.codename = 'view_flightprovidermodel'
    auth_permission_84 = importer.save_or_locate(auth_permission_84)

    auth_permission_85 = Permission()
    auth_permission_85.name = 'Can add Hotel'
    auth_permission_85.content_type = ContentType.objects.get(app_label="mdm", model="hotelmodel")
    auth_permission_85.codename = 'add_hotelmodel'
    auth_permission_85 = importer.save_or_locate(auth_permission_85)

    auth_permission_86 = Permission()
    auth_permission_86.name = 'Can change Hotel'
    auth_permission_86.content_type = ContentType.objects.get(app_label="mdm", model="hotelmodel")
    auth_permission_86.codename = 'change_hotelmodel'
    auth_permission_86 = importer.save_or_locate(auth_permission_86)

    auth_permission_87 = Permission()
    auth_permission_87.name = 'Can delete Hotel'
    auth_permission_87.content_type = ContentType.objects.get(app_label="mdm", model="hotelmodel")
    auth_permission_87.codename = 'delete_hotelmodel'
    auth_permission_87 = importer.save_or_locate(auth_permission_87)

    auth_permission_88 = Permission()
    auth_permission_88.name = 'Can view Hotel'
    auth_permission_88.content_type = ContentType.objects.get(app_label="mdm", model="hotelmodel")
    auth_permission_88.codename = 'view_hotelmodel'
    auth_permission_88 = importer.save_or_locate(auth_permission_88)

    auth_permission_89 = Permission()
    auth_permission_89.name = 'Can add Market'
    auth_permission_89.content_type = ContentType.objects.get(app_label="mdm", model="marketmodel")
    auth_permission_89.codename = 'add_marketmodel'
    auth_permission_89 = importer.save_or_locate(auth_permission_89)

    auth_permission_90 = Permission()
    auth_permission_90.name = 'Can change Market'
    auth_permission_90.content_type = ContentType.objects.get(app_label="mdm", model="marketmodel")
    auth_permission_90.codename = 'change_marketmodel'
    auth_permission_90 = importer.save_or_locate(auth_permission_90)

    auth_permission_91 = Permission()
    auth_permission_91.name = 'Can delete Market'
    auth_permission_91.content_type = ContentType.objects.get(app_label="mdm", model="marketmodel")
    auth_permission_91.codename = 'delete_marketmodel'
    auth_permission_91 = importer.save_or_locate(auth_permission_91)

    auth_permission_92 = Permission()
    auth_permission_92.name = 'Can view Market'
    auth_permission_92.content_type = ContentType.objects.get(app_label="mdm", model="marketmodel")
    auth_permission_92.codename = 'view_marketmodel'
    auth_permission_92 = importer.save_or_locate(auth_permission_92)

    auth_permission_93 = Permission()
    auth_permission_93.name = 'Can add Roomtype'
    auth_permission_93.content_type = ContentType.objects.get(app_label="mdm", model="roomtypemodel")
    auth_permission_93.codename = 'add_roomtypemodel'
    auth_permission_93 = importer.save_or_locate(auth_permission_93)

    auth_permission_94 = Permission()
    auth_permission_94.name = 'Can change Roomtype'
    auth_permission_94.content_type = ContentType.objects.get(app_label="mdm", model="roomtypemodel")
    auth_permission_94.codename = 'change_roomtypemodel'
    auth_permission_94 = importer.save_or_locate(auth_permission_94)

    auth_permission_95 = Permission()
    auth_permission_95.name = 'Can delete Roomtype'
    auth_permission_95.content_type = ContentType.objects.get(app_label="mdm", model="roomtypemodel")
    auth_permission_95.codename = 'delete_roomtypemodel'
    auth_permission_95 = importer.save_or_locate(auth_permission_95)

    auth_permission_96 = Permission()
    auth_permission_96.name = 'Can view Roomtype'
    auth_permission_96.content_type = ContentType.objects.get(app_label="mdm", model="roomtypemodel")
    auth_permission_96.codename = 'view_roomtypemodel'
    auth_permission_96 = importer.save_or_locate(auth_permission_96)

    auth_permission_97 = Permission()
    auth_permission_97.name = 'Can add Supplier'
    auth_permission_97.content_type = ContentType.objects.get(app_label="mdm", model="suppliermodel")
    auth_permission_97.codename = 'add_suppliermodel'
    auth_permission_97 = importer.save_or_locate(auth_permission_97)

    auth_permission_98 = Permission()
    auth_permission_98.name = 'Can change Supplier'
    auth_permission_98.content_type = ContentType.objects.get(app_label="mdm", model="suppliermodel")
    auth_permission_98.codename = 'change_suppliermodel'
    auth_permission_98 = importer.save_or_locate(auth_permission_98)

    auth_permission_99 = Permission()
    auth_permission_99.name = 'Can delete Supplier'
    auth_permission_99.content_type = ContentType.objects.get(app_label="mdm", model="suppliermodel")
    auth_permission_99.codename = 'delete_suppliermodel'
    auth_permission_99 = importer.save_or_locate(auth_permission_99)

    auth_permission_100 = Permission()
    auth_permission_100.name = 'Can view Supplier'
    auth_permission_100.content_type = ContentType.objects.get(app_label="mdm", model="suppliermodel")
    auth_permission_100.codename = 'view_suppliermodel'
    auth_permission_100 = importer.save_or_locate(auth_permission_100)

    auth_permission_101 = Permission()
    auth_permission_101.name = 'Can add session'
    auth_permission_101.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_101.codename = 'add_session'
    auth_permission_101 = importer.save_or_locate(auth_permission_101)

    auth_permission_102 = Permission()
    auth_permission_102.name = 'Can change session'
    auth_permission_102.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_102.codename = 'change_session'
    auth_permission_102 = importer.save_or_locate(auth_permission_102)

    auth_permission_103 = Permission()
    auth_permission_103.name = 'Can delete session'
    auth_permission_103.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_103.codename = 'delete_session'
    auth_permission_103 = importer.save_or_locate(auth_permission_103)

    auth_permission_104 = Permission()
    auth_permission_104.name = 'Can view session'
    auth_permission_104.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_104.codename = 'view_session'
    auth_permission_104 = importer.save_or_locate(auth_permission_104)

    auth_permission_105 = Permission()
    auth_permission_105.name = 'Can add site'
    auth_permission_105.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_105.codename = 'add_site'
    auth_permission_105 = importer.save_or_locate(auth_permission_105)

    auth_permission_106 = Permission()
    auth_permission_106.name = 'Can change site'
    auth_permission_106.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_106.codename = 'change_site'
    auth_permission_106 = importer.save_or_locate(auth_permission_106)

    auth_permission_107 = Permission()
    auth_permission_107.name = 'Can delete site'
    auth_permission_107.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_107.codename = 'delete_site'
    auth_permission_107 = importer.save_or_locate(auth_permission_107)

    auth_permission_108 = Permission()
    auth_permission_108.name = 'Can view site'
    auth_permission_108.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_108.codename = 'view_site'
    auth_permission_108 = importer.save_or_locate(auth_permission_108)

    # Processing model: django.contrib.auth.models.Group

    from django.contrib.auth.models import Group

    auth_group_1 = Group()
    auth_group_1.name = 'reviewer'
    auth_group_1 = importer.save_or_locate(auth_group_1)

    auth_group_1.permissions.add(auth_permission_57)
    auth_group_1.permissions.add(auth_permission_58)
    auth_group_1.permissions.add(auth_permission_59)
    auth_group_1.permissions.add(auth_permission_61)
    auth_group_1.permissions.add(auth_permission_62)
    auth_group_1.permissions.add(auth_permission_63)
    auth_group_1.permissions.add(auth_permission_65)
    auth_group_1.permissions.add(auth_permission_66)
    auth_group_1.permissions.add(auth_permission_67)

    auth_group_2 = Group()
    auth_group_2.name = 'contentmanager'
    auth_group_2 = importer.save_or_locate(auth_group_2)

    auth_group_3 = Group()
    auth_group_3.name = 'datarecorder'
    auth_group_3 = importer.save_or_locate(auth_group_3)

    auth_group_4 = Group()
    auth_group_4.name = 'analyst'
    auth_group_4 = importer.save_or_locate(auth_group_4)

    auth_group_5 = Group()
    auth_group_5.name = 'customer'
    auth_group_5 = importer.save_or_locate(auth_group_5)

    # Processing model: django.contrib.auth.models.User

    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.password = 'pbkdf2_sha256$100000$UtZ1m9fOdP8k$uqDoVibaQ0pJCyEqLeErwSGAqxQC5WpPYP86lSIKVKY='
    auth_user_1.last_login = None
    auth_user_1.is_superuser = False
    auth_user_1.username = 'test-customer'
    auth_user_1.first_name = 'Customer'
    auth_user_1.last_name = 'Test'
    auth_user_1.email = 'customer.test@top.cherubits.hu'
    auth_user_1.is_staff = False
    auth_user_1.is_active = True
    auth_user_1.date_joined = dateutil.parser.parse("2018-08-06T21:46:41+00:00")
    auth_user_1 = importer.save_or_locate(auth_user_1)

    auth_user_1.groups.add(auth_group_5)

    auth_user_2 = User()
    auth_user_2.password = 'pbkdf2_sha256$100000$ZXtMWc5G490O$Rnk20/amboWg7Jc9E9IORU+xkk0cDBtHEg12DUatyas='
    auth_user_2.last_login = None
    auth_user_2.is_superuser = False
    auth_user_2.username = 'test-administrator'
    auth_user_2.first_name = 'Administrator'
    auth_user_2.last_name = 'Test'
    auth_user_2.email = 'administrator.test@top.cherubits.hu'
    auth_user_2.is_staff = False
    auth_user_2.is_active = True
    auth_user_2.date_joined = dateutil.parser.parse("2018-08-06T21:48:06+00:00")
    auth_user_2 = importer.save_or_locate(auth_user_2)

    auth_user_2.groups.add(auth_group_1)
    auth_user_2.groups.add(auth_group_2)
    auth_user_2.groups.add(auth_group_3)

    auth_user_3 = User()
    auth_user_3.password = 'pbkdf2_sha256$100000$wTI1ngWQZ3rT$4FPsvmK6R8B5aMSKN5S1TC4sritYBT+6hdV7M2co6LA='
    auth_user_3.last_login = dateutil.parser.parse("2018-08-07T16:19:41.407710+00:00")
    auth_user_3.is_superuser = True
    auth_user_3.username = 'Kury33TOP'
    auth_user_3.first_name = 'Gergely'
    auth_user_3.last_name = 'Kurinyecz'
    auth_user_3.email = 'gergely.kurinyecz@theoutsourcepro.com'
    auth_user_3.is_staff = True
    auth_user_3.is_active = True
    auth_user_3.date_joined = dateutil.parser.parse("2018-08-06T21:41:05+00:00")
    auth_user_3 = importer.save_or_locate(auth_user_3)

    auth_user_4 = User()
    auth_user_4.password = 'pbkdf2_sha256$120000$j51jBQXOd5I7$0HvARJgeoUadwmqolcNUlpUe1fY64odyYPTcuiQv2g8='
    auth_user_4.last_login = dateutil.parser.parse("2018-08-28T17:31:53.948139+00:00")
    auth_user_4.is_superuser = True
    auth_user_4.username = 'lordoftheflies'
    auth_user_4.first_name = 'László'
    auth_user_4.last_name = 'Hegedűs'
    auth_user_4.email = 'laszlo.hegedus@cherubits.hu'
    auth_user_4.is_staff = True
    auth_user_4.is_active = True
    auth_user_4.date_joined = dateutil.parser.parse("2018-08-06T21:37:42+00:00")
    auth_user_4 = importer.save_or_locate(auth_user_4)

