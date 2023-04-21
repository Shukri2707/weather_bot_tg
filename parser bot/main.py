from telebot import *
from geopy.geocoders import Nominatim
from parcer import *

TOKEN = "6014257404:AAEZFBwDTgcGH79tzPywBWySqziqNLcolCA"

geolocator = Nominatim(user_agent="GetLoc")


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])

def start(message):
	bot.send_message(message.chat.id, "Здравствуйте, нажмите 'Отправить геолокацию', чтобы мы определили ваше местоположение", reply_markup = geo_markup())
def geo_markup():
	#geobutton = types.KeyboardButton("Отправить геолокацию", request_location=True)
	typecity = types.KeyboardButton("Написать название города")
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add(typecity)
	return markup

@bot.message_handler(content_types=['text'])
def reply_city(message):
	if message.text == "Написать название города":
		bot.send_message(message.chat.id, "Напишите название своего города")

#@bot.message_handler(content_types=['text'])
def city(message):
	URL = "https://sinoptik.ua/погода-" + message.text.lower()
	print(URL)
	pr_date = date(URL)
	bot.send_message(message.chat.id, "Погода в Сиферополе на " + pr_date[0] + " " + pr_date[1] + ":" + "\n"+ pr_date[2] + "\n" + '\n'.join(map(str, weather_detailed(URL))))



@bot.message_handler(content_types=['location'])
def aaaaa(message):
	#location = geolocator.reverse('{} {}'.format(message.location.latitude, message.location.longitude))
	#address = location.raw['address']
	#print(address.get('county', ''))
	#print(message.location)
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("Краткий прогноз")
	btn2 = types.KeyboardButton("Подробный прогноз")
	
	bot.send_message(message.chat.id, "Выберите тип прогноза", reply_markup=markup)
	markup.add(btn1, btn2)
	pr_date = date(URL)
	if message.text == 'Подробный прогноз':
		
		bot.send_message(message.chat.id, "Погода в Сиферополе на " + pr_date[0] + " " + pr_date[1] + ":" + "\n"+ pr_date[2] + "\n" + '\n'.join(map(str, weather_detailed(URL))))
	elif message.text == 'Краткий прогноз':
		bot.send_message(message.chat.id, "Погода в Сиферополе на " + pr_date[0] + " " + pr_date[1] + ":" + "\n"+ pr_date[2] + "\n" + '\n'.join(map(str, weather_short(URL))))
	

bot.polling()