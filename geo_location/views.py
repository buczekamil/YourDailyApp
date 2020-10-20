from django.shortcuts import render
from django.views import View
from geopy import Nominatim
from geo_location.forms import LocationForm


class FindRestaurantView(View):

    def get(self, request):
        if request.method == "GET":
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
            loc = ('Latitude = {}, Longitude = {}'.format(location.latitude, location.longitude))
            return render(request, 'geo_location.html', {'loc': loc})
