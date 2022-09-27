import requests

_config = {
    "response" : "",
    "base_url" : "",
    "params" : {

    }
}

def getConfig():
    return _config

def setBaseUrl(url):
    _config["base_url"] = url

def getBaseUrl():
    return _config["base_url"]

def setParam(name,value):
    _config["params"][name] = value

def getParam(name):
    return _config["params"][name]

def getAllParam():
    return _config["params"]

def getQuery():
    return _config["query"]

def getCleanResponse():
    return _config["response"]

def createQuery(base_url,params):
    query = f"{base_url}?"
    for key, value in params.items():
        query += f"{key}={value}&"
    query = query[:-1]
    _config["query"] = query
    return query

def connectApi(url):
    resp = requests.get(url)
    _config["response"] = resp
    _config["json_response"] = resp.json()
    return resp

def getJson(response=None):
    if(not response):
        response = _config["response"]
    return response.json()