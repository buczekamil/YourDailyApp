import json

import requests
from django.shortcuts import render
from django.views import View
from geopy import Nominatim

import api
from geo_location.forms import LocationForm


class FindRestaurantView(View):

    def get(self, request):
        form = LocationForm()
        return render(request, 'geo_location.html', {'form': form})

    def post(self, request):
        form = LocationForm(request.POST)
        if form.is_valid():
            street = form.cleaned_data['street']
            city = form.cleaned_data['city']
            country = form.cleaned_data['country']
            locator = Nominatim(user_agent="geo_location")
            location = locator.geocode(f'{street}, {city}, {country}')
            try:
                latitude = location.latitude
                longitude = location.longitude
            except AttributeError:
                text = "Entered address is incorrect - please try again."
                return render(request, 'geo_location.html',
                              {'form': form, 'text': text})
            else:
                url = f"https://developers.zomato.com/api/v2.1/geocode?lat={latitude}&lon={longitude}"
                request_json = requests.get(url, headers={'user-key': api.zomato_api})
                zomato = request_json.json()
                return render(request, 'geo_location.html',
                              {'form': form, 'longitude': longitude, 'latitude': latitude, "zomato": zomato})
