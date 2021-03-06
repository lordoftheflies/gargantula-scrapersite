import csv

from ... import models as mdm_models
from .baseimport import ImportCommand


class Command(ImportCommand):
    help = 'Import airport data from csv.'
    modelclass = mdm_models.AirportModel

    def import_element(self, row):
        return mdm_models.AirportModel.objects.get_or_create(
            code=row[1],
            display_name=row[2],
            description=row[3],
        )
