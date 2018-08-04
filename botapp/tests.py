from botapp.models import SPIDER_CHOICES
from django.test import TestCase
from botapp import models as bot_models

#
# # Create your tests here.
# class ProjectTestCase(TestCase):
#     def setUp(self):
#         bot_models.ProjectModel.objects.create(
#             pk=1,
#             name="test-project",
#             scrapy=bot_models.ProjectModel.SCRAPY_PROJECT_NAME_PORTALCRAWLER,
#             version='9.9.9',
#             spider='angular')
#
#     def test_project_unique_name(self):
#         """Animals that can speak are correctly identified"""
#         test_project = bot_models.ProjectModel.objects.get(name="test-project")
#         self.assertEqual(str(test_project), 'test-project:9.9.9')
#
#
# class ProjectStepModel(TestCase):
#     def setUp(self):
#         project = bot_models.ProjectModel.objects.create(
#             pk=2,
#             name="test-project",
#             scrapy=bot_models.ProjectModel.SCRAPY_PROJECT_NAME_PORTALCRAWLER,
#             version='9.9.9',
#             spider='angular')
#
#         bot_models.ClickProjectStepModel.objects.create(
#             display_name="test-step#0",
#             order_index=1,
#             project=project,
#             html_query='body')
#         bot_models.ClickProjectStepModel.objects.create(
#             display_name="test-step#1",
#             order_index=2,
#             project=project,
#             html_query='body')
#         bot_models.ClickAndWaitProjectStepModel.objects.create(
#             display_name="test-step#2",
#             order_index=3,
#             project=project,
#             value='1.0',
#             html_query='body')
#         bot_models.ClickAndWaitProjectStepModel.objects.create(
#             display_name="test-step#3",
#             order_index=4,
#             project=project,
#             value='1.0',
#             html_query='body')
#         bot_models.OpenProjectStepModel.objects.create(
#             display_name="test-step#4",
#             order_index=5,
#             project=project,
#             value='https://www.google.com',
#             html_query='body')
#         bot_models.OpenProjectStepModel.objects.create(
#             display_name="test-step#5",
#             order_index=6,
#             project=project,
#             value='https://www.google.com',
#             html_query='body')
#         bot_models.WaitProjectStepModel.objects.create(
#             display_name="test-step#6",
#             order_index=7,
#             project=project,
#             value='1.0',
#             html_query='body')
#         bot_models.WaitProjectStepModel.objects.create(
#             display_name="test-step#7",
#             order_index=8,
#             project=project,
#             value='1.0',
#             html_query='body')
#         bot_models.WriteProjectStepModel.objects.create(
#             display_name="test-step#8",
#             order_index=9,
#             project=project,
#             value='text',
#             html_query='body')
#         bot_models.WriteProjectStepModel.objects.create(
#             display_name="test-step#9",
#             order_index=10,
#             project=project,
#             value='text',
#             html_query='body')
#         bot_models.StoreSelectedValueProjectStepModel.objects.create(
#             display_name="test-step#10",
#             order_index=11,
#             project=project,
#             value='variable#10',
#             html_query='body',
#             variable=True)
#         bot_models.StoreSelectedValueProjectStepModel.objects.create(
#             display_name="test-step#11",
#             order_index=12,
#             project=project,
#             value='variable#11',
#             html_query='body',
#             variable=True)
#
#     def test_get_steps_by_order(self):
#         actual_project_steps = bot_models.ProjectModel.objects.get(pk=2).get_steps_by_order
#
#         self.assertEqual(len(actual_project_steps), 12)
#         for index, step in enumerate(actual_project_steps):
#             self.assertEqual(step.order_index, index + 1)
#
#     def test_get_output_variable_names(self):
#         actual_output_variable_names = bot_models.ProjectModel.objects.get(pk=2).get_output_variable_names
#
#         self.assertListEqual(actual_output_variable_names, ['variable#10', 'variable#11'])

