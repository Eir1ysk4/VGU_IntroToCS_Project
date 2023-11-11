from dotenv import load_dotenv
load_dotenv()
import os
import datetime as dt
import requests
from shared_resources import  resources
BASE_URL = os.getenv("BASE_URL")
API_KEY =  os.getenv('API_KEY')
# CITY = " tokyo"
class Task4:
    def __init__(self):
        print("Init task 4")

    def kelvin_to_celsius_fahrenheit(self, kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9 / 5) + 32
        return celsius, fahrenheit
    def Task4_Run(self):
        print("Task 4 is activated!!!!")
        task3_output = resources.shared_data.get('task3_output')
        print(task3_output)

        url = BASE_URL + "appid=" + API_KEY + "&q= " + task3_output

        response = requests.get(url).json()
        temp_kelvin = response['main']['temp']
        temp_celsius, temp_fahrenheit = self.kelvin_to_celsius_fahrenheit(temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        feels_like_celsius, feels_like_fahrenheit = self.kelvin_to_celsius_fahrenheit(feels_like_kelvin)
        wind_speed = response['wind']['speed']
        humidity = response['main']['humidity']
        description = response['weather'][0]['description']
        sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
        sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
        lon = response['coord']['lon']
        lat = response['coord']['lat']

        collect_data = {
            "temp_kelvin": temp_kelvin,
            "temp_celsius": temp_celsius,
            "temp_fahrenheit": temp_fahrenheit,
            "feels_like_celsius": feels_like_celsius,
            "feels_like_fahrenheit": feels_like_fahrenheit,
            "wind_speed": wind_speed,
            "humidity": humidity,
            "description": description,
            "sunrise_time": sunrise_time,
            "sunset_time": sunset_time,
            "lon": lon,
            "lat": lat,
        }

        resources.shared_data['task2_output'] = 'web'

        # Store the weather data in shared resources
        resources.shared_data['task4_output'] = collect_data

        
    