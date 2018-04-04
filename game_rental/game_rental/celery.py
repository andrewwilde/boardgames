from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_rental.settings')

app = Celery('game_rental', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = { 'popularity': { 'task': 'kickstarters.tasks.store_kickstarters',
                                            'schedule': crontab(hour=8, minute=0),
                                            'args': ['popularity', 15] },
                           'end_date': { 'task': 'kickstarters.tasks.store_kickstarters',
                                            'schedule': crontab(hour=8, minute=0),
                                            'args': ['newest', 15] },
                           'newest':      { 'task': 'kickstarters.tasks.store_kickstarters',
                                            'schedule': crontab(hour=8, minute=0),
                                            'args': ['end_date', 15] }
                         }

# Load task modules from all registered Django app configs.
