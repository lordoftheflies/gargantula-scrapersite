import csv

from mdm import models as mdm_models
from mdm.management.commands.baseimport import ImportCommand


class Command(ImportCommand):
    help = 'Import hotel data from csv.'
    modelclass = mdm_models.HotelModel

    def import_element(self, row):
        return mdm_models.HotelModel.objects.get_or_create(
            stars=row[1],
            display_name=row[2],
            description=row[3],
        )
