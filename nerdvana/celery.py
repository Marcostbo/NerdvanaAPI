import os

from django.conf import settings
from celery.schedules import crontab
from celery import Celery

# Celery Settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nerdvana.settings")
app = Celery("nerdvana", broker=settings.CELERY_BROKER_URL)

# Celery Beat Settings

app.conf.beat_schedule = {
    "new_task": {
        "task": "nerdvanapp.tasks.test_celery",
        "schedule": crontab(minute="*/1"),
    },
}

app.autodiscover_tasks()
