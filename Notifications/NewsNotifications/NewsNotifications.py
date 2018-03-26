from bs4 import BeautifulSoup
import requests
import json

APIKey = "706f6fdcadc34c25bf93687ed509ac42"

country = raw_input("Enter Country: ")

url="https://newsapi.org/docs/endpoints/top-headlines"
response = requests.get(url)

soup = BeautifulSoup(response.content,'html.parser')

paragraphs = soup.find_all('p',class_='table-group-item-description').select('code')



