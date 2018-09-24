from django.conf.urls import url, include
from django.views import generic
from rest_framework.routers import DefaultRouter
from . import views as mdm_views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'airport', mdm_views.AirportViewSet)
router.register(r'bagtype', mdm_views.BagTypeViewSet)
router.register(r'board', mdm_views.BoardViewSet)
router.register(r'flightprovider', mdm_views.FlightProviderViewSet)
router.register(r'hotel', mdm_views.HotelViewSet)
router.register(r'market', mdm_views.MarketViewSet)
router.register(r'roomtype', mdm_views.RoomTypeViewSet)
router.register(r'supplier', mdm_views.SupplierViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
