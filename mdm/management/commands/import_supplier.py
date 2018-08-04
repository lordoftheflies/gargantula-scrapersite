import csv

from mdm import models as mdm_models
from mdm.management.commands.baseimport import ImportCommand


class Command(ImportCommand):
    help = 'Import supplier data from csv.'
    modelclass = mdm_models.SupplierModel

    def import_element(self, row):
        return mdm_models.SupplierModel.objects.get_or_create(
            portal=row[1],
            display_name=row[2],
            description=row[3],
        )
