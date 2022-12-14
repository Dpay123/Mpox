from email.policy import default
from django import forms
from django.forms import ModelForm

from .models import *

class LogEntryForm(ModelForm):
    class Meta:
        model = LogEntry
        exclude = []

class TaskEntryForm(ModelForm):
    class Meta:
        model = Task
        exclude = ['completed', 'compDate', 'date']

class Filter(forms.Form):

    CHOICES = [
        ('', '--------'),
        ('numCases', 'Cases (min)'), 
        ('-numCases', 'Cases (max)'), 
        ('numDeaths', 'Deaths (min)'), 
        ('-numDeaths', 'Deaths (max)')
    ]

    date = forms.ModelChoiceField(queryset=CaseEntry.objects.values_list('date', flat=True).distinct(), required=True, label='Date:')
    country = forms.ModelChoiceField(queryset=CaseEntry.objects.values_list('country', flat=True).distinct(), required=False, label='Country:')
    reportBy = forms.ChoiceField(choices=CHOICES, required=False, label='Report By')