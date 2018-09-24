from django.db import models
from django_pandas.managers import DataFrameManager
from django.utils.translation import gettext as _


class AirportModel(models.Model):

    objects = DataFrameManager()

    code = models.CharField(max_length=3, unique=True)
    display_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    description = models.CharField(max_length=2000, default=None, null=True, blank=True)

    class Meta:
        db_table = 'mdm_airports'
        verbose_name = _('Airport')
        verbose_name_plural = _('Airports')

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code if self.display_name is None else self.display_name


class BagTypeModel(models.Model):
    objects = DataFrameManager()

    code = models.CharField(max_length=3, unique=True)
    weight = models.IntegerField()
    display_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    description = models.CharField(max_length=2000, default=None, null=True, blank=True)

    class Meta:
        db_table = 'mdm_bagtype'
        verbose_name = _('Bagtype')
        verbose_name_plural = _('Bagtypes')

    def __str__(self):
        return '%skg' % self.weight


class BoardModel(models.Model):

    objects = DataFrameManager()

    code = models.CharField(max_length=2, unique=True)
    display_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    description = models.CharField(max_length=2000, default=None, null=True, blank=True)

    class Meta:
        db_table = 'mdm_boards'
        verbose_name = _('Board')
        verbose_name_plural = _('Boards')

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code if self.display_name is None else self.display_name


class FlightProviderModel(models.Model):

    objects = DataFrameManager()

    code = models.CharField(max_length=3, unique=True)
    display_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    description = models.CharField(max_length=2000, default=None, null=True, blank=True)

    class Meta:
        db_table = 'mdm_flightprovider'
        verbose_name = _('Flight provider')
        verbose_name_plural = _('Flight providers')

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code if self.display_name is None else self.display_name


class HotelModel(models.Model):

    objects = DataFrameManager()

    code = models.CharField(max_length=3, unique=True)
    display_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    description = models.CharField(max_length=2000, default=None, null=True, blank=True)
    stars = models.IntegerField()

    class Meta:
        db_table = 'mdm_hotels'
        verbose_name = _('Hotel')
        verbose_name_plural = _('Hotels')

    def __str__(self):
        return 'hotel (%s)' % self.stars if self.display_name is None else self.display_name


class MarketModel(models.Model):

    objects = DataFrameManager()

    code = models.CharField(max_length=5, unique=True)
    display_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    description = models.CharField(max_length=2000, default=None, null=True, blank=True)

    class Meta:
        db_table = 'mdm_markets'
        verbose_name = _('Market')
        verbose_name_plural = _('Markets')

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code if self.display_name is None else self.display_name


class RoomTypeModel(models.Model):

    objects = DataFrameManager()

    code = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    description = models.CharField(max_length=2000, default=None, null=True, blank=True)

    class Meta:
        db_table = 'mdm_roomtypes'
        verbose_name = _('Roomtype')
        verbose_name_plural = _('Roomtypes')

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code if self.display_name is None else self.display_name


class SupplierModel(models.Model):

    objects = DataFrameManager()

    code = models.CharField(max_length=5, unique=True)
    display_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    description = models.CharField(max_length=2000, default=None, null=True, blank=True)
    portal = models.URLField(max_length=2000)

    class Meta:
        db_table = 'mdm_suppliers'
        verbose_name = _('Supplier')
        verbose_name_plural = _('Suppliers')

    def __str__(self):
        return self.code if self.display_name is None else self.display_name

class MdmManager():

    def resolve(self, slug, value):
        entity = None

        if slug == 'airport':
           entity = AirportModel.objects.get(id=value)
        elif slug == 'bagtype':
            entity = BagTypeModel.objects.get(id=value)
        elif slug == 'board':
            entity = BoardModel.objects.get(id=value)
        elif slug == 'flightprovider':
            entity = FlightProviderModel.objects.get(id=value)
        elif slug == 'hotel':
            entity = HotelModel.objects.get(id=value)
        elif slug == 'market':
            entity = MarketModel.objects.get(id=value)
        elif slug == 'roomtype':
            entity = RoomTypeModel.objects.get(id=value)
        elif slug == 'supplier':
            entity = SupplierModel.objects.get(id=value)

        result = dict(
            label=entity.display_name,
            code=entity.code,
            id=entity.id,
        )

        return result
