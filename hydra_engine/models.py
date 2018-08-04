from django.db import models

EXECUTION_STATE_PENDING = 'pending'
EXECUTION_STATE_RUNNING = 'running'
EXECUTION_STATE_COMPLETED = 'completed'
EXECUTION_STATE_FAILED = 'failed'
EXECUTION_STATES = [
    (EXECUTION_STATE_PENDING, 'Pending'),
    (EXECUTION_STATE_RUNNING, 'Running'),
    (EXECUTION_STATE_COMPLETED, 'Completed'),
    (EXECUTION_STATE_FAILED, 'Failed'),
]

# Create your models here.
class ProcessModel(models.Model):
    pass

class TaskModel(models.Model):
    pass

class ExecutionModel(models.Model):
    started = models.DateTimeField()
    ended = models.DateTimeField()
    state = models.CharField(choices=EXECUTION_STATES, default=EXECUTION_STATE_PENDING)
    process = models.ForeignKey(to=ProcessModel, related_name='executions')

