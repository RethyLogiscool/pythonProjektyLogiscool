from apiModule2 import *

setBaseUrl("https://api.genderize.io/")
setParam("name","Marek")
createQuery(getBaseUrl(),getAllParam())
connectApi(getQuery())
print(getConfig())