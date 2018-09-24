import json
import random
import time
import traceback

import datetime
from urllib.parse import urljoin

import hydra_notebook
import os

import requests
from asgiref.sync import async_to_sync
from celery import shared_task, Task, task
from celery.utils.log import get_task_logger
from channels.layers import get_channel_layer
from django.conf import settings
from scrapyd_api import ScrapydAPI
from scrapyd_api.constants import ADD_VERSION_ENDPOINT, CANCEL_ENDPOINT, DELETE_PROJECT_ENDPOINT, \
    DELETE_VERSION_ENDPOINT, LIST_JOBS_ENDPOINT, LIST_PROJECTS_ENDPOINT, LIST_SPIDERS_ENDPOINT, LIST_VERSIONS_ENDPOINT, \
    SCHEDULE_ENDPOINT, FINISHED
from scrapyd_api.exceptions import ScrapydResponseError

from engine.exceptions import SplashMiddlewareException
from . import serializers
from celery.signals import task_prerun

from . import models

logger = get_task_logger(__name__)


@task_prerun.connect(sender='engine.tasks.splash_notebook')
def task_prerun_handler(sender=None, headers=None, body=None, **kwargs):
    # information about task are located in headers for task messages
    # using the task protocol version 2.
    info = headers if 'task' in headers else body
    print('after_task_publish for task id {info[id]}'.format(
        info=info,
    ))


class ScrapyDaemonClientMixin(object):
    SCRAPY_PROJECT = settings.SCRAPY_PROJECT
    SCRAPY_SPIDER = settings.SCRAPY_SPIDER

    def __init__(self):
        super().__init__()

        logger.warning('Connect to Scrapy Daemon: %s' % settings.SCRAPYD_URL)
        self._scrapyd = ScrapydAPI(settings.SCRAPYD_URL, endpoints={
            ADD_VERSION_ENDPOINT: '%s/addversion.json' % settings.SCRAPYD_PREFIX,
            CANCEL_ENDPOINT: '%s/cancel.json' % settings.SCRAPYD_PREFIX,
            DELETE_PROJECT_ENDPOINT: '%s/delproject.json' % settings.SCRAPYD_PREFIX,
            DELETE_VERSION_ENDPOINT: '%s/delversion.json' % settings.SCRAPYD_PREFIX,
            LIST_JOBS_ENDPOINT: '%s/listjobs.json' % settings.SCRAPYD_PREFIX,
            LIST_PROJECTS_ENDPOINT: '%s/listprojects.json' % settings.SCRAPYD_PREFIX,
            LIST_SPIDERS_ENDPOINT: '%s/listspiders.json' % settings.SCRAPYD_PREFIX,
            LIST_VERSIONS_ENDPOINT: '%s/listversions.json' % settings.SCRAPYD_PREFIX,
            SCHEDULE_ENDPOINT: '%s/schedule.json' % settings.SCRAPYD_PREFIX,
        })

    @property
    def scrapyd(self) -> ScrapydAPI:
        return self._scrapyd

    def scrapy_schedule(self, **kwargs):
        scrapyd_job_id = self.scrapyd.schedule(project=self.SCRAPY_PROJECT, spider=self.SCRAPY_SPIDER, settings=kwargs)
        return scrapyd_job_id

    def scrapy_poll_job_state(self, scrapy_job_id):
        return self.scrapyd.job_status(project=self.SCRAPY_PROJECT, job_id=scrapy_job_id)


class PublisherMixin(object):
    """
    Channel layer client mixin.
    """

    def __init__(self, prefix):
        super().__init__()

        self.channel_layer = get_channel_layer()
        self.prefix = prefix

    @property
    def channel_id(self):
        raise NotImplementedError('PublisherMixin instance must implement a "channel_id" property.')

    @property
    def name(self):
        return '%s_%s' % (self.prefix, self.channel_id)

    def broadcast(self, message_type: str = 'chat_message', **kwargs):
        """
        Broadcast message through channel layer.
        :param message_type: Type of message at the consumer
        :param kwargs: Message key-value arguments
        :return:
        """
        try:
            async_to_sync(self.channel_layer.group_send)(self.name, dict(
                type=message_type,
                message=kwargs
            ))
        except BaseException as e:
            logger.error('[%s] channel error: %s' % (message_type, e.__class__))
            traceback.print_exc()

    def feedback(self, message_type: str = 'chat_message', **kwargs):
        """
        User feedback.
        :param message_type:
        :param kwargs:
        :return:
        """
        logger.warning('[%s] feedback: %s' % (
            message_type,
            json.dumps(kwargs)
        ))
        self.broadcast(message_type=message_type, **kwargs)


