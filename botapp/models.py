import logging

import os

from copy import deepcopy
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from mdm import models as mdm_models
from datastore import models as data_models
from scrapyd_api import ScrapydAPI

logger = logging.getLogger(__name__)
scrapyd = ScrapydAPI('http://localhost:6800')

# Create your models here.

SPIDER_CHOICES = [
    ('angular', 'Angular'),
    ('screenshot', 'Screenshot'),
    ('json', 'Json'),
    ('xml', 'Xml')
]
OPERATION_ID_CLICK = 'click'
OPERATION_ID_OPEN = 'open'
OPERATION_ID_WAIT = 'wait'
OPERATION_ID_CLICK_AND_WAIT = 'clickAndWait'
OPERATION_ID_WRITE = 'write'
OPERATION_ID_STORE_SELECTED_VALUE = 'storeSelectedValue'
SCRAPY_PROJECT_NAME_APPCRAWLER = 'appcrawler'
SCRAPY_PROJECT_NAME_PORTALCRAWLER = 'portalcrawler'
SCRAPY_PROJECT_NAME_BOT = 'bot'
SCRAPY_PROJECT_NAME_NOMONO = 'nomono'
SCRAPY_PROJECT_CHOICES = [
    (SCRAPY_PROJECT_NAME_APPCRAWLER, _('SPA Crawler')),
    (SCRAPY_PROJECT_NAME_PORTALCRAWLER, _('Web Crawler')),
    (SCRAPY_PROJECT_NAME_NOMONO, _('Nomono Crawler')),
    (SCRAPY_PROJECT_NAME_BOT, _('Web bot'))
]
SCRAPY_JOB_STATE_VALUE_PENDING = 'pending'
SCRAPY_JOB_STATE_VALUE_RUNNING = 'running'
SCRAPY_JOB_STATE_VALUE_FINISHED = 'finished'
SCRAPY_JOB_STATES = [
    (SCRAPY_JOB_STATE_VALUE_PENDING, _('Pending')),
    (SCRAPY_JOB_STATE_VALUE_FINISHED, _('Finished')),
    (SCRAPY_JOB_STATE_VALUE_RUNNING, _('Running'))
]
PORTAL_PROPERTY_TYPE_TEXT = 'text'
PORTAL_PROPERTY_TYPE_NUMBER = 'number'
PORTAL_PROPERTY_TYPE_SELECT = 'select'
PORTAL_PROPERTY_TYPES = [
    (PORTAL_PROPERTY_TYPE_NUMBER, _('Number')),
    (PORTAL_PROPERTY_TYPE_SELECT, _('Select')),
    (PORTAL_PROPERTY_TYPE_TEXT, _('Text'))
]


