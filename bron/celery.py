import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bron.settings")

app = Celery("bron")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
