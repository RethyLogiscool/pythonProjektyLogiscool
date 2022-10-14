import requests
api_key = "d2a8a06f38ad6f4d84485d7f983f873f"
symbols = "USD,CZK,AUD,GBP"
url = f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}&base=EUR&symbols={symbols}"
response = requests.get(url)

resp = response.json()

currency = []


currency = resp["rates"]
symbols = symbols.split(",")

for i in range(len(resp["rates"])):
    currency[i] = currency[symbols[i]]/1
    print(f"{symbols[i]} | we buy {round(currency[i] - currency[i]*0.1,2)} | we sell {round(currency[i] + currency[i]*0.1,2)} ")

