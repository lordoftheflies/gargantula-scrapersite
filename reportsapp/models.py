from django.contrib.postgres.fields import ArrayField
from django.db import models
from report_builder.models import Report

# Create your models here.


class ReportModel(models.Model):
    definition = models.ForeignKey(Report, related_name='instances', on_delete=models.CASCADE)

class EntryModel(models.Model):
    report = models.ForeignKey(to=ReportModel, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    

class GridModel(models.Model):
    column_index = models.IntegerField(default=0, null=False, blank=False)
    row_index = models.IntegerField(default=0, null=False, blank=False)
    owner = models.ForeignKey(to=ReportModel, on_delete=models.CASCADE)

class FormModel(GridModel):
    title = models.CharField(max_length=100, default=None, blank=True, null=True)

class FieldModel(GridModel):
    container = models.ForeignKey(to=FormModel, on_delete=models.CASCADE, related_name='fields')
    label = models.CharField(max_length=100, blank=False, null=False)
    index = models.IntegerField(default=0, null=False, blank=False)
    value = models.CharField(max_length=1000, default=None, blank=True, null=True)

class TableModel(GridModel):
    title = models.CharField(max_length=100, default=None, blank=True, null=True)

class RowModel(GridModel):
    container = models.ForeignKey(to=TableModel, on_delete=models.CASCADE, related_name='rows')
    data_array = ArrayField(models.CharField(max_length=100))

class ColumnModel(GridModel):
    label = models.CharField(max_length=100, blank=False, null=False)
    container = models.ForeignKey(to=TableModel, on_delete=models.CASCADE, related_name='columns')
