import datetime as dt
import requests
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "8638629b3877d52e8f249b14d702472b"
CITY = "Thanh pho Ho Chi Minh"
class Task3:
    def __init__(self):
        print("Init task 3")
    
        url =  BASE_URL + "appid=" + API_KEY+ "&q= " + CITY
        
        response = requests.get(url).json()

        def kelvin_to_celsius_fahrenheit(kelvin):
            celsius = kelvin - 273.15
            fahrenheit = celsius*(9/5)+32
            return celsius, fahrenheit
        
        self.temp_kelvin = response['main']['temp']
        self.temp_celsius, self.temp_fahrenheit = kelvin_to_celsius_fahrenheit(self.temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        self.feels_like_celsius, self.feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
        self.wind_speed = response['wind']['speed']
        self.humidity = response ['main']['humidity']
        self.description = response['weather'][0]['description']
        self.sunrise_time =dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
        self.sunset_time =dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
        return

    def Task3_Run(self):
        print("Task 3 is activated!!!!")
        print(f"Temperature in {CITY}: {self.temp_celsius: .2f}°C or {self.temp_fahrenheit:.2f}°F")
        print(f"Temperature in {CITY} feels like: {self.feels_like_celsius: .2f}°C or {self.feels_like_fahrenheit:.2f}°F")
        print(f"Humidity in {CITY}: {self.humidity}%")
        print(f"Wind Speed in {CITY}: {self.wind_speed} m/s")
        print(f"General weather in {CITY}: {self.description}")
        print(f"Sun rises in {CITY} at {self.sunrise_time} local time.")
        print(f"Sun sets in {CITY} at {self.sunset_time} local time.")
        
    