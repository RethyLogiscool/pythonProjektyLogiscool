
import requests

base_url = f"https://v2.jokeapi.dev/joke/Any"
response = requests.get(base_url)
resp = response.json()

if(resp["type"] == "single"):
    print(resp["joke"])
if(resp["type"] == "twopart"):
    print(resp["setup"])
    print("...")
    print(resp["delivery"])