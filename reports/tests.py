from datetime import datetime

from django.test import TestCase
from . import models
from mdm import models as mdm_models
from engine import models as engine_models
from hydra_datastore import models as datastore_models


# Create your tests here.
class ReportModelTest(TestCase):

    def setUp(self):
        mdm_models.AirportModel.objects.create(code='LTN', display_name='London, Luton', description='ksjkfsd')
        mdm_models.AirportModel.objects.create(code='LT1', display_name='London, Luton1', description='ksjkfsd1')
        mdm_models.AirportModel.objects.create(code='LT2', display_name='London, Luton2', description='ksjkfsd2')
        mdm_models.SupplierModel.objects.create(code='SPN', display_name='Supplier #1', description='ksjkfsd sfsdfsf',
                                                portal='https://www.google.com')

        schema = datastore_models.SchemaModel.objects.create(value=dict())
        dataset = datastore_models.DatasetModel.objects.create(timestamp=datetime.now(), schema=schema)
        datastore_models.EntryModel.objects.create(
            dataset=dataset,
            coordinates=dict(
                departure_airport='LTN',
                arrival_airport='ALT',
                duration=10,
                start=str(datetime.now()),
            ),
            data=dict(
                price=200,
                bag_price=1112222.23
            ),
        )
        datastore_models.EntryModel.objects.create(
            dataset=dataset,
            coordinates=dict(
                departure_airport='LTN',
                arrival_airport='CNN',
                duration=1,
                start=str(datetime.now()),
            ),
            data=dict(
                price=100,
                bag_price=2222.23
            ),
        )
        models.ReportModel.objects.create(slug='report-simple', title='Report #1')
        models.ReportModel.objects.create(slug='report-query', title='Report #2')
        models.ReportModel.objects.create(slug='report-dataset', title='Report #3')

    def test_report_get(self):
        """
        Test get report
        :return:
        """
        report = models.ReportModel.objects.get(slug="report-simple")
        self.assertEqual(report.title, 'Report #1')

    def test_make_simple_report(self):
        report = models.ReportModel.objects.get(slug="report-simple")  # type: models.ReportModel
        report.make(
            airports=mdm_models.AirportModel,
            suppliers=mdm_models.SupplierModel
        )

    def test_make_query_report(self):
        report = models.ReportModel.objects.get(slug="report-query")  # type: models.ReportModel
        report.builder().query(
            'joined', engine_models.ProcessModel.objects.filter(active=True).all()
        ).build()

    def test_make_query_report(self):
        report = models.ReportModel.objects.get(slug="report-dataset")  # type: models.ReportModel
        report.builder().query(
            sheet_name='entries',
            q=datastore_models.EntryModel.objects.all(),
            flattened_columns=['data', 'coordinates'],
            # fieldnames=('dataset', 'data', 'coordinates')
        ).build()
