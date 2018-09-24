import json
import logging

import os
import traceback

from datetime import datetime
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from hydra_notebook.core import NotebookBuilder, NotebookFileHandler
from django_pandas.managers import DataFrameManager

from mdm.models import MdmManager

logger = logging.getLogger(__name__)


# Create your models here.


class NamedMixin(models.Model):
    slug = models.CharField(max_length=100)

    class Meta:
        abstract = True


class ContentMixin(NamedMixin):
    friendly_name = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)

    class Meta:
        abstract = True

    def __str__(self):
        return self.friendly_name


class ProcessModel(ContentMixin):
    objects = DataFrameManager()

    active = models.BooleanField(default=True)
    notebook = models.FilePathField(path=settings.NOTEBOOKS_ROOT, allow_files=True, allow_folders=False, max_length=500)

    class Meta:
        verbose_name = _('Process')
        verbose_name_plural = _('Processes')

    def __str__(self):
        return '%s (%s)' % (str(self.friendly_name), self.id)

    @property
    def parameters_query(self):
        return ArgumentModel.objects.filter(process=self)

    @property
    def parameters(self):
        arguments = self.parameters_query.all()
        return {argument.slug: argument.default_value for argument in arguments}

    @property
    def properties(self):
        properties = PropertyModel.objects.filter(process=self).all()
        return {argument.slug: argument.default_value for argument in properties}

    def start(self):
        execution = ExecutionModel.objects.create(
            process=self,
            configuration=json.dumps(self.parameters)
        )

        return execution

    @property
    def notebook_filename(self):
        return os.path.splitext(self.notebook)[0].split('/')[-1]

    @property
    def notebook_basename(self):
        return os.path.basename(self.notebook)

    @property
    def executions(self):
        return ExecutionModel.objects.filter(process=self)

    def generate_notebook(self):
        b = NotebookBuilder()
        nb = b.notebook().build()
        return nb

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save(force_insert=force_insert, force_update=force_update, using=None, update_fields=update_fields)

        if self.notebook is None:
            self.notebook = 'notebook%s' % self.id
            logger.info('Generate notebook: %s' % self.notebook)
            notebook = self.generate_notebook()
        else:
            logger.info('Update notebook: %s' % self.notebook)
            notebook = self.refresh_notebook()

        self.update_notebook(notebook)

    def refresh_notebook(self):
        fh = NotebookFileHandler(fullname=self.notebook_filename)
        fh.read()
        return fh.notebook

    def update_notebook(self, nb):
        if 'gargantula' not in nb['metadata']:
            b = NotebookBuilder(notebook=nb)
            b.meta_property('gargantula', False)
            b.markdown(
                "# %s" % self.friendly_name,
                self.description
            )
            b.code('print("pre")')
            b.code('print("post")')
            b.cells = b.cells[0:1] + nb['cells'] + [b.cells[1]]
            nb = b.build()

            fh = NotebookFileHandler(fullname=self.notebook_filename)
            fh.notebook = nb
            fh.write()
        elif not nb['metadata']['gargantula']:
            b = NotebookBuilder(notebook=nb)
            b.meta_property('gargantula', False)
            b.code('print("pre")')
            b.code('print("post")')
            b.cells = [nb['cells'][0], b.cells[0]] + nb['cells'][2:-2] + [b.cells[-1]]
            nb = b.build()

            fh = NotebookFileHandler(fullname=self.notebook_filename)
            fh.notebook = nb
            fh.write()
        else:
            logger.warning('notebook setup skipped, metadata = %s' % nb['metadata'])


class ParameterModel(ContentMixin):
    TYPE_TEXT = 'text'
    TYPE_NUMBER = 'number'
    TYPE_DATE = 'date'
    TYPE_BOOLEAN = 'boolean'
    TYPE_ENUMERATION_AIRPORT = 'enumeration_airport'
    TYPE_ENUMERATION_BAGTYPE = 'enumeration_bagtype'
    TYPE_ENUMERATION_BOARD = 'enumeration_board'
    TYPE_ENUMERATION_FLIGHTPROVIDER = 'enumeration_flightprovider'
    TYPE_ENUMERATION_HOTEL = 'enumeration_hotel'
    TYPE_ENUMERATION_MARKET = 'enumeration_market'
    TYPE_ENUMERATION_ROOMTYPE = 'enumeration_roomtype'
    TYPE_ENUMERATION_SUPPLIER = 'enumeration_supplier'

    TYPES = [
        (TYPE_TEXT, _('Text')),
        (TYPE_NUMBER, _('Number')),
        (TYPE_DATE, _('Date')),
        (TYPE_BOOLEAN, _('Boolean')),
        (TYPE_ENUMERATION_AIRPORT, _('Airports')),
        (TYPE_ENUMERATION_BAGTYPE, _('Bag type')),
        (TYPE_ENUMERATION_BOARD, _('Board')),
        (TYPE_ENUMERATION_FLIGHTPROVIDER, _('Flight provider')),
        (TYPE_ENUMERATION_HOTEL, _('Hotel')),
        (TYPE_ENUMERATION_MARKET, _('Market')),
        (TYPE_ENUMERATION_ROOMTYPE, _('Room type')),
        (TYPE_ENUMERATION_SUPPLIER, _('Supplier')),
    ]

    data_type = models.CharField(max_length=30, choices=TYPES, default=TYPE_TEXT)
    default_value = models.CharField(max_length=1000, default=None, blank=True, null=True)
    tag = models.CharField(max_length=50, default=None, blank=True, null=True)

    class Meta:
        abstract = True


