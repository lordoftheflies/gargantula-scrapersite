from django.conf.urls import url, include
from django.views import generic

from datastore import views

# Create a router and register our viewsets with it.
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'best_offer', views.BestOfferAPIView)

urlpatterns = [
    url('^$', generic.RedirectView.as_view(url='./best_offer/'), name="index"),
    url('^best_offer/', include(views.BestOfferViewSet().urls)),
    # url(r'^api/', include(router.urls)),
    url(r'^data/', views.BestOfferAPIView.as_view(), name='data-bestoffer')
    # url('^best_offer/input/', include(views.BestOfferOutputViewSet().urls)),
    # url('^best_offer/output/', include(views.BestOfferInputViewSet().urls)),
    # url('^journey/', include(views.JourneyViewSet().urls)),
    # url('^reservation/', include(views.ReservationViewSet().urls)),
    # url('^route/', include(views.RouteViewSet().urls)),
    # url('^jobs/', include(views.JobViewSet().urls)),
]
