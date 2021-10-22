from django.conf import settings
from celery import shared_task
from celery.decorators import task

from . import models

import sys


@shared_task
def update_status(): 
    race_object = models.Race.objects.all()
    
    race_object.status = True
    
    race_object.save() 