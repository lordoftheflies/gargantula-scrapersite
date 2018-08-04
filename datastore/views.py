from django.shortcuts import render

# Create your views here.
from material.frontend.views import ModelViewSet
from datastore import models as data_models
from botapp import models as bot_models
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from datastore import serializers as data_serializers


class BestOfferViewSet(ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions ProjectModel.
    """
    model = data_models.BestOfferModel

    list_display = ['timestamp', 'duration', 'supplier', 'market', 'departure', 'arrival', 'lowest_price', 'bag_weight', 'bag_price']


    # layout = Layout(
    #     Row('name', 'parent'),
    #     'ocean',
    #     Row('area', 'avg_depth', 'max_depth'),
    #     'basin_countries'
    # )

    #
    # class JourneyViewSet(ModelViewSet):
    #     """
    #     This viewset automatically provides `list` and `detail` actions ProjectModel.
    #     """
    #     model = data_models.JourneyModel
    #
    #
    # class RouteViewSet(ModelViewSet):
    #     """
    #     This viewset automatically provides `list` and `detail` actions ProjectModel.
    #     """
    #     model = data_models.RouteModel
    #
    #
    # class ReservationViewSet(ModelViewSet):
    #     """
    #     This viewset automatically provides `list` and `detail` actions ProjectModel.
    #     """
    #     model = data_models.ReservationModel


class BestOfferAPIView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        items = data_models.BestOfferModel.objects.all()
        serializer = data_serializers.BestOfferSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = data_serializers.BestOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
