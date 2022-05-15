from __future__ import absolute_import, unicode_literals

from config.celery import celery_app

__all__ = ('celery_app',)

try:
    from config.local import *
except ImportError:
    from config.settings import *
