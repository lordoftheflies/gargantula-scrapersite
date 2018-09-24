from __future__ import absolute_import

import os

import dotenv
from celery import Celery
from django.conf import settings as django_settings

dotenv_path = os.path.join(str(os.path.expanduser('~')), '.gargantula')
dotenv.load_dotenv(dotenv_path=dotenv_path)

ENVIRONMENT = os.getenv('ENVIRONMENT')

if ENVIRONMENT == 'STAGING':
    settings = 'staging'
elif ENVIRONMENT == 'PRODUCTION':
    settings = 'production'
else:
    settings = 'development'

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrapersite.settings')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'scrapersite.settings'
os.environ.setdefault('DJANGO_CONFIGURATION', settings.title())

import configurations

configurations.setup()

app = Celery('scrapersite')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
# app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: django_settings.INSTALLED_APPS)


# app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
