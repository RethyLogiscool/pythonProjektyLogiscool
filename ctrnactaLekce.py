from apiModule import * 
import requests

addBaseUrl("https://api.genderize.io/")
addParam("name","Andrew")
print(getBaseUrl())
print(createQuery(getBaseUrl(),getAllParam()))
connectApi(getQuery())
json = getJson()
print("Gender is: " + json["gender"])

