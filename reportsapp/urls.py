from django.conf.urls import url, include
from django.views import generic
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
# router.register(r'reports', views.ReportViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url('^$', generic.RedirectView.as_view(url='./history/'), name="index"),
    url('^reporting/', view=views.reporting_polymer_view, name='reporting_frontend'),
    url('^history/', include(views.ReportViewSet().urls)),
]