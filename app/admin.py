from distutils.log import Log
from django.contrib import admin

from .models import LogEntry, Task
from .models import *
# Register your models here.
admin.site.register(LogEntry)
admin.site.register(Task)