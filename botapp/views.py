import logging

from botapp import forms as bot_forms
from botapp import models as botapp_models
from datastore import models as data_models
from django.forms import inlineformset_factory
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.urls import reverse
from material.frontend import views as material_views
from material.frontend.views import ModelViewSet
from scrapyd_api import ScrapydAPI

# from django.forms.formsets import formset_factory
# scrapyd = ScrapydAPI('http://box.cherubits.hu:6800')
scrapyd = ScrapydAPI('http://localhost:6800')

logger = logging.getLogger(__name__)


class PortalDetailsView(material_views.DetailModelView):
    model = botapp_models.PortalModel
    template_name = 'botapp/portal-details.html'


def upload_lua_source(request, pk):
    portal = botapp_models.PortalModel.objects.get(pk=pk)
    # Handle file upload
    if request.method == 'POST':
        form = bot_forms.LuaSourceForm(request.POST, request.FILES)
        if form.is_valid():
            portal.lua_source = request.FILES['file']
            portal.save()
            logger.info('project[%s] successfully uploaded LUA source: %s' % (portal.name, portal.lua_source.name))
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('botapp:portalmodel_detail', kwargs={'pk': portal.pk}))
        else:
            logger.warning('project[%s] LUA source upload failed: %s' % (portal.name, portal.lua_source.name))
    else:
        form = bot_forms.LuaSourceForm()  # A empty, unbound form

        logger.debug('project[%s] upload LUA source ...' % portal.name)
    return render(request, 'botapp/portal-upload-source.html', {
        'form': form,
        'model': botapp_models.PortalModel,
        'object': portal
    })


def scrapy_schedule(request, pk):
    portal = botapp_models.PortalModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = bot_forms.BestOfferInputForm(request.POST)
        if form.is_valid():
            job = portal.start_job(form.instance)
            return HttpResponseRedirect(reverse('botapp:bestofferjobmodel_detail', kwargs={'pk': job.pk}))
    else:
        job = botapp_models.BestOfferJobModel(portal=portal, data=data_models.BestOfferModel())
        form = bot_forms.BestOfferInputForm(instance=job.data)

    return render(
        request=request,
        template_name='botapp/datacollection-details.html',
        context={
            'form': form,
            'model': botapp_models.PortalModel,
            'object': portal
        })


class PortalModelViewSet(ModelViewSet):
    model = botapp_models.PortalModel
    detail_view_class = PortalDetailsView

    upload_lua_source_view = [
        r'^(?P<pk>.+)/upload/$',
        upload_lua_source,
        '{model_name}_upload_lua_source'
    ]

    scrapy_schedule_view = [
        r'^(?P<pk>.+)/schedule/$',
        scrapy_schedule,
        '{model_name}_scrapy_schedule'
    ]

def multi_job_detail_view(request, pk):
    return render(
        request=request,
        template_name='botapp/multi-job-details.html',
        context={
            'model': botapp_models.BestOfferJobModel,
            'object': botapp_models.BestOfferJobModel.objects.get(pk=pk)
        })

def scrapy_schedule_comparison(request, pk):
    comparison = botapp_models.ComparisonModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = bot_forms.BestOfferInputForm(request.POST)
        if form.is_valid():
            job = comparison.start_job(form.instance)
            return HttpResponseRedirect(reverse('botapp:bestofferjobmodel_multi', kwargs={'pk': job.pk}))
    else:
        job = botapp_models.BestOfferJobModel(comparison=comparison, data=data_models.BestOfferModel())
        form = bot_forms.BestOfferInputForm(instance=job.data)

    return render(
        request=request,
        template_name='botapp/multi-datacollection-details.html',
        context={
            'form': form,
            'model': botapp_models.ComparisonModel,
            'object': comparison
        })


class ComparisonDetailView(material_views.DetailModelView):
    model = botapp_models.ComparisonModel
    template_name = 'botapp/comparison-details.html'


class ComparisonModelViewSet(ModelViewSet):
    model = botapp_models.ComparisonModel
    detail_view_class = ComparisonDetailView

    scrapy_schedule_view = [
        r'^(?P<pk>.+)/schedule/$',
        scrapy_schedule_comparison,
        '{model_name}_scrapy_schedule'
    ]


class BestOfferJobDetailsView(material_views.DetailModelView):
    model = botapp_models.BestOfferJobModel
    template_name = 'botapp/job-details.html'



