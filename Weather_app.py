import requests
from pprint import pprint
API_Key ='efb9cf5d2cf4667283564b3b4705686d'
city = input("Enter a city")

base_url="http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data =requests.get(base_url).json()
pprint(weather_data)