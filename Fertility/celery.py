from __future__ import absolute_import, unicode_literals

import os
import sys

from celery import Celery
from celery.schedules import crontab

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fertility.settings')

# celery settings for the demo_project
app = Celery('Fertility')
app.config_from_object('django.conf:settings', namespace='CELERY')
# here is the beat schedule dictionary defined


app.autodiscover_tasks()

app.conf.beat_schedule = {
    'dti-calc': {
        'task': 'dti-calc',
        'schedule': 3600
    },
    'currencies_rate_update': {
        'task': 'currencies_rate_update',
        'schedule': 30

    },
}
