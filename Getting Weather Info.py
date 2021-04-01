import requests
from pprint import pprint


API_Key = '8308cdbbba182b4a7f9e24fe77882d2c'

city = input("Enter your city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
