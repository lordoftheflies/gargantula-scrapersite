from django.contrib.auth import models as auth_model
from rest_framework import serializers as rest_serializers
from . import models


class AirportSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.AirportModel
        fields = ['id', 'code', 'display_name', 'description']


class BagTypeSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.BagTypeModel
        fields = ['id', 'code', 'display_name', 'description', 'weight']


class BoardSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.BagTypeModel
        fields = ['id', 'code', 'display_name', 'description']


class FlightProviderSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.FlightProviderModel
        fields = ['id', 'code', 'display_name', 'description']


class HotelSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.HotelModel
        fields = ['id', 'code', 'display_name', 'description', 'stars']


class MarketSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.MarketModel
        fields = ['id', 'code', 'display_name', 'description']


class RoomTypeSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.RoomTypeModel
        fields = ['id', 'code', 'display_name', 'description']


class SupplierSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.SupplierModel
        fields = ['id', 'code', 'display_name', 'description', 'portal']
