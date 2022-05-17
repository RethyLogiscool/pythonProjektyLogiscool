import requests, json

_config = {
    "params" : {
    },
    "base_url" : "",
    "response" : "",
    "query" : ""
}

def addBaseUrl(url):
    _config["base_url"] = url
    return 200

def getBaseUrl():
    return _config["base_url"]

def addParam(name,value):
    _config["params"][name] = value
    return 200

def getParam(name,value):
    return _config["params"][name]

def getAllParam():
    return _config["params"]

def getQuery():
    return _config["query"]

def createQuery(base_url,params):
    query = f"{base_url}?"
    for key, value in params.items():
        query += f"{key}={value}&"
    query = query[:-1]
    _config["query"] = query
    return query

def connectApi(query):
    resp = requests.get(query)
    _config["response"] = resp
    return resp

def getJson():
    return _config["response"].json()