class PortalModel(models.Model):
    name = models.CharField(max_length=250)
    version = models.CharField(max_length=10, default='3.13.54')
    lua_source = models.FileField(upload_to='source', blank=True, null=True, default=None)
    scrapy = models.CharField(max_length=250, choices=SCRAPY_PROJECT_CHOICES, default=SCRAPY_PROJECT_NAME_PORTALCRAWLER)
    spider = models.CharField(max_length=200, choices=SPIDER_CHOICES, default=SCRAPY_PROJECT_NAME_PORTALCRAWLER)
    supplier = models.ForeignKey(mdm_models.SupplierModel, default=None, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("portal")
        verbose_name_plural = _("portals")

        # @property
        # def lua_script(self):
        #     data = ""
        #     with open(os.path.join(settings.MEDIA_ROOT, self.lua_source.name), 'rt') as src:
        #         data = src.readlines()
        #     return ''.join((data[4:] + ['return result']))

    # @property
    # def parameter_map(self):
    #     parameters = ParameterModel.objects.filter(subject=self)
    #     map = {}
    #     for parameter in parameters:
    #         map[parameter.argument.name] = parameter.current_value
    #     return map

    @property
    def lua_script_for_execute(self):
        data = ""
        with open(os.path.join(settings.MEDIA_ROOT, self.lua_source.name), 'rt') as src:
            data = src.readlines()
        return ''.join(['function main(splash, args)\n'] +
                       # ['\n\t-- Auto generated parameters\n'] +
                       # ['\t%s' % line for line in self.generate_lua_parameters_parts()] +
                       ['\n\t-- Notebook defined scraper script from "%s"' % self.lua_source.name] +
                       ['\t%s' % line for line in data[4:]] +
                       ['\n\t-- End of notebook'] +
                       ['\n\treturn result', '\nend'])

    @property
    def get_jobs(self):
        return list(BestOfferJobModel.objects.filter(portal=self).order_by('-created'))

    # @property
    # def get_parameters(self):
    #     return ParameterModel.objects.filter(subject=self)

    def start_job(self, data, parent=None):
        # Persist input
        data.save()
        # Create job entity
        job = BestOfferJobModel.objects.create(portal=self, state=SCRAPY_JOB_STATE_VALUE_PENDING, data=data, parent=parent)
        # Start remote scrape on scrapy server
        job.scrapy_job = scrapyd.schedule(project=self.scrapy, spider=self.spider, job_id=job.pk)
        job.save()
        logging.info('Portal %s[%s] start new job[%s], scrapy job id=%s' % (self.name, self.pk, job.pk, job.scrapy_job))
        return job

    def __str__(self):
        return "%s:%s" % (self.name, self.version)


class ComparisonModel(models.Model):
    name = models.CharField(max_length=250)
    subject = models.ForeignKey(PortalModel, related_name='subject_portals', on_delete=models.CASCADE)
    competitors = models.ManyToManyField(PortalModel, related_name='compared_portals')

    @property
    def get_jobs(self):
        return list(BestOfferJobModel.objects.filter(comparison=self).filter(parent=None).order_by('-created'))

    def start_job(self, data):
        data.save()

        parent_job = BestOfferJobModel.objects.create(
            state=SCRAPY_JOB_STATE_VALUE_PENDING,
            data=data,
            comparison=self
        )

        supplier_job_input = deepcopy(data)
        supplier_job_input.pk = None
        supplier_job_input.save()
        supplier_job = self.subject.start_job(data=supplier_job_input, parent=parent_job)

        for organization in self.competitors.all():
            competitor_job_input = deepcopy(data)
            competitor_job_input.pk = None
            competitor_job_input.save()

            competitor_job = BestOfferJobModel.objects.create(
                parent=parent_job,
                portal=organization,
                state=SCRAPY_JOB_STATE_VALUE_PENDING,
                data=competitor_job_input
            )
            competitor_job.scrapy_job = scrapyd.schedule(
                project=self.subject.scrapy,
                spider=self.subject.spider,
                job_id=competitor_job.pk
            )
            competitor_job.save()
            logging.info('Portal %s[%s] start new job[%s], scrapy job id=%s' % (
                self.name,
                self.pk,
                competitor_job.pk,
                competitor_job.scrapy_job
            ))

        return supplier_job

    def __str__(self):
        return self.name


class BestOfferJobModel(models.Model):
    portal = models.ForeignKey(PortalModel, related_name='jobs', null=True, blank=True, default=None, on_delete=models.CASCADE)
    scrapy_job = models.CharField(max_length=50, null=True, blank=True, default=None)
    state = models.CharField(max_length=30, choices=SCRAPY_JOB_STATES, null=True, blank=True, default=None)
    created = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey("self", related_name='children', null=True, blank=True, default=None, on_delete=models.CASCADE)
    comparison = models.ForeignKey(ComparisonModel, null=True, blank=True, default=None, on_delete=models.CASCADE)
    data = models.ForeignKey(data_models.BestOfferModel, blank=True, null=True, default=None, on_delete=models.CASCADE)

    @property
    def lua_script_for_execute(self):
        data = ""
        with open(os.path.join(settings.MEDIA_ROOT, self.portal.lua_source.name), 'rt') as src:
            data = src.readlines()
        return ''.join(['function main(splash, args)\n'] +
                       ['\n\t-- Auto generated parameters\n'] +
                       ['\t%s' % line for line in self.generate_lua_parameters_parts()] +
                       ['\n\t-- Notebook defined scraper script from "%s"' % self.portal.lua_source.name] +
                       ['\t%s' % line for line in data[4:]] +
                       ['\n\t-- End of notebook'] +
                       ['\n\treturn result', '\nend'])

    @property
    def subject_portal(self):
        return self.comparison.subject

    @property
    def log_file_url(self):
        return '%s/%s.log' % (settings.SCRAPY_DAEMON_HOST, self.scrapy_job)

    @property
    def get_children(self):
        return BestOfferJobModel.objects.filter(parent=self)

    @property
    def lua_script_for_run(self):
        data = ""
        with open(os.path.join(settings.MEDIA_ROOT, self.portal.lua_source.name), 'rt') as src:
            data = src.readlines()
        return ''.join(self.generate_lua_parameters_parts() + data[4:] + ['\nreturn result'])

    @property
    def lua_script_for_run_with_rownumbers(self):
        data = ""
        with open(os.path.join(settings.MEDIA_ROOT, self.portal.lua_source.name), 'rt') as src:
            data = src.readlines()
        lines = self.generate_lua_parameters_parts() + data[4:] + ['\nreturn result']
        numbered_lines = []
        index = 0
        for l in lines:
            numbered_lines.append('%s: %s' % (index, l))
            index = index + 1
        return ''.join(numbered_lines)

    def generate_lua_parameters_parts(self):
        parameter_list = ['parameters = {}\n']
        for key, value in self.data.input_parameters().items():
            parameter_list.append('parameters.%s = "%s"\n' % (key, value))
        return parameter_list

#
#
# class LuaScriptBuilder(object):
#     def _wait_command(self, time_for_wait):
#         return "assert(splash:wait(%s))" % time_for_wait
#
#     def _private_mode_command(self):
#         return "splash.private_mode_enabled = false"
#
#     def _init_cookies_command(self):
#         return "splash:init_cookies(splash.args.cookies)"
#
#     def _go_command(self, url='args.url'):
#         return "assert(splash:go(%s))" % url
#
#     def _click_command(self, selector):
#         return 'splash:select(\"%s\"):mouse_click()' % selector
#
#     def _write_command(self, selector, value):
#         return 'splash:select(\"%s\"):value = ' % (selector, value)
#
#     def _get_cookies_command(self):
#         return "cookies=splash:get_cookies()"
#
#     def _success_command(self):
#         return "ok=true"
#
#     def _png_command(self, variable='image'):
#         return "%s=splash:png()" % variable
#
#     def _html_command(self, variable='html'):
#         return "%s=splash:html()" % variable
#
#     def _final_url_command(self, variable='final_url'):
#         return "%s=splash:url()" % variable
#
#     def _store_command(self, selector, variable):
#         return '%s=splash:select("%s"):text()' % (variable, selector)
#
#     def __init__(self):
#         self.logger = logging.getLogger(__name__)
#         self.lines = []
#         self.output = []
#         self.current_indentation = 0
#
#     def _script_line(self, command_line, indentation=0, conjunction=False):
#         prefix = ''
#         for x in range(0, indentation):
#             prefix += '\t'
#         suffix = ',' if conjunction else ''
#         return prefix + command_line + suffix
#
#     def initialize(self):
#         self.lines.append(
#             self._script_line(command_line=self._private_mode_command(), indentation=self.current_indentation))
#         # self.lines.append(self._script_line(command_line=self._init_cookies_command(), indentation=self.current_indentation))
#         self.lines.append(self._script_line(command_line=self._go_command(), indentation=self.current_indentation))
#         return self
#
#     def click(self, selector):
#         self.lines.append(self._script_line(command_line=self._click_command(selector=selector),
#                                             indentation=self.current_indentation))
#         return self
#
#     def go(self, selector):
#         self.lines.append(self._script_line(command_line=self._go_command(), indentation=self.current_indentation))
#         return self
#
#     def write(self, selector, value):
#         self.lines.append(self._script_line(command_line=self._write_command(
#             selector=selector,
#             value=value
#         ), indentation=self.current_indentation))
#         return self
#
#     def wait(self, time_for_wait):
#         self.lines.append(self._script_line(command_line=self._wait_command(time_for_wait=time_for_wait),
#                                             indentation=self.current_indentation))
#         return self
#
#     def get_cookies(self):
#         self.output.append(
#             self._script_line(command_line=self._get_cookies_command(), indentation=self.current_indentation))
#         return self
#
#     def png(self):
#         self.output.append(self._script_line(command_line=self._png_command(), indentation=self.current_indentation))
#         return self
#
#     def html(self):
#         self.output.append(self._script_line(command_line=self._html_command(), indentation=self.current_indentation))
#         return self
#
#     def store(self, selector, variable):
#         self.output.append(self._script_line(command_line=self._store_command(selector=selector, variable=variable), indentation=self.current_indentation))
#         return self
#
#     def __enter__(self):
#         self.lines.append(self._script_line(command_line="return {", indentation=self.current_indentation))
#         # self.current_indentation += 1
#         self.conjunction = True
#         self.get_cookies()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#
#         for line in self.output:
#             self.lines.append(self._script_line(command_line=line, indentation=self.current_indentation + 1, conjunction=True))
#
#         self.lines.append(self._script_line(command_line=self._success_command(), indentation=self.current_indentation + 1))
#
#         self.lines.append(self._script_line(command_line="}", indentation=self.current_indentation))
#         return self
#
#     def build(self):
#         return ' \n'.join(self.lines)
