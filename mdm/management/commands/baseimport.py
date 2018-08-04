import csv

from django.core.management import BaseCommand


class ImportCommand(BaseCommand):
    help = 'Import data from csv.'
    modelclass = None

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        path = options['path']

        imported_element_count = 0
        header_parsed = False
        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
                if (header_parsed is True):
                    if len(row) > 0:
                        self.stdout.write(str(row))
                        _, created = self.import_element(row)

                        imported_element_count = imported_element_count + 1
                else:
                    header_parsed = True
        self.stdout.write(self.style.SUCCESS('Successfully imported %s %s model from %s' % (imported_element_count, self.modelclass, path)))

    def import_element(self, row):
        raise NotImplementedError('Implement import')
