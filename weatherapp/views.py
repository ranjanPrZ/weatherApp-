import requests
from django.shortcuts import render
from .models import City
# Create your views here.

def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
	city ='Madhubani'

	cities = City.objects.all()

	weather_data = []

	for city in cities:

		r = requests.get(url.format(city)).json()
		#print(r.text)

		city_weather = {
			'city': city.name,
			'temprature': r['main']['temp'],
			'description': r['weather'][0]['description'],
			'icon': r['weather'][0]['icon'],
		}

		weather_data.append(city_weather)

		#print(weather_data)

	context = {'weather_data' : weather_data}

	return render(request,'weatherapp/weather.html',context)