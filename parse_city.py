import requests
from bs4 import BeautifulSoup as bs

URL = "https://hramy.ru/regions/city_abc.htm"

def parse(url):
	r = requests.get(url)
	soup = bs(r.text, 'html.parser')
	city_list = []
	while True:
		try:
			city_list.append(soup.select("table > tr > td")[0].text)
		except Exception as e:
			print(e)
	return city_list
r = requests.get(URL)
soup = bs(r.text, 'html.parser')
print(soup.select("table > tdbody > tr > th")[0].text)