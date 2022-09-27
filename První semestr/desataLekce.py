import requests, json

api_key = "f5ffb4015654ae09070369cdd03643c4"
city = input("Jaké město: ")
lang = "cz"
units = "metric"
base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang={lang}&units={units}"

response = requests.get(base_url)
resp = response.json()

if resp["cod"] == 200:
	current_temperature = resp["main"]["temp"]
	current_pressure = resp["main"]["pressure"]
	current_humidity = resp["main"]["humidity"]
	weather_description = resp["weather"][0]["description"]
	location = resp["name"]
	print(" Teplota (C) = " +
					str(current_temperature) +
		"\n tlak (hPa) = " +
					str(current_pressure) +
		"\n vlhkost (procenta) = " +
					str(current_humidity) +
		"\n popis = " +
					str(weather_description) +
		"\n lokace = " +
					str(location))

else:
	print("Error: " + str(resp["cod"]));

