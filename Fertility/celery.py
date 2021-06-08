from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fertility.settings')
# celery settings for the demo_project
app = Celery('Fertility')
app.config_from_object('django.conf:settings', namespace='CELERY')
# here is the beat schedule dictionary defined

app.conf.beat_schedule = {
    'calculate-dti-every-10-sec': {
        'task': 'base.tasks.calculate_dti',
        'schedule': 5.0
    },
}

app.conf.timezone = 'UTC'
app.autodiscover_tasks()
