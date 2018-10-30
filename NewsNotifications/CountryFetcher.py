from bs4 import BeautifulSoup
import requests

##############The following block fetches the supported country codes###
def return_hashtable():
	url_country_code="https://newsapi.org/docs/endpoints/top-headlines"
	response = requests.get(url_country_code)

	soup = BeautifulSoup(response.content,'html.parser')

	code = soup.select('p code')

	country_codes_guess = []
	for value in code:
		if (len(value.get_text()))==2:
			country_codes_guess.append(value.get_text())


	#########The following block fetchces the country relative to each code###
	hashtable={}
	
	for country_code in country_codes_guess:
		
		try:	
			url_country='https://laendercode.net/en/2-letter-code/'+country_code
			response = requests.get(url_country)

			soup = BeautifulSoup(response.content,'html.parser')
			code=soup.select('div div h3')
			print code[0].get_text()
			hashtable[code[0].get_text()]=country_code

		except:
			continue

	return hashtable


