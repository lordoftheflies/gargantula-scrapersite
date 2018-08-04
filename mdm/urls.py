from django.conf.urls import url, include
from django.views import generic

from mdm import views as mdm_views

urlpatterns = [
    url('^$', generic.RedirectView.as_view(url='./supplier/'), name="index"),
    url('^airport/', include(mdm_views.AirportViewSet().urls)),
    url('^bagtype/', include(mdm_views.BagTypeViewSet().urls)),
    url('^board/', include(mdm_views.BoardViewSet().urls)),
    url('^flight/', include(mdm_views.FlightProviderViewSet().urls)),
    url('^hotel/', include(mdm_views.HotelViewSet().urls)),
    url('^market/', include(mdm_views.MarketViewSet().urls)),
    url('^roomtype/', include(mdm_views.RoomTypeViewSet().urls)),
    url('^supplier/', include(mdm_views.SupplierViewSet().urls))
]
