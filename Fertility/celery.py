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

app.config_from_object(settings)
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
