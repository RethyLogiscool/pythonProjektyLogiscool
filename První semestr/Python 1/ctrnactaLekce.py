from DiscordBot.apiModule import * 

# https://api.genderize.io/?name=Andrew
# addBaseUrl("https://api.genderize.io/")
# addParam("name","Andrew")

print(connectApi(createQuery("https://api.genderize.io/",{"name":"Andrew"})).json())



