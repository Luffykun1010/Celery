from celery import Celery,shared_task
from .models import YourModel

@shared_task(bind=True)
def change(self):
    for i in YourModel.objects.all():
        i.a = int(i.a) + 1
        i.save()