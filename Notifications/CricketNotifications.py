import bs4
import requests
import json

APIKey = "uwqAB34u0hXVWFb693NFrHpERUz1"



try:
	url = "https://cricapi.com/api/cricket?apikey="+APIKey
	dataJSON = requests.get(url)
	data = dataJSON.json()
except:
	print "Try again"