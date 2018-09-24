import logging

import os

from django.conf import settings
from django.db import models
import pandas as pd
from django.utils.translation import gettext as _
from django_pandas.io import read_frame
from django_pandas.managers import DataFrameManager

logger = logging.getLogger(__name__)


class ReportBuilder():

    def __init__(self, path, filename=None, extension='xlsx', engine='xlsxwriter'):
        self.path = path
        self.filename = filename
        self.extension = extension
        self.engine = engine
        self.frames = []
        self.sheets = []

    def set_filename(self, filename) -> 'ReportBuilder':
        self.filename = filename
        return self

    def set_extension(self, extension) -> 'ReportBuilder':
        self.extension = extension
        return self

    def dataframe(self, sheet_name, dataframe: pd.DataFrame, flattened_columns=[]) -> 'ReportBuilder':
        """
        Add dataframe to a report as a separated sheet
        :param sheet_name: Name of the created sheet
        :param dataframe: Source dataframe
        :param flattened_columns: JSON column names, which need to be flattened
        :return:
        """
        concatenated_frames = []
        for column in flattened_columns:
            frame = pd.DataFrame(dataframe[column].values.tolist())
            frame.columns = column + '.' + frame.columns
            concatenated_frames.append(frame)
            logger.info('flatten column "%s"' % column)

        already_flattened_df = dataframe.columns.difference(flattened_columns)
        normalized_df = pd.concat([dataframe[already_flattened_df]] + concatenated_frames, axis=1)

        self.frames.append(normalized_df)
        self.sheets.append(sheet_name)
        return self

    def query(self, sheet_name, q, fieldnames=(), flattened_columns=[]) -> 'ReportBuilder':
        """
        Add querset to a report as a separated sheet
        :param sheet_name: 
        :param q: Query which model has a DataframeManager
        :param fieldnames: Names of mapped columns
        :param flattened_columns: 
        :return: 
        """
        df = q.to_dataframe(fieldnames=fieldnames)
        return self.dataframe(sheet_name, df, flattened_columns)

    def flatten(self, js):
        return pd.DataFrame(js).set_index('pos').squeeze()

    @property
    def full_filepath(self) -> str:
        return os.path.join(self.path, '%s.%s' % (self.filename, self.extension))

    def build(self) -> str:
        writer = pd.ExcelWriter(self.full_filepath, engine=self.engine, options=dict(remove_timezone=True))
        for i in range(0, len(self.frames)):
            self.frames[i].to_excel(writer, sheet_name=self.sheets[i])
        writer.save()
        return self.full_filepath


# Create your models here.
class ReportModel(models.Model):
    EXCEL_EXTENSION = 'xlsx'
    EXCEL_WRITER = 'xlsxwriter'

    slug = models.CharField(max_length=100, blank=True, null=True, default=None)
    title = models.CharField(max_length=100, blank=True, null=True, default=None)

    # title = models.CharField(max_length=100, blank=True, null=True, default=None)

    def generate_filename(self) -> str:
        return self.slug

    def builder(self) -> ReportBuilder:
        return ReportBuilder(
            path=settings.MEDIA_ROOT,
            filename=self.generate_filename(),
            extension=self.EXCEL_EXTENSION,
            engine=self.EXCEL_WRITER
        )

    def make(self, **kwargs) -> str:
        builder = self.builder()
        for key, model_cls in kwargs.items():
            qs = model_cls.objects.all()
            builder.query(key, qs)
        return builder.build()


class BlockModel(models.Model):
    label = models.CharField(max_length=100, blank=True, null=True, default=None)

    class Meta:
        abstract = True


#
# class OneDimensionBlockModel(BlockModel):
#     entry = models.ForeignKey(to=datastore_models.EntryModel, on_delete=models.CASCADE)
#
#
# class TwoDimensionalBlockModel(BlockModel):
#     dataset = models.ForeignKey(to=datastore_models.DatasetModel, on_delete=models.CASCADE)


class BestOfferModel(models.Model):
    departure_city = models.CharField(max_length=25)
    departure_airport = models.CharField(max_length=25)
    departure_timestamp = models.DateTimeField()
    arrival_airport = models.CharField(max_length=25)
    arrival_date = models.DateTimeField()
    region = models.CharField(max_length=25)
    hotel = models.CharField(max_length=25)
    stars = models.CharField(max_length=25)
    room_type = models.CharField(max_length=25)
    board_basis = models.CharField(max_length=25)
    number_of_passangers = models.IntegerField(default=2)
    duration = models.IntegerField(default=1)

    objects = DataFrameManager()
