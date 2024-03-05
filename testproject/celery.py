from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testproject.settings')

app = Celery('testproject')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')
app.conf.beat_schedule = {
    'work-at-every-5':{
        'task': 'testapp.tasks.change',
        'schedule':crontab(minute='*')
    }
}
app.autodiscover_tasks()