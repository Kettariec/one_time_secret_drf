from celery import shared_task
from datetime import datetime
from keep_secrets.models import Secret
import pytz
from django.conf import settings


@shared_task
def check_secrets():
    zone = pytz.timezone(settings.TIME_ZONE)
    now = datetime.now(zone)

    secrets = Secret.objects.filter(time__lte=now)

    for secret in secrets:
        secret.delete()
