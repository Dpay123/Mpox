from sqlite3 import IntegrityError
from tkinter.tix import INTEGER
from django.shortcuts import render, redirect
from django.db.models import Sum
from datetime import datetime

from . import convert
from .forms import *

def index(request):
    message = 'Select Filter'
    if request.method == 'GET':
        context = {
            'message': message,
            'form': Filter()
        }
        return render(request, "app/index.html", context)
    else:
        # dateInput variable stores format 'yyyy-mm-dd'
        dateInput = request.POST['date']
        countryInput = request.POST['country']
        if countryInput:
            cases = CaseEntry.objects.filter(date=dateInput, country=countryInput)
            totalC = CaseEntry.objects.filter(date=dateInput, country=countryInput).aggregate(Sum('numCases'))
            totalD = CaseEntry.objects.filter(date=dateInput, country=countryInput).aggregate(Sum('numDeaths'))
        else:
            cases = CaseEntry.objects.filter(date=dateInput)
            totalC = CaseEntry.objects.filter(date=dateInput).aggregate(Sum('numCases'))
            totalD = CaseEntry.objects.filter(date=dateInput).aggregate(Sum('numDeaths'))
        context = {
            'message': message,
            'cases': cases,
            'form': Filter(request.POST),
            'totalC': totalC['numCases__sum'],
            'totalD': totalD['numDeaths__sum']
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
    