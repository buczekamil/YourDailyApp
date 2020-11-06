from django.forms import ModelForm, DateInput
from django import forms
from events.models import Event


class EventModelForm(ModelForm):
    class Meta:
        model = Event
        labels = {'end_time': "Due date"

                  }
        widgets = {
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'description': forms.Textarea(attrs={'rows': 10, 'cols': 50}),
            'title': forms.Textarea(attrs={'rows': 1, 'cols': 56}),

        }
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventModelForm, self).__init__(*args, **kwargs)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
