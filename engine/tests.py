from datetime import datetime

import pytest
from django.test import TestCase
from configurations.management import call_command
from engine import tasks
from engine import models


class CommandsTestCase(TestCase):
    def test_schema_export(self):
        " Test schema_export command."

        args = ['../modeling/schema.json']
        opts = {}
        call_command('schema_export', *args, **opts)

    def test_schema_import(self):
        " Test schema_import command."

        args = ['../modeling/schema.json']
        opts = {}
        call_command('schema_import', *args, **opts)


#
# # Create your tests here.
# class ScrapyTestCase(TestCase):
#
#     def test_crawl(self):
#         from scrapy.cmdline import execute
#         execute(argv=['ata', 'atb'])
#
#
# class ProcessTests(APITestCase):
#     def test_create_process(self):
#         """
#         Ensure we can create a new account object.
#         """
#         url = reverse('process-list')
#         data = dict(
#             slug='test_process',
#             friendly_name='Test process',
#             description='Description of test process',
#             active=False,
#         )
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(models.ProcessModel.objects.count(), 1)
#         self.assertEqual(models.ProcessModel.objects.get().slug, 'test_process')
#
#
# @pytest.mark.celery(result_backend='redis://')
# class JonTestCase(TestCase):
#
#     def test_job(self):
#         process = models.ProcessModel.objects.create(
#             slug='test_process',
#             friendly_name='Test process',
#             description='Description of test process',
#             active=False,
#         )  # type: models.ProcessModel
#         execution = models.ExecutionModel.objects.create(
#             process=process
#         )  # type: models.ExecutionModel
#
#         tasks.job(
#             process_id=process.id,
#             execution_id=execution.id
#         )
#
#
@pytest.mark.celery(result_backend='redis://')
class TasksTestCase(TestCase):


    def setUp(self):
        self.process = models.ProcessModel.objects.create(
            slug='bot',
            friendly_name='test-display-name',
            description='description of test-display-name',
            notebook='bot.ipynb'
        )
        self.execution = models.ExecutionModel.objects.create(
            started=datetime.now(),
            ended=datetime.now(),
            process=self.process,
            configuration='{}',
            status=models.ExecutionModel.STATUS_COMPLETED
        )

    def test_splash_notebook(self):
        """ Test notebook script get """
        response = tasks.splash_notebook(
            notebook='bot',
            execution_id=1
        )
        print('response')
        # self.assertEqual(execution_result['process_id'], process.id)

    def test_scrapy_observer(self):
        """ Test observe scrapy job """
        response = tasks.scrapy_observer(
            scrapy_job_id='bot',
            process_id=self.process.id,
            execution_id=self.execution.id,
        )
        self.assertEqual(response, None)
