from django.conf import settings
from celery import shared_task
from celery.decorators import task

from . import models

import sys


@shared_task
def update_status(): 
    race_object = models.Race.objects.all()
    
    for obj in race_object:
        if obj.status is True:
            obj.status = False
            obj.save()
        else:
            obj.status = True
            obj.save()