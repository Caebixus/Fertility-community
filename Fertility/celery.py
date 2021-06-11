from __future__ import absolute_import, unicode_literals

import os
import sys

from celery import Celery
from celery.schedules import crontab

import django
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '/home/djangoadmin/pyapps/Fertility-community')))
django.setup()
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fertility.settings')

# celery settings for the demo_project
app = Celery('Fertility')
app.config_from_object('django.conf:settings', namespace='CELERY')
# here is the beat schedule dictionary defined

app.conf.timezone = 'UTC'
app.autodiscover_tasks()

app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'
