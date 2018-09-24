import importlib

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

engine_routing = importlib.import_module(name='engine.routing')

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)

    "websocket": AuthMiddlewareStack(
        URLRouter(engine_routing.websocket_urlpatterns)
    ),
})
