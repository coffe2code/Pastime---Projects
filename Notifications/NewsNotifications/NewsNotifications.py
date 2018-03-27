import requests
import json
from termcolor import colored
from CountryFetcher import return_hashtable

APIKey = "706f6fdcadc34c25bf93687ed509ac42"

print("Fetching Country List.......")
country_hashed = return_hashtable()

while True:
	required_country = raw_input("Which country's news do you want to see?(Add name as in list above): ")

	country_code = country_hashed[required_country]
	url = "https://newsapi.org/v2/top-headlines?country="+country_code+"&apiKey="+APIKey
	

	response = requests.get(url)
	content = response.json()

	for article in content["articles"]:
		print colored(article["title"],'red')
		print colored(article["description"],'green')
		print "\n"
