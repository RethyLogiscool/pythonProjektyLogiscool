import requests

api_key = "f5ffb4015654ae09070369cdd03643c4"
city = input("Jaké město: ")
lang = "cz"
units = "metric"
base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang={lang}&units={units}"

response = requests.get(base_url)
resp = response.json()

if(resp["cod"] == 200):
    print(f"Ve mestě {resp['name']} je právě {resp['weather'][0]['description']} s teplotou {resp['main']['temp']}C")
else:
    print(f"Nastal problém. Kód chyby: {resp['cod']}")