from datetime import datetime

from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms
from .models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'

class ToDoForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = "name", "to_date", "time"
        widgets = {'to_date': DateInput(),
                   'time': TimeInput(),
                   'name': forms.Textarea(attrs={'rows': 1, 'cols': 50})}
        labels = {
            "name": "Task",
            "to_date": "Date",
            "time": "Time"
        }


class TaskModelForm(BSModalModelForm):
    class Meta:
        model = Task
        fields = ['name', 'to_date', 'time', 'if_done']
        labels = {
            "name": "Task",
            "to_date": "Date",
            "time": "Time",
            "if_done": "Done : "
        }
