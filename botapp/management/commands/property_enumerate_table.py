from django.core.management.base import BaseCommand, CommandError
# from mdm import models as mdm_models
# from botapp import models as bot_models
import mdm
import botapp
import reportsapp
import report_builder


class Command(BaseCommand):
    help = 'Generate enumeration property for portal.'

    def add_arguments(self, parser):
        parser.add_argument('display_name', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('modelclass', type=str)
        parser.add_argument('property_name', type=str)

    def handle(self, *args, **options):
        display_name = options['display_name']
        description = options['description']
        modelclass = options['modelclass']
        property_name = options['property_name']

        group = botapp.models.EnumerationGroupModel.objects.create(
            display_name=display_name,
            description=description
        )
        self.stdout.write('Create enumeration group: %s' % group.display_name)

        cls = eval(modelclass)

        for entity in cls.objects.all():
            item = botapp.models.EnumerationValueModel.objects.create(owner=group, entity=entity)
            self.stdout.write('- Add item to enumeration: %s' % item.display_name)

        property = botapp.models.EnumerationPropertyModel.objects.create(
            name=property_name,
            display_name=display_name,
            group=group
        )

        self.stdout.write(self.style.SUCCESS('Successfully created enumeration property %s[pk=%s]' % (property.display_name, property.pk)))
