from django.db import models
from datetime import datetime

# Create your models here.

class LogEntry(models.Model):
    version = models.FloatField(null=True, blank=True)
    date = models.DateField(auto_now=True)
    desc = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return f"{self.version} | {self.date} | {self.desc}"

class Task(models.Model):
    date = models.DateTimeField(blank=True, default=datetime.now)
    desc = models.CharField(blank=False, max_length=250)
    priority = models.IntegerField(default=3)
    completed = models.BooleanField(default=False)
    compDate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.priority} | {self.desc}"

class CaseEntry(models.Model):
    class Meta:
        unique_together = (('country', 'date'),)

    id = models.IntegerField(primary_key = True)
    country = models.CharField(max_length=50)
    numCases = models.IntegerField()
    numDeaths = models.IntegerField()
    endemic = models.BooleanField()
    date = models.DateField()