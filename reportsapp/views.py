from django.shortcuts import render
from material.frontend.views import ModelViewSet
from reportsapp import models as reportsapp_models



class ReportViewSet(ModelViewSet):
    model = reportsapp_models.ReportModel
    list_display = ['definition']

# class ReportViewSet(rest_viewsets.ReadOnlyModelViewSet):
# #     """
# #     This viewset automatically provides `list` and `detail` actions ReportModel.
# #     """
#     queryset = report_models.Report.objects.all()
#     serializer_class = botapp_serializers.ProjectItemSerializer
# #
# #     @detail_route(renderer_classes=[rest_renderers.BrowsableAPIRenderer])
# #     def long_details(self, request, *args, **kwargs):
# #         project = self.get_object()
# #         return Response(project)


def reporting_polymer_view(request):
    return render(
        request=request,
        template_name='reportsapp/spa.html',
        context={
        })