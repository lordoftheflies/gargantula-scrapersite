from django.conf.urls import url, include
from django.views import generic

from . import views

from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'process', views.ProcessViewSet)
router.register(r'execution', views.ExecutionViewSet)
router.register(r'job', views.JobViewSet)

urlpatterns = [
    url('^$', generic.RedirectView.as_view(url='./portal/'), name="index"),
    url(r'^api/', include(router.urls)),

 ]