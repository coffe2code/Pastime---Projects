#! /usr/bin/python3
import bs4
import requests
import json

APIKey = "9ef1cdc7628a4f6091b141947172912"
city = input("Enter city name: ")
i = 1
while(i!=0):
	try:
		url="http://api.apixu.com/v1/current.json?key="+APIKey+"&q="+city
		weatherDataJson = requests.get(url)
		weatherData = weatherDataJson.json()
		i=0
	except:
		i+=1

Name = weatherData["location"]["name"]
Region = weatherData["location"]["region"]
Longitude = weatherData["location"]["lon"]
Latitude = weatherData["location"]["lat"]
Temperature = weatherData["current"]["temp_c"]
WindSpeed = weatherData["current"]["wind_kph"]
WindDirection = weatherData["current"]["wind_dir"]
Humidity = weatherData["current"]["humidity"]

print("-------------LOCATION DETAILS--------------")
print("Name: "+Name)
print("Region: "+Region)
print("Longitude: "+str(Longitude))
print("Latitude: "+str(Latitude))

print("-------------WEATHER DETAILS--------------")
print("Temperature: "+str(Temperature)+" C")
print("WindSpeed: "+str(WindSpeed)+" kph")
print("WindDirection: "+WindDirection)
print("Humidity: "+str(Humidity)+"%")

print("------------------------------------------")