from __future__ import absolute_import, unicode_literals

import os
import sys

from celery import Celery
from celery.schedules import crontab

from django.conf import settings
from django.apps import apps

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fertility.settings')

# celery settings for the demo_project
app = Celery('Fertility')
app.config_from_object('django.conf:settings', namespace='CELERY')
# here is the beat schedule dictionary defined


app.autodiscover_tasks()

from celery.schedules import crontab
CELERY_BEAT_SCHEDULE = {
    'task-number-one': {
        'task': 'base.tasks.calculate_dti',
        'schedule': 30
    },
    'task-number-two': {
        'task': 'clinic.tasks.currencies_rate_update',
        'schedule': 15
    },
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
