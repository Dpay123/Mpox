from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from datetime import datetime

from . import convert
from .forms import *

def index(request):
    if request.method == 'GET':
        cases = CaseEntry.objects.all()
        context = {
            'cases': cases,
            'form': DateFilter()
        }
        return render(request, "app/index.html", context)
    else:
        # dateInput variable stores format 'yyyy-mm-dd'
        dateInput = request.POST['date']
        cases = CaseEntry.objects.filter(date=dateInput)
        context = {
            'cases': cases,
            'form': DateFilter(request.POST),
            'date': dateInput
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
    