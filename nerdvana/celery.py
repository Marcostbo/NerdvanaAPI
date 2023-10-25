import os

from django.conf import settings
from celery.schedules import crontab
from celery import Celery

# Celery General Settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nerdvana.settings")
app = Celery("nerdvana", broker=settings.CELERY_BROKER_URL)

# Celery Tasks Settings

app.conf.task_routes = {
    'notification.tasks.send_email': {'queue': 'email_sending'}
}

# Celery Beat Settings

app.conf.beat_schedule = {
    "new_task": {
        "task": "nerdvanapp.tasks.evaluate_price_alerts",
        "schedule": crontab(minute="*/3"),
        "options": {"queue": "game_pricing"}
    },
}

app.autodiscover_tasks()
