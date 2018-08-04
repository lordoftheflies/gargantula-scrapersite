
from django.views.generic.base import TemplateView
from django.conf import settings


class CubesViewerView(TemplateView):

    template_name = "cubesviewer/index.html"
    exclude = ()

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context["cubesviewer_cubes_url"] = settings.CUBESVIEWER_CUBES_URL
        context["cubesviewer_backend_url"] = settings.CUBESVIEWER_BACKEND_URL
        return context

