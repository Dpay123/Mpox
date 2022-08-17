from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.forms import ModelForm
import csv
from datetime import datetime

from .models import *
from . import convert

class LogEntryForm(ModelForm):
    class Meta:
        model = LogEntry
        fields = ['version', 'desc']

class TaskEntryForm(ModelForm):
    class Meta:
        model = Task
        fields = ['priority', 'desc']    

def index(request):
    # get raw data conversion from .csv
    data = convert.convert()
    # store into db
    CaseEntry.objects.bulk_create([CaseEntry(**{
        'country': d['country'],
        'numCases': d['cases'],
        'numDeaths': d['deaths'],
        'endemic': d['endemic'],
        'date': d['date']
    }) for d in data], ignore_conflicts=True)
    cases = CaseEntry.objects.all()
    context = {
        'cases': cases
    }
    return render(request, "app/index.html", context)

def todo(request):
    if request.method == 'GET':
        tasks = Task.objects.all().order_by('priority').values()
        form = TaskEntryForm()
        context = {
            "tasks": tasks,
            "form": form
        }
        return render(request, 'app/todo.html', context)
    else:
        form = TaskEntryForm(request.POST)
        if form.is_valid():
            entry = form.save()
            return redirect('todo')

def log(request):
    if request.method == 'GET':
        logs = LogEntry.objects.all()
        form = LogEntryForm()
        context = {
            "logs": logs,
            "form": form
        }
        return render(request, 'app/log.html', context)

    else:
        form = LogEntryForm(request.POST)
        if form.is_valid():
            entry = form.save()
            return redirect("log")
    