class BestOfferJobViewSet(ModelViewSet):
    model = botapp_models.BestOfferJobModel
    detail_view_class = BestOfferJobDetailsView
#
#
# class ParameterViewSet(ModelViewSet):
#     model = botapp_models.ParameterModel

#
#
#
#
#
# class ProjectViewSet(rest_viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions ProjectModel.
#     """
#     queryset = botapp_models.ProjectModel.objects.all()
#     serializer_class = botapp_serializers.ProjectItemSerializer
#
#     @detail_route(renderer_classes=[rest_renderers.BrowsableAPIRenderer])
#     def long_details(self, request, *args, **kwargs):
#         project = self.get_object()
#         return Response(project)
#
#
# # class JobViewSet(rest_viewsets.ModelViewSet):
# #     """
# #     This viewset automatically provides `list`, `create`, `retrieve`,
# #     `update` and `destroy` actions for .
# #
# #     Additionally we also provide an extra `highlight` action.
# #     """
# #     queryset = botapp_models.ProjectStepModel.objects.all()
# #     serializer_class = botapp_serializers
# #     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
# #                           IsOwnerOrReadOnly,)
# #
# #     @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
# #     def highlight(self, request, *args, **kwargs):
# #         snippet = self.get_object()
# #         return Response(snippet.highlighted)
# #
# #     def perform_create(self, serializer):
# #         serializer.save(owner=self.request.user)
#
#
# class ProjectList(generics.ListCreateAPIView):
#     queryset = botapp_models.ProjectModel.objects.all()
#     serializer_class = botapp_serializers.ProjectItemSerializer
#
#
# class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = botapp_models.ProjectModel.objects.all()
#     serializer_class = botapp_serializers.ProjectDetailsSerializer
#
#
# # Create your views here.
# class ProjectDetailsView(material_views.DetailModelView):
#     model = botapp_models.ProjectModel
#     template_name = 'botapp/project-details.html'
#
#
#
#
# class ProjectModelViewSet(ModelViewSet):
#     model = botapp_models.ProjectModel
#     detail_view_class = ProjectDetailsView
#
#
#
#
# def scrapy_daemon_index(request):
#     try:
#         projects = scrapyd.list_projects()
#         response = {'projects': []}
#
#         for p in projects:
#             project = {
#                 'spiders': [],
#                 'name': p,
#                 # 'versions': scrapyd.list_versions(project=p)
#             }
#             # spiders = scrapyd.list_spiders(p)
#             # for s in spiders:
#             #     project['spiders'].append(s)
#             response['projects'].append(project)
#     except Exception:
#         raise Http404("Could not communicate with Scrapy Daemon on")
#     return render(request, 'botapp/daemon-dashboard.html', response)
#
#
# #
# #
# #
# # #
# # def scrapy_schedule(request):
# #     # if this is a POST request we need to process the form data
# #     if request.method == 'POST':
# #         # create a form instance and populate it with data from the request:
# #         form = bot_forms.ScheduleForm(request.POST)
# #         # check whether it's valid:
# #         if form.is_valid():
# #             # process the data in form.cleaned_data as required
# #             project = form.cleaned_data['project']
# #             p = botapp_models.ProjectModel.objects.get(pk=project.pk)
# #             scrapy_job_id = scrapyd.schedule(project=p.scrapy, spider=p.spider, project_id=p.pk)
# #             job = p.start_job(job_id=scrapy_job_id)
# #             # redirect to a new URL:
# #             return HttpResponseRedirect(reverse('botapp:jobmodel_detail', kwargs={'pk': job.pk}))
# #
# #     # if a GET (or any other method) we'll create a blank form
# #     else:
# #         form = bot_forms.ScheduleForm()
# #
# #     return render(request, 'botapp/datacollection-details.html', {'form': form})
#
#
# @csrf_exempt
# def job_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         return JsonResponse(scrapyd.list_projects(), safe=False)
#
#
# @csrf_exempt
# def project_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         projects = botapp_models.ProjectModel.objects.projects()
#         serializer = botapp_serializers.ProjectItemSerializer(projects, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#         # elif request.method == 'POST':
#         #     data = JSONParser().parse(request)
#         #     serializer = SnippetSerializer(data=data)
#         #     if serializer.is_valid():
#         #         serializer.save()
#         #         return JsonResponse(serializer.data, status=201)
#         #     return JsonResponse(serializer.errors, status=400)
