import requests

from pprint import pprint


def getWeather(cityName):
    API_Key = '8308cdbbba182b4a7f9e24fe77882d2c'
    base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+cityName
    weather_data = requests.get(base_url).json()
    return weather_data


if __name__ == '__main__':
    cityName = input("Enter city name: ")
    weatherData = getWeather(cityName)
    pprint(weatherData['main'])
