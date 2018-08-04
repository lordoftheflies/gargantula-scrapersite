from __future__ import absolute_import, unicode_literals
from scrapersite.version import __version__
from .celery import app as celery_app
__all__ = ['celery_app']
