import pyowm
import telebot

owm = pyowm.OWM('5519bab1bd6d300b9a918680a4decd14', language='ru')
bot = telebot.TeleBot("1244607070:AAEqPTsCcMKz32iOcHN8gfp3n9eZKqvf4ZI")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')['temp']
	humidity = w.get_humidity()
	wind = w.get_wind() ['speed'] 
	winddegree = w.get_wind() ['deg'] 


	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "." "\n"  
	answer += "Температура воздуха " + str(temp) + " градусов." "\n" 
	answer += "Влажность воздуха составляет " + str(humidity) + " %." "\n" 
	answer += "Скорость ветра " + str(wind) + " метров в секунду." "\n" 


	if winddegree > 0:
		answer += "Ветер Северо-Восточный." "\n" 
	elif winddegree > 90: 
		answer += "Ветер Юго-Восточный." "\n" 
	elif winddegree > 180: 
		answer += "Юго-Западный." "\n" 
	elif winddegree > 270: 
		answer += "Северо-Западный." "\n" 
	elif winddegree == 360: 
		answer += "Владимирский централ - ВЕТЕР Северный." "\n" 
	elif winddegree == 0: 
		answer += "Владимирский централ - ВЕТЕР Северный." "\n" 
	elif winddegree == 90: 
		answer += "Ветер восточный." "\n" 
	elif winddegree == 180: 
		answer += "Ветр южный." "\n" 
	elif winddegree == 270: 
		answer += "Ветр западный." "\n" 

	if temp < 3:
		answer += "Да ну нахер сиди дома БРО там ад!." "\n" 
	elif temp < 15: 
		answer += "Сейчас так себе на улице конечно..." "\n" 
	else:
		answer += "На улице кайф ГО гулять!." "\n" 


	bot.send_message(message.chat.id, answer)



bot.polling( none_stop = True )





















input()