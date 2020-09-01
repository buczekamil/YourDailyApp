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
                   'name': forms.Textarea(attrs={'rows': 4, 'cols': 16})}
        labels = {
            "name": "Task",
            "to_date": "Date",
            "time": "Time"
        }
