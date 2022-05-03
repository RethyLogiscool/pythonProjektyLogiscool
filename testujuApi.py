import requests,json

apiKey = "726a76576b22351e7b11c12549f00f98"
meny = "GBP, USD, CZK, JPY"

querry = f"http://api.exchangeratesapi.io/v1/latest?access_key={apiKey}&base=EUR&format=1&symbols={meny}"

response = requests.get(querry)
data = response.json()
print(data["rates"])