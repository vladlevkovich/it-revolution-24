from celery import Celery
from celery.schedules import crontab
from aquarium import settings
import os


app = Celery('aquarium', broker='redis://redis:6379/0')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete_task': {
        'task': 'src.fish.tasks.notification_eat',
        'schedule': crontab(minute='*/1')
    }
}

