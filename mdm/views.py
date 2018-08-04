from material.frontend import views as material_views

from mdm import models as mdm_models


class AirportViewSet(material_views.ModelViewSet):
    model = mdm_models.AirportModel
    list_display = ['display_name', 'code']


class BagTypeViewSet(material_views.ModelViewSet):
    model = mdm_models.BagTypeModel
    list_display = ['display_name', 'weight']


class BoardViewSet(material_views.ModelViewSet):
    model = mdm_models.BoardModel


class FlightProviderViewSet(material_views.ModelViewSet):
    model = mdm_models.FlightProviderModel
    list_display = ['display_name', 'code']


class HotelViewSet(material_views.ModelViewSet):
    model = mdm_models.HotelModel
    list_display = ['display_name', 'stars']


class MarketViewSet(material_views.ModelViewSet):
    model = mdm_models.MarketModel
    list_display = ['display_name', 'code']


class RoomTypeViewSet(material_views.ModelViewSet):
    model = mdm_models.RoomTypeModel


class SupplierListView(material_views.ListModelView):
    model = mdm_models.SupplierModel
    template_name = 'mdm/supplier-list.html'


class SupplierViewSet(material_views.ModelViewSet):
    model = mdm_models.SupplierModel
    list_display = ['display_name', 'portal']
    list_view_class = SupplierListView
