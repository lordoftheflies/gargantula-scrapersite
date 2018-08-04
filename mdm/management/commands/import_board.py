import csv

from mdm import models as mdm_models
from mdm.management.commands.baseimport import ImportCommand


class Command(ImportCommand):
    help = 'Import board data from csv.'
    modelclass = mdm_models.BoardModel

    def import_element(self, row):
        return mdm_models.BoardModel.objects.get_or_create(
            code=row[1],
            display_name=row[2],
            description=row[3],
        )
