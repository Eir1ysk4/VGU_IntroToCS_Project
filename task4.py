from dotenv import load_dotenv
load_dotenv()
import os
import datetime as dt
import requests
BASE_URL = os.getenv("BASE_URL")
API_KEY =  os.getenv('API_KEY')
CITY = "London"
class Task4:
    collect_data = None

    def __init__(self):
        print("Init task 4")
    
        url =  BASE_URL + "appid=" + API_KEY+ "&q= " + CITY
        
        response = requests.get(url).json()

        
        self.temp_kelvin = response['main']['temp']
        self.temp_celsius, self.temp_fahrenheit = self.kelvin_to_celsius_fahrenheit(self.temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        self.feels_like_celsius, self.feels_like_fahrenheit = self.kelvin_to_celsius_fahrenheit(feels_like_kelvin)
        self.wind_speed = response['wind']['speed']
        self.humidity = response ['main']['humidity']
        self.description = response['weather'][0]['description']
        self.sunrise_time =dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
        self.sunset_time =dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
        self.lon = response['coord']['lon']
        self.lat = response['coord']['lat']
        return
    def kelvin_to_celsius_fahrenheit(self, kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9 / 5) + 32
        return celsius, fahrenheit
    def Task4_Run(self):
        print("Task 3 is activated!!!!")
        print(f"Temperature in {CITY}: {self.temp_celsius: .2f}°C or {self.temp_fahrenheit:.2f}°F")
        print(f"Temperature in {CITY} feels like: {self.feels_like_celsius: .2f}°C or {self.feels_like_fahrenheit:.2f}°F")
        print(f"Humidity in {CITY}: {self.humidity}%")
        print(f"Wind Speed in {CITY}: {self.wind_speed} m/s")
        print(f"General weather in {CITY}: {self.description}")
        print(f"Sun rises in {CITY} at {self.sunrise_time} local time.")
        print(f"Sun sets in {CITY} at {self.sunset_time} local time.")
        
    