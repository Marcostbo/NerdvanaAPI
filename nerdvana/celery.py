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
        "task": "nerdvanapp.tasks.evaluate_price_alerts",
        "schedule": crontab(minute="*/3"),
    },
}

app.autodiscover_tasks()
