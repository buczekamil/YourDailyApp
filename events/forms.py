from bootstrap_modal_forms.forms import BSModalModelForm
from django.forms import ModelForm, DateInput
from django import forms
from events.models import Event


class EventModelForm(ModelForm):
    class Meta:
        model = Event
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'description': forms.Textarea(attrs={'rows': 10, 'cols': 50}),
        }
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventModelForm, self).__init__(*args, **kwargs)
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)


class BSEventModelForm(BSModalModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time']
        # labels = {
        #     "name": "Task",
        #     "to_date": "Date",
        #     "time": "Time",
        #     "if_done": "Done : ",
        # }
