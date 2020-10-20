from django import forms


class LocationForm(forms.Form):
    street = forms.CharField(required=True)
    city = forms.CharField(initial="Warsaw", required=True)
    country = forms.CharField(initial="Poland", required=True)
