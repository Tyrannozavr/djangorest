import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'json_api_auth.settings')

app = Celery('json_api_auth')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')