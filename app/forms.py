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
        exclude = []

class Filter(forms.Form):
    date = forms.ModelChoiceField(queryset=CaseEntry.objects.values_list('date', flat=True).distinct(), required=True)
    country = forms.ModelChoiceField(queryset=CaseEntry.objects.values_list('country', flat=True), required=False)