class ArgumentModel(ParameterModel):
    objects = DataFrameManager()

    process = models.ForeignKey(
        to=ProcessModel,
        related_name='arguments',
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('Argument')
        verbose_name_plural = _('Arguments')


class PropertyModel(ParameterModel):
    objects = DataFrameManager()
    process = models.ForeignKey(
        to=ProcessModel,
        related_name='schema',
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('Property')
        verbose_name_plural = _('Properties')


class ExecutionModel(models.Model):
    objects = DataFrameManager()
    STATUS_INITIAL = 'initial'
    STATUS_PENDING = 'pending'
    STATUS_RUNNING = 'running'
    STATUS_COMPLETED = 'completed'
    STATUS_FAILED = 'failed'
    STATUS_PAUSED = 'paused'
    STATUSES = [
        (STATUS_INITIAL, _('Initial')),
        (STATUS_COMPLETED, _('Completed')),
        (STATUS_FAILED, _('Failed')),
        (STATUS_PAUSED, _('Paused')),
        (STATUS_PENDING, _('Pending')),
        (STATUS_RUNNING, _('Running')),
    ]

    started = models.DateTimeField(null=True, blank=False, default=timezone.now)
    ended = models.DateTimeField(null=True, blank=True, default=None)
    process = models.ForeignKey(
        to=ProcessModel,
        related_name='executions',
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True
    )
    configuration = models.TextField(max_length=1000, default='{}', blank=False, null=False)
    status = models.CharField(max_length=50, choices=STATUSES, default=STATUS_INITIAL, blank=False, null=False)

    @property
    def arguments(self):
        if self.configuration is not None:
            return json.loads(self.configuration)
        else:
            return dict()

    @arguments.setter
    def arguments(self, value):
        self.configuration = json.dumps(value)

    @property
    def friendly_name(self):
        return self.process.friendly_name

    @property
    def parameters(self):
        return self.process.parameters_query.all()

    def __str__(self):
        return '%s[%s - %s]' % (
            self.friendly_name,
            datetime.strftime(self.started, '%Y-%m-%d %H:%M:%S'),
            datetime.strftime(self.ended, '%Y-%m-%d %H:%M:%S'),
        )

    @property
    def dashboard(self):
        values = self.arguments
        arguments = self.process.parameters_query.all()
        manager = MdmManager()

        result = []
        for argument in arguments:
            try:
                if argument.tag is None:
                    value = values.get(argument.slug, argument.default_value)
                else:
                    data = manager.resolve(
                        slug=argument.tag,
                        value=values.get(argument.slug, argument.default_value)
                    )
                    value = '%s (%s)' % (data['label'], data['code'])
                item = dict(
                    slug=argument.slug,
                    label=argument.friendly_name,
                    description=argument.description,
                    value=value,
                )

            except BaseException as e:
                traceback.print_exc()
                item = dict(
                    slug=argument.slug,
                    label=argument.friendly_name,
                    description=argument.description,
                    value='Unkown value'
                )
            finally:
                result.append(item)
        return result

    def start(self):
        self.status = self.STATUS_RUNNING
        self.started = timezone.now()
        self.save()

    def complete(self):
        self.status = self.STATUS_COMPLETED
        self.ended = self.ended = timezone.now()
        self.save()

    def fail(self):
        self.status = self.STATUS_FAILED
        self.ended = self.ended = timezone.now()
        self.save()

    def pause(self):
        self.status = self.STATUS_PAUSED
        self.save()

    def resume(self):
        self.status = self.STATUS_PENDING
        self.save()

    def configure(self, **kwargs):
        context = dict()
        for key, value in self.arguments.items():
            context[key] = value
        for key, value in kwargs.items():
            context[key] = value
        self.arguments = context
        logger.info('%s:%s configured: %s' % (
            self.process.friendly_name,
            self.id,
            json.dumps(context,  sort_keys=True, indent=4)
        ))
        self.save()


class EventModel(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    message = models.CharField(max_length=1000)
    cause = models.CharField(max_length=1000, null=True, blank=True, default=None)
