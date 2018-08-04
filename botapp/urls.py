from django.conf.urls import url, include
from django.views import generic

from botapp import views

# Create a router and register our viewsets with it.
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'projects', views.ProjectViewSet)

urlpatterns = [
    url('^$', generic.RedirectView.as_view(url='./portal/'), name="index"),
    url(r'^api/', include(router.urls)),
    # url('^scrapy_daemon/', views.scrapy_daemon_index, name="scrapy_daemon"),
    # url('^scrapy_schedule/', views.JobDetailsView.as_view(), name="scrapy_schedule"),
    url('^scrapy_schedule/', views.scrapy_schedule, name="scrapy_schedule"),
    # url('^project/', include(views.ProjectModelViewSet().urls)),

    url('^portal/', include(views.PortalModelViewSet().urls)),
    url('^comparison/', include(views.ComparisonModelViewSet().urls)),
    # url('^parameter/', include(views.ParameterViewSet().urls)),
    url('^jobs/', include(views.BestOfferJobViewSet().urls)),
    url('^jobs/(?P<pk>.+)/multi/', view=views.multi_job_detail_view, name='bestofferjobmodel_multi'),
]