class EngineMixin(PublisherMixin):

    def __init__(self, prefix):
        super().__init__(prefix=prefix)

        self._process = None
        self._execution = None

    @property
    def execution(self) -> 'models.ExecutionModel':
        if self._execution is None:
            execution_id = self.request.kwargs['execution_id']
            self._execution = models.ExecutionModel.objects.get(id=execution_id)
        return self._execution

    @execution.setter
    def execution(self, value: 'models.ExecutionModel'):
        self._execution = value

    @property
    def process(self) -> 'models.ProcessModel':
        if self._process is None:
            process_id = self.request.kwargs['process_id']
            self._process = models.ProcessModel.objects.get(id=process_id)
        return self._process

    @process.setter
    def process(self, value: 'models.ProcessModel'):
        self._process = value

    def publish_state(self, message='', steps=None, progress=None, infinite=True, bubbles=False):
        # logger.info('publish state change of execution#%s: %s -> %s' % (
        #     self.execution.id,
        #     original_state,
        #     self.execution.status,
        # ))
        async_to_sync(self.channel_layer.group_send)('process_%s' % self.process.id, {
            'type': 'publish_state',
            'message': dict(
                job=serializers.ExecutionSerializer(self.execution).data,

                status=self.execution.status,
                message=message,
                steps=steps,
                progress=progress,
                infinite=infinite,
                bubbles=bubbles,
            )
        })


class ExecutionTask(Task, EngineMixin):

    def __init__(self):
        super().__init__(prefix='execution')
        logger.info('create %s task' % self.prefix)

    @property
    def channel_id(self):
        return self.execution.id

    def event_error(self, cause=None):
        event = models.EventModel.objects.create(message=str(cause), cause=cause)
        logger.error(str(event))
        return event

    def on_success(self, retval, task_id, args, kwargs):
        super().on_success(retval, task_id, args, kwargs)

        try:
            self.execution.resume()

            message = 'Execution %s#%s succeed' % (
                self.process.friendly_name,
                self.execution.id
            )
            logger.info(message)
            self.feedback(message=message)

        except BaseException as e:
            self.event_error(e)
            traceback.print_exc()

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        super().on_retry(exc, task_id, args, kwargs, einfo)

        try:
            self.execution.pause()

            message = 'Execution %s#%s retry' % (
                self.process.friendly_name,
                self.execution.id
            )
            logger.info(message)
            self.feedback(message=message)

        except BaseException as e:
            self.event_error(e)
            traceback.print_exc()

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        super().on_failure(exc, task_id, args, kwargs, einfo)

        try:
            self.execution.fail()
            logger.error(str(exc))

        except BaseException as e:
            self.event_error(e)
            traceback.print_exc()

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        super().after_return(status, retval, task_id, args, kwargs, einfo)

        try:
            message = 'Execution %s#%s processed' % (
                self.process.friendly_name,
                self.execution.id
            )
            logger.info(message)
            self.feedback(message=message)

        except BaseException as e:
            self.event_error(e)
            traceback.print_exc()


class JobTask(Task, EngineMixin):

    def __init__(self) -> None:
        super().__init__(prefix='execution')
        logger.info('create task')

    @property
    def channel_id(self):
        return self.execution.id

    def on_success(self, retval, task_id, args, kwargs):
        super().on_success(retval, task_id, args, kwargs)

        try:
            self.execution.complete()

            message = 'Execution %s#%s succeed' % (
                self.process.friendly_name,
                self.execution.id
            )
            logger.info(message)
            self.feedback(message=message)
            self.publish_state(
                message=message,
                progress=5,
                steps=5,
                infinite=True,
                bubbles=False,
            )

        except BaseException as e:
            self.event_error(e)
            traceback.print_exc()

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        super().on_failure(exc, task_id, args, kwargs, einfo)

        try:
            self.execution.fail()
            logger.error(str(exc))
            self.publish_state(
                message=str(exc),
                infinite=True,
                bubbles=True,
            )

        except BaseException as e:
            self.event_error(e)
            traceback.print_exc()


class SplashScrapyExecutionTask(ExecutionTask, ScrapyDaemonClientMixin):

    def __init__(self):
        super().__init__()


class SplashScrapyJobTask(JobTask, ScrapyDaemonClientMixin):

    def __init__(self):
        super().__init__()


