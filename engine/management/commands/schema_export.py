import json
import traceback

from django.core.management import BaseCommand

from ... import models as engine_models
from ... import serializers as engine_serializers


class Command(BaseCommand):
    help = 'Export schema model.'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        try:
            path = options['path']

            with open(path, mode='wt') as f:
                processes = engine_serializers.ProcessSerializer(engine_models.ProcessModel.objects.all(), many=True).data
                schema = dict(
                    processes=processes
                )

                json.dump(schema, f, indent=4, sort_keys=True)

            self.stdout.write(self.style.SUCCESS('Successfully exported process model schema from %s' % path))
        except BaseException as e:
            traceback.print_exc()