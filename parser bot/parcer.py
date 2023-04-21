import requests
from bs4 import BeautifulSoup as bs

URL = "https://sinoptik.ua/погода-симферополь"

def weather_detailed(url):
	r = requests.get(url)
	soup = bs(r.text, 'html.parser')
	clock = []
	for i in range(1,9):
		clock.append(soup.select(".time > .p"+str(i))[0].text)
	temperatures = []
	for i in range(1,9):
		temperatures.append(soup.select(".temperature > .p"+str(i))[0].text)

	list_of_wt = []

	for i in range(0,8):
		list_of_wt.append(clock[i] + "      " + temperatures[i] )
	return list_of_wt

def weather_short(url):
	r = requests.get(url)
	soup = bs(r.text, 'html.parser')
	mintemp = soup.select(".loaded > .temperature > .min")[0].text
	maxtemp = soup.select(".loaded > .temperature > .max")[0].text
	return mintemp, maxtemp
print(weather_short(URL))

def date(url):
	r = requests.get(url)
	soup = bs(r.text, 'html.parser')
	day = soup.select(".loaded > .date")[0].text
	month = soup.select(".loaded > .month")[0].text
	title = soup.select(".loaded > .weatherIco")[0]['title']
	return day, month, title
print(date(URL))