@shared_task(base=SplashScrapyExecutionTask, bind=True, ignore_result=False, serializer='json', track_started=True)
def splash_notebook(self: SplashScrapyExecutionTask, **kwargs):
    response = {}
    try:
        self.process = models.ProcessModel.objects.get(id=kwargs['process_id'])  # type: models.ProcessModel
        self.execution = models.ExecutionModel.objects.create(
            process=self.process,
            started=datetime.datetime.now()
        )  # type: models.ExecutionModel

        entities = dict(
            execution_id=self.execution.id,
            # process_id=self.process.id,
        )

        # self.publish_state(original_state=None)
        logger.warning('Start task[%s] with arguments: %s' % (
            self.request.id,
            json.dumps(kwargs, indent=4, sort_keys=True)
        ))

        kwargs_with_entities = dict(
            **entities,
            **kwargs
        )

        scrapyd_job_id = self.scrapy_schedule(**kwargs_with_entities)
        logger.warning('Task[%s] started scrapy-job[%s]' % (self.request.id, scrapyd_job_id))
        scrapyjob = dict(
            scrapy_job_id=scrapyd_job_id
        )
        self.publish_state(
            message='Scrapy job[%s] started' % scrapyd_job_id,
            infinite=True,
            progress=0,
            steps=5,
            bubbles=True,
        )

        context = dict(
            arguments=kwargs,
            **kwargs_with_entities,
            **scrapyjob,
            # **kwargs
        )

        scrapy_observer.delay(**context)

        return context
    except ScrapydResponseError as scrapy_error:
        # message = 'Task[%s] failed: %s' % (self.request.id, str(scrapy_error))
        # logger.warning(message)
        # return dict(message=message, cause=str(scrapy_error))
        raise SplashMiddlewareException(scrapy_error)
    except requests.exceptions.ConnectionError as connection_error:
        # message = 'Scrapy Daemon client failed to connect "%s"' % settings.SCRAPYD_URL
        # logger.warning(message)
        # return dict(message=message, cause=str(connection_error))
        raise SplashMiddlewareException(connection_error)
    except BaseException as e:
        message = 'Server side error'
        logger.error(message)
        traceback.print_exc()
        return dict(message=message, cause=str(e))


@shared_task(base=SplashScrapyJobTask, bind=True, ignore_result=True, serializer='json', track_started=True)
def scrapy_observer(self: SplashScrapyJobTask, scrapy_job_id, process_id, execution_id, poll_time=5, **kwargs):
    state = 'INITIAL'

    self.process = models.ProcessModel.objects.get(id=process_id)  # type: models.ProcessModel
    self.execution = models.ExecutionModel.objects.get(id=execution_id)  # type: models.ExecutionModel

    if 'arguments' in kwargs:
        self.execution.configure(**kwargs['arguments'])
    else:
        self.execution.configure(**self.process.parameters)

    self.execution.start()
    self.publish_state(
        message='Started',
        progress=1,
        steps=5,
        infinite=True,
        bubbles=False
    )

    while state != FINISHED:
        # while True:
        try:
            state = self.scrapy_poll_job_state(scrapy_job_id=scrapy_job_id)
            logger.debug('task[%s] polling scrapy-job[%s], state=%s' % (self.request.id, scrapy_job_id, state))
            self.publish_state(
                message='Working ...',
                progress=3,
                steps=5,
                infinite=True,
                bubbles=False
            )
            time.sleep(poll_time)
        except ScrapydResponseError as scrapy_error:
            logger.error('Task[%s] failed: %s' % (self.request.id, str(scrapy_error)))
            traceback.print_exc()
        finally:
            self.publish_state(
                message='Finished',
                progress=4,
                steps=5,
                infinite=True,
                bubbles=False
            )

            self.feedback(
                task=self.request.id,
                job=scrapy_job_id,
                state=state,
            )


@shared_task(base=JobTask, bind=True, ignore_result=True, serializer='json', track_started=True)
def job(self, **kwargs):
    try:
        self.process = models.ProcessModel.objects.get(id=kwargs['process_id'])  # type: models.ProcessModel
        self.execution = models.ExecutionModel.objects.get(id=kwargs['execution_id'])  # type: models.ExecutionModel
        self.publish_state(original_state=None)

        time.sleep(3)

        message_start = 'Run process "%s" start execution #%s' % (
            self.process.friendly_name,
            self.execution.id
        )
        logger.info(message_start)
        # if 'arguments' in kwargs:
        #     self.execution.configure(**kwargs['arguments'])
        original_state = self.execution.status
        self.execution.start()

        logger.warning('Begin notebook "%s" from process "%s" ...' % (
            self.process.notebook,
            self.process.friendly_name
        ))
        with hydra_notebook.NotebookExecutor(
                path=settings.NOTEBOOKS_ROOT,
                fullname=os.path.splitext(self.process.notebook)[0]
        ) as e:
            e()
        logger.warning('End notebook "%s" from process "%s" ...' % (
            self.process.notebook,
            self.process.friendly_name
        ))

        original_state = self.execution.status
        self.execution.stop()

        # self.feedback(
        #     execution_id=self.execution.id,
        #     process_id=self.process.id,
        #     dataset=datastore_serializers.DatasetDetailSerializer(dataset).data,
        #     message='Data collection completed',
        #     execution=serializers.ExecutionSerializer(self.execution).data
        # )
    except BaseException as e:
        logger.error(str(e))
        traceback.print_exc()


@shared_task(bind=True, ignore_result=False)
def run_process(self, process_id, **kwargs):
    try:
        process = models.ProcessModel.objects.get(id=process_id)  # type: models.ProcessModel
        execution = process.start()  # type: models.ExecutionModel
        execution.configure(**kwargs)
        result = dict(
            execution_id=execution.id,
            process_id=process.id,
            arguments=kwargs
        )

        job.apply_async(kwargs=result)

        return result
    except BaseException as e:
        logger.error(str(e))
        traceback.print_exc()


def kill_job():
    pass
