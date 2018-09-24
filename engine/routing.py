from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/status/(?P<process_id>[^/]+)/$', consumers.ProcessConsumer),
    url(r'^ws/execution/(?P<execution_id>[^/]+)/$', consumers.ChatConsumer),
]