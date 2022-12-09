import requests

name = input("Zadej jméno: ")
base_url = f"https://api.genderize.io/?name={name}"
response = requests.get(base_url);
resp = response.json()

print(resp["gender"])
print(str(int(resp["probability"]*100))+" %");