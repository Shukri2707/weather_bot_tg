import requests
from bs4 import BeautifulSoup as bs

URL = "https://sinoptik.ua/погода-симферополь"

def city(url):
	pass

def change_URL(city):
	global URL
	URL = 'https://sinoptik.ua/погода-'+city.lower()

def weather_detailed_day(url):
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

def weather_short_1day(url):
	r = requests.get(url)
	soup = bs(r.text, 'html.parser')
	mintemp = soup.select(".loaded > .temperature > .min")[0].text
	maxtemp = soup.select(".loaded > .temperature > .max")[0].text
	return mintemp, maxtemp

def date(url):
	r = requests.get(url)
	soup = bs(r.text, 'html.parser')
	day = soup.select(".loaded > .date")[0].text
	month = soup.select(".loaded > .month")[0].text
	title = soup.select(".loaded > .weatherIco")[0]['title']
	return day, month, title

def weather_week(url):
	r = requests.get(url)
	soup = bs(r.text, 'html.parser')
	days = []
	month = []
	day_week = []
	mintemp = []
	maxtemp = []
	desription = []
	for i in range(0,7):
		days.append(soup.select(".main > .date")[i].text)
		month.append(soup.select(".main > .month")[i].text)
		if i == 0:
			day_week.append(soup.select(".main > .day-link")[i].text)
		else:
			day_week.append(soup.select(".main > p > .day-link")[i-1].text)
		mintemp.append(soup.select(".main > .temperature > .min")[i].text)
		maxtemp.append(soup.select(".main > .temperature > .max")[i].text)
		desription.append(soup.select(".main > .weatherIco")[i]['title'])
	weather_list = []
	for i in range(0, 7):
		weather_list.append(days[i] + " " + month[i] + " "  + day_week[i] + " --- " + desription[i] + " --- " + mintemp[i] + " " + maxtemp[i] )
		

	return weather_list
