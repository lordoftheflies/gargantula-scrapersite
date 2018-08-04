from django.db import models


# Create your models here.
#
# class EntityModel(models.Model):
#     display_name = models.CharField(max_length=200, default=None, null=True, blank=True)
#     description = models.CharField(max_length=2000, default=None, null=True, blank=True)
#
#     def __repr__(self):
#         return 'entity-%s' % self.pk
#
#     def __str__(self):
#         return self.display_name


# class EnumerationDimensionModel(EntityModel):
#     elements = models.ManyToManyField(EntityModel, related_name='containers')
#
# class FloatDimensionModel(EntityModel):


class MarketModel(models.Model):
    code = models.CharField(max_length=5, unique=True)
    display_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    description = models.CharField(max_length=2000, default=None, null=True, blank=True)

    class Meta:
        db_table = 'mdm_markets'

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code if self.display_name is None else self.display_name


class SupplierModel(models.Model):
    portal = models.URLField(max_length=2000)
    display_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    description = models.CharField(max_length=2000, default=None, null=True, blank=True)

    class Meta:
        db_table = 'mdm_suppliers'

    def __str__(self):
        return self.code if self.display_name is None else self.display_name


class AirportModel(models.Model):
    code = models.CharField(max_length=3, unique=True)
    display_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    description = models.CharField(max_length=2000, default=None, null=True, blank=True)

    class Meta:
        db_table = 'mdm_airports'

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code if self.display_name is None else self.display_name


class FlightProviderModel(models.Model):
    code = models.CharField(max_length=2, unique=True)
    display_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    description = models.CharField(max_length=2000, default=None, null=True, blank=True)

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code if self.display_name is None else self.display_name


class HotelModel(models.Model):
    stars = models.IntegerField()
    # market = models.ForeignKey(MarketModel, related_name='hotels')
    display_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    description = models.CharField(max_length=2000, default=None, null=True, blank=True)

    class Meta:
        db_table = 'mdm_hotels'

    def __str__(self):
        return 'hotel (%s)' % self.stars if self.display_name is None else self.display_name


class BoardModel(models.Model):
    code = models.CharField(max_length=2, unique=True)
    display_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    description = models.CharField(max_length=2000, default=None, null=True, blank=True)

    class Meta:
        db_table = 'mdm_boards'

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code if self.display_name is None else self.display_name


class RoomTypeModel(models.Model):
    code = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    description = models.CharField(max_length=2000, default=None, null=True, blank=True)

    class Meta:
        db_table = 'mdm_roomtypes'

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code if self.display_name is None else self.display_name


class BagTypeModel(models.Model):
    weight = models.IntegerField()
    display_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    description = models.CharField(max_length=2000, default=None, null=True, blank=True)

    def __str__(self):
        return '%skg' % self.weight
