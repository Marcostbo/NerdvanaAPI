import os

from django.conf import settings
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nerdvana.settings")
app = Celery("nerdvana", broker=settings.CELERY_BROKER_URL)
