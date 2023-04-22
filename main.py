from telebot import *
from geopy.geocoders import Nominatim
from parser import *

TOKEN = "6014257404:AAEZFBwDTgcGH79tzPywBWySqziqNLcolCA"

geolocator = Nominatim(user_agent="GetLoc")


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])

def start(message):
	bot.send_message(message.chat.id, "Здравствуйте, нажмите 'Отправить геолокацию', чтобы мы определили ваше местоположение, или", reply_markup = geo_markup())
def geo_markup():
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	geobtn = types.KeyboardButton("Отправить геолокацию", request_location=True)
	typecity_btn = types.KeyboardButton("Написать название города")
	markup_btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add(typecity_btn, geobtn)
	return markup

@bot.message_handler(content_types=['text'])
def reply_city(message):
	if message.text == "Написать название города":
		bot.send_message(message.chat.id, "Напишите название своего города")
		bot.register_next_step_handler(message, city_written);

def city_written(message):
	global URL
	URL = 'https://sinoptik.ua/погода-'+message.text.lower()
	day1_btn = types.InlineKeyboardButton("1 день", callback_data  = "1")
	day3_btn = types.InlineKeyboardButton("3 дня", callback_data  = "3")
	day5_btn = types.InlineKeyboardButton("5 дней", callback_data  = "5")
	day7_btn = types.InlineKeyboardButton("7 дней", callback_data  = "7")
	markup = types.InlineKeyboardMarkup()
	markup.add(day1_btn, day3_btn, day5_btn, day7_btn)
	bot.send_message(message.chat.id, "Погоду на сколько дней вы хотите увидеть?", reply_markup=markup)
	print(message.text)
	#bot.register_next_step_handler(message, hmdays_markup);

@bot.callback_query_handler(func=lambda call:True)
def callback_days(call):
	bot.send_message(call.message.chat.id, '\n'.join(map(str, weather_week(URL)[0:int(call.data)])))


@bot.message_handler(content_types=['location'])
def aaaaa(message):
	location = geolocator.reverse('{} {}'.format(message.location.latitude, message.location.longitude))
	address = location.raw['address']
	print(address.get('county', ''))
	print(message.location)
	"""
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("Краткий прогноз")
	btn2 = types.KeyboardButton("Подробный прогноз")
	
	bot.send_message(message.chat.id, "Выберите тип прогноза", reply_markup=markup)
	markup.add(btn1, btn2)
	pr_date = date(URL)
	if message.text == 'Подробный прогноз':
		
		bot.send_message(message.chat.id, "Погода в Сиферополе на " + pr_date[0] + " " + pr_date[1] + ":" + "\n"+ pr_date[2] + "\n" + '\n'.join(map(str, weather_detailed(URL))))
	elif message.text == 'Краткий прогноз':
		bot.send_message(message.chat.id, "Погода в Сиферополе на " + pr_date[0] + " " + pr_date[1] + ":" + "\n"+ pr_date[2] + "\n" + '\n'.join(map(str, weather_short(URL))))"""
	
bot.polling()