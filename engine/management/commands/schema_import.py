import json

from django.core.management import BaseCommand

from ... import models as engine_models


class Command(BaseCommand):
    help = 'Import schema model.'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        path = options['path']

        with open(path) as f:
            schema = json.load(f)
            for process_json in schema['processes']:
                process_model = self.create_process(**process_json)
                for argument_json in process_json['arguments']:
                    self.create_argument(process=process_model, **argument_json)
                for property_json in process_json['schema']:
                    self.create_argument(process=process_model, **property_json)

        self.stdout.write(self.style.SUCCESS('Successfully imported process model schema from %s' % path))

    def create_process(self, **kwargs) -> engine_models.ProcessModel:
        process = engine_models.ProcessModel.objects.create(
            friendly_name=kwargs['friendly_name'],
            description=kwargs['description'],
            active=kwargs['active'],
            notebook=kwargs['notebook'],
            slug=kwargs['slug'],
        )
        return process

    def create_argument(self, process: engine_models.ProcessModel, **kwargs) -> engine_models.ArgumentModel:
        argument = engine_models.ArgumentModel.objects.create(
            friendly_name=kwargs['friendly_name'],
            description=kwargs['description'],
            data_type=kwargs['data_type'],
            default_value=kwargs['default_value'],
            tag=kwargs['tag'],
            process=process,
            slug=kwargs['slug'],
        )
        return argument

    def create_property(self, process: engine_models.ProcessModel, **kwargs) -> engine_models.PropertyModel:
        argument = engine_models.PropertyModel.objects.create(
            friendly_name=kwargs['friendly_name'],
            description=kwargs['description'],
            data_type=kwargs['data_type'],
            default_value=kwargs['default_value'],
            tag=kwargs['tag'],
            process=process,
            slug=kwargs['slug'],
        )
        return argument
