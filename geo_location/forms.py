from django import forms


class LocationForm(forms.Form):
    street = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()

