from __future__ import absolute_import, unicode_literals

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fertility.settings')
import sys

from celery import Celery
from celery.schedules import crontab


from django.conf import settings


# celery settings for the demo_project
app = Celery('Fertility')
app.config_from_object('django.conf:settings', namespace='CELERY')
# here is the beat schedule dictionary defined


app.autodiscover_tasks()

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_BEAT_SCHEDULE = {
    'dti-calc': {
        'task': 'base.tasks.calculate_dti',
        'schedule': 30
        }
    }
