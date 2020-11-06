from django import forms
from .models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class ToDoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "name", "to_date", "time", "add_to_calendar"
        widgets = {'to_date': DateInput(),
                   'time': TimeInput(),
                   'name': forms.Textarea(attrs={'rows': 1, 'cols': 50})}
        labels = {
            "name": "Description",
            "to_date": "Date",
            "time": "Time",
            'add_to_calendar': "Add to your calendar?"
        }


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'to_date', 'time', 'if_done']
        labels = {
            "name": "Name",
            "to_date": "Date",
            "time": "Time",
            "if_done": "Is it done?",
        }


