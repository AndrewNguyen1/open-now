from django.shortcuts import render

from django.db import models
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from django.views import generic

from .models import Login, Business, Measurement
from .forms import MeasurementModelForm

from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo, get_center_coordinates, get_zoom, get_ip_address
import folium



def login(request):
    return render(request, 'open_now/login.html')


class LoginView(generic.ListView):
    template_name = 'open_now/login.html'

    def get_queryset(self):
        """
        """
        return

class HomeView(generic.ListView):
    template_name = 'open_now/home.html'

    def get_queryset(self):
        """
        """
        return

class BusinessView(generic.ListView):
    template_name = 'open_now/business_list.html'
    context_object_name = 'business_list'

    def get_queryset(self):
        """
        """
        return Business.objects.all()
        return

class BusinessFormView(generic.ListView):
    template_name = 'open_now/business_form.html'

    def get_queryset(self):
        """
        """
        return

def get_business(request):

    business_name = request.POST['business_name']
    description = request.POST['description']
    phone_number = request.POST['phone_number']
    website = request.POST['website']
    business_category = request.POST['business_category']
    t = Business(business_name=business_name,description=description, phone_number = phone_number, website = website,
                 business_category = business_category)
    t.save()
    return HttpResponseRedirect(reverse('open_now:business_list'))

def search_business(request):
    srh = request.GET['query']
    businesses = Business.objects.filter(business_name__icontains=srh, business_category__icontains=srh, description__icontains=srh)
    params={'businesses': businesses, 'search':srh}
    return render(request, 'open_now/search_business.html', params)



def calculate_distance_view(request):
	# initial values
	distance = None
	destination = None

	obj = get_object_or_404(Measurement, id=1)
	form = MeasurementModelForm(request.POST or None)
	geolocator = Nominatim(user_agent='open_now')

	# ip address from local host
	# doesn't work :(
	ip_ = get_ip_address(request)
	# print(ip_)

	# hard coded ip address for charlottesville va
	ip = '128.143.22.119'
	country, city, lat, lon = get_geo(ip)

	location = geolocator.geocode(city)

	# location coordinates
	l_lat = lat
	l_lon = lon
	pointA = (l_lat, l_lon)

	# initial folium map
	m = folium.Map(width=800, height=500, location=get_center_coordinates(l_lat, l_lon), zoom_start=8)

	# location marker
	folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'], icon=folium.Icon(color='purple')).add_to(m)

	if form.is_valid():
		instance = form.save(commit=False)
		destination_ = form.cleaned_data.get('destination')
		destination = geolocator.geocode(destination_)

		# destination coordinates
		d_lat = destination.latitude
		d_lon = destination.longitude

		# print(destination)
		pointB = (d_lat, d_lon)

		# distance calculation
		distance = round(geodesic(pointA, pointB).km, 2)

		# map modification
		m = folium.Map(width=800, height=500, location=get_center_coordinates(l_lat, l_lon, d_lat, d_lon), zoom_start=get_zoom(distance))

		# location marker
		folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'], icon=folium.Icon(color='purple')).add_to(m)

		# destination marker
		# location marker
		folium.Marker([d_lat, d_lon], tooltip='click here for more', popup=city['city'], icon=folium.Icon(color='red', icon='cloud')).add_to(m)

		# draw the lint between the location and destination
		line = folium.PolyLine(locations=[pointA, pointB], weight=2, color='blue')

		# add the line to the map
		m.add_child(line)


		instance.location = location
		instance.distance = distance
		instance.save()

	m = m._repr_html_()
	# distance = None


	context = {
		'distance': distance,
		'destination': destination,
		'form': form,
		'map': m,
	}

	return render(request, 'open_now/main.html', context)