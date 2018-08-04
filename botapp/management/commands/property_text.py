from django.core.management.base import BaseCommand, CommandError
# from mdm import models as mdm_models
# from botapp import models as bot_models
import mdm
import botapp
import reportsapp
import report_builder


class Command(BaseCommand):
    help = 'Generate text property'

    def add_arguments(self, parser):
        parser.add_argument('display_name', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('property_name', type=str)
        parser.add_argument('property_value', type=str)

    def handle(self, *args, **options):
        display_name = options['display_name']
        description = options['description']
        property_name = options['property_name']
        property_value = options['property_value']

        property = botapp.models.TextPropertyModel.objects.create(
            name=property_name,
            display_name=display_name,
            default_value=property_value
        )

        self.stdout.write(self.style.SUCCESS('Successfully created text property %s[pk=%s]' % (property.display_name, property.pk)))
