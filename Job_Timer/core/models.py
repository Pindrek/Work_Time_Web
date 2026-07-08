from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class WorkSession(models.Model):
    progress_bar = models.IntegerField(default=0)
    progress = models.DurationField(default=timedelta(hours=0, minutes=0, seconds=0))
    date = models.DateField(default=timezone.localdate)

    def __str__(self):
        return f"progress bar: {self.progress_bar} | progress: {self.progress} | date: {self.date}"