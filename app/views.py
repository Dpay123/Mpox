from django.shortcuts import render, redirect
from django.forms import ModelForm

from .models import *

class LogEntryForm(ModelForm):
    class Meta:
        model = LogEntry
        fields = ['version', 'desc']

# Create your views here.
def index(request):
    return render(request, "app/index.html")

def todo(request):
    return render(request, 'app/todo.html')

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
    