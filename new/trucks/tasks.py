from __future__ import absolute_import, unicode_literals
from celery import shared_task, task
import time
from .models import *

'''
@shared_task
def xsum(numbers):
    return sum(numbers)
'''


@task(name="delete read")
def delete_notifications():
    obj = Notifications.objects.all()
    for i in obj:
        if(i.boolean is False):
            i.delete()
    print("ds")
