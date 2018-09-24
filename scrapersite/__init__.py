from __future__ import absolute_import, unicode_literals

import logging

import sys

from django.core.management import color_style

from .version import __version__
from .celery import app as celery_app
__all__ = ['celery_app']
