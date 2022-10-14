import requests, json

params = ""
safe = input("Chceš safe mode? (ANO/NE)")
if(safe=="ANO"):
    params = "safe-mode"
else:
    category = input("Chceš si vybrat kategorii vtipů? (ANO/NE")
    if(category == "ANO"):
        category = input("Jakou chceš kategorii? (programming, misc, dark, pun, spooky, christmas")
        params += "&category" + category
base_url = f"https://v2.jokeapi.dev/joke/Any?{params}"
response = requests.get(base_url)
resp = response.json()

if(resp["type"] == "single"):
    print(resp["joke"])
else:
    print(resp["setup"])
    input("zmáčky enter")
    print(resp["delivery"])


