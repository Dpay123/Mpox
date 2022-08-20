from datetime import datetime
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse
import csv

from .models import *
from .forms import *
from .modules import convert

def removeTask(request, id):
    Task.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('todo'))

def completeTask(request, id):
    Task.objects.filter(id=id).update(completed=True, compDate=datetime.now())
    return HttpResponseRedirect(reverse('todo'))

def update(request):
    # get raw data conversion from .csv
    data = convert()
    # store into db
    CaseEntry.objects.bulk_create([CaseEntry(**{
        'country': d['country'],
        'numCases': d['cases'],
        'numDeaths': d['deaths'],
        'endemic': d['endemic'],
        'date': d['date']
    }) for d in data], ignore_conflicts=True)
    return HttpResponseRedirect(reverse('index'))

def index(request):
    message = 'Select Filter'
    if request.method == 'GET':
        cases = CaseEntry.objects.all()
        context = {
            'message': message,
            'cases': cases,
            'form': Filter(initial= {'date': max(CaseEntry.objects.values_list('date'))})
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
            'totalC': totalC['numCases__sum'],
            'totalD': totalD['numDeaths__sum'],
            'form': Filter(request.POST)
        }
        return render(request, "app/index.html", context)


def todo(request):
    if request.method == 'GET':
        tasks = Task.objects.all().order_by('completed', 'priority').values()
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
    