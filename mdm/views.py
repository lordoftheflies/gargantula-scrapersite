from rest_framework import viewsets

from . import models as mdm_models
from . import serializers as mdm_serializers


class AirportViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing airport instances.
    """
    serializer_class = mdm_serializers.AirportSerializer
    queryset = mdm_models.AirportModel.objects.all()


class BagTypeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing bag-type instances.
    """
    serializer_class = mdm_serializers.BagTypeSerializer
    queryset = mdm_models.BagTypeModel.objects.all()


class BoardViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing board instances.
    """
    serializer_class = mdm_serializers.BoardSerializer
    queryset = mdm_models.BoardModel.objects.all()


class FlightProviderViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing flight-provider instances.
    """
    serializer_class = mdm_serializers.FlightProviderSerializer
    queryset = mdm_models.FlightProviderModel.objects.all()


class HotelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing hotel instances.
    """
    serializer_class = mdm_serializers.HotelSerializer
    queryset = mdm_models.HotelModel.objects.all()


class MarketViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing market instances.
    """
    serializer_class = mdm_serializers.MarketSerializer
    queryset = mdm_models.MarketModel.objects.all()


class RoomTypeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing room-type instances.
    """
    serializer_class = mdm_serializers.RoomTypeSerializer
    queryset = mdm_models.RoomTypeModel.objects.all()



class SupplierViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing supplier instances.
    """
    serializer_class = mdm_serializers.SupplierSerializer
    queryset = mdm_models.SupplierModel.objects.all()

