from django.db import models

# Create your models here.

class LogEntry(models.Model):
    version = models.FloatField(null=True, blank=True)
    date = models.DateField(auto_now=True)
    desc = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return f"{self.version} | {self.date} | {self.desc}"

class Task(models.Model):
    desc = models.CharField(blank=False, max_length=250)
    priority = models.IntegerField(default=3)

    def __str__(self):
        return f"{self.priority} | {self.desc}"