import logging

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework import pagination
from rest_framework.response import Response
from django.contrib.auth import models as auth_model

from . import models
from . import serializers
from hydra_datastore import serializers as datastore_serializers
from hydra_datastore import models as datastore_models
from . import tasks

logger = logging.getLogger(__name__)


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = auth_model.User.objects.all()

    @action(methods=['get'], detail=False, url_name='info', url_path='info')
    def info(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        return Response()


class OrdinaryPagination(pagination.PageNumberPagination):
    page_size_query_param = 'per_page'


class ProcessViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = serializers.ProcessSerializer
    queryset = models.ProcessModel.objects.all()
    pagination_class = OrdinaryPagination

    @action(methods=['get'], detail=True, url_name='executions')
    def executions(self, request, pk=None):
        process = self.get_object()  # type: models.ProcessModel

        paginator = OrdinaryPagination()
        context = paginator.paginate_queryset(process.executions.all(), request)
        # context = process.executions
        serializer = serializers.ExecutionItemSerializer(context, many=True)
        return paginator.get_paginated_response(serializer.data)
        # return Response(serializer.data)

    @action(methods=['post'], detail=True, url_name='run')
    def run(self, request, pk=None):
        process = self.get_object()  # type: models.ProcessModel
        result = tasks.splash_notebook.delay(
            process_id=process.id,
            notebook=process.notebook_filename,
            **request.data
        )
        response = result.get()
        logger.info('process run: %s' % response)
        return Response(response)

    @action(methods=['post'], detail=True, url_name='run_with_defaults')
    def run_with_defaults(self, request, pk=None):
        process = self.get_object()  # type: models.ProcessModel
        result = tasks.splash_notebook.delay(
            process_id=process.id,
            notebook=process.notebook_filename,
            **process.parameters
        )
        response = result.get()
        logger.info('process run with default parameters: %s' % process.parameters)
        return Response(response)


class ExecutionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = serializers.ExecutionSerializer
    queryset = models.ExecutionModel.objects.all()
    pagination_class = OrdinaryPagination

    @action(methods=['post'], detail=True, url_name='restart')
    def restart(self, request, pk=None):


        execution = self.get_object()  # type: models.ExecutionModel

        result = tasks.run_process.delay(process_id=execution.process.id, **execution.arguments)
        response = result.get()
        # tasks.run_process.apply_async(process_id=pk)
        #
        # # serializer = PasswordSerializer(data=request.data)
        # # if serializer.is_valid():
        # #     user.set_password(serializer.data['password'])
        # #     user.save()
        # #     return Response({'status': 'password set'})
        # # else:
        # #     return Response(serializer.errors,
        # #                     status=status.HTTP_400_BAD_REQUEST)
        return Response(response)

    @action(methods=['post'], detail=True, url_name='stop')
    def stop(self, request, pk=None):
        # # process = self.get_object() # type: models.ProcessModel
        # tasks.run_process.apply_async(process_id=pk)
        #
        # # serializer = PasswordSerializer(data=request.data)
        # # if serializer.is_valid():
        # #     user.set_password(serializer.data['password'])
        # #     user.save()
        # #     return Response({'status': 'password set'})
        # # else:
        # #     return Response(serializer.errors,
        # #                     status=status.HTTP_400_BAD_REQUEST)
        return Response({})

    @action(detail=False, url_name='pause')
    def pause(self, request):
        # recent_users = User.objects.all().order('-last_login')
        #
        # page = self.paginate_queryset(recent_users)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        #
        # serializer = self.get_serializer(recent_users, many=True)
        # return Response(serializer.data)
        return Response({})

    @action(detail=False, url_name='resume')
    def resume(self, request):
        # recent_users = User.objects.all().order('-last_login')
        #
        # page = self.paginate_queryset(recent_users)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        #
        # serializer = self.get_serializer(recent_users, many=True)
        # return Response(serializer.data)
        return Response({})



    @action(methods=['get'], detail=True, url_name='parameters')
    def parameters(self, request, pk=None):
        execution= self.get_object()
        serializer = serializers.ArgumentSerializer(execution.parameters, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, url_name='dashboard')
    def dashboard(self, request, pk=None):
        execution = self.get_object()
        serializer = serializers.ExecutionDashbordSerializer(execution, many=False)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, url_name='results')
    def results(self, request, pk=None):

        execution = self.get_object()
        logger.info('fetch results of execution "%s"' % execution)

        entries = datastore_models.EntryModel.objects.filter(coordinates__notebook='bot').all()
        serializer = datastore_serializers.EntryDetailSerializer(entries, many=True)
        return Response(serializer.data)
    #     # process = self.get_object()  # type: models.ProcessModel
    #     process = models.ProcessModel.objects.get(id=pk)  # type: models.ProcessModel
    #
    #     paginator = pagination.PageNumberPagination()
    #     context = paginator.paginate_queryset(process.executions, request)
    #     # context = process.executions
    #     serializer = serializers.ExecutionSerializer(context, many=True)
    #     return paginator.get_paginated_response(serializer.data)
    #     # return Response(serializer.data)


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = serializers.ExecutionSerializer
    queryset = models.ExecutionModel.objects.all()

    def filter_by_status(self, status: str):
        return models.ExecutionModel.objects.filter(status=status)

    def filter_by_status_and_process_id(self, status: str, process_id):
        return models.ExecutionModel.objects.filter(status=status, process_id=process_id)

    def make_response(self, queryset):
        page = self.paginate_queryset(queryset=queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

    @action(detail=False, url_name='completed', url_path='completed')
    def completed(self, request):
        return self.make_response(queryset=self.filter_by_status(status=models.ExecutionModel.STATUS_COMPLETED))

    @action(detail=False, url_name='failed', url_path='failed')
    def failed(self, request):
        return self.make_response(queryset=self.filter_by_status(status=models.ExecutionModel.STATUS_FAILED))

    @action(detail=False, url_name='pending', url_path='pending')
    def pending(self, request):
        return self.make_response(queryset=self.filter_by_status(status=models.ExecutionModel.STATUS_PENDING))

    @action(detail=False, url_name='paused', url_path='paused')
    def paused(self, request):
        return self.make_response(queryset=self.filter_by_status(status=models.ExecutionModel.STATUS_PAUSED))

    @action(detail=False, url_name='running', url_path='running')
    def running(self, request):
        return self.make_response(queryset=self.filter_by_status(status=models.ExecutionModel.STATUS_RUNNING))

    @action(detail=True, url_name='completed_by_process', url_path='completed')
    def completed_by_process(self, request, pk):
        return self.make_response(queryset=self.filter_by_status_and_process_id(
            status=models.ExecutionModel.STATUS_COMPLETED,
            process_id=pk
        ))

    @action(detail=True, url_name='failed_by_process', url_path='failed')
    def failed_by_process(self, request, pk):
        return self.make_response(queryset=self.filter_by_status_and_process_id(
            status=models.ExecutionModel.STATUS_FAILED,
            process_id=pk
        ))

    @action(detail=True, url_name='pending_by_process', url_path='pending')
    def pending_by_process(self, request, pk):
        return self.make_response(queryset=self.filter_by_status_and_process_id(
            status=models.ExecutionModel.STATUS_PENDING,
            process_id=pk
        ))

    @action(detail=True, url_name='paused_by_process', url_path='paused')
    def paused_by_process(self, request, pk):
        return self.make_response(queryset=self.filter_by_status_and_process_id(
            status=models.ExecutionModel.STATUS_PAUSED,
            process_id=pk
        ))

    @action(detail=True, url_name='running_by_process', url_path='running')
    def running_by_process(self, request, pk):
        return self.make_response(queryset=self.filter_by_status_and_process_id(
            status=models.ExecutionModel.STATUS_RUNNING,
            process_id=pk
        ))
