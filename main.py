import datetime as dt
import requests

def open_file():
    return open("api.txt","r").read()

def city():
    return input("Enter the City to know the temperature: ")


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = city()
API_KEY = open_file()

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()
assert response['cod'] == 200
print(response)