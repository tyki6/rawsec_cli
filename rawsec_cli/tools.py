import requests


def loadInventoryJson():
    r = requests.get("https://inventory.raw.pm/api/api.json")
    # TODO error when call failed
    return r.json()


# Items
def getToolsJson(json):
    return json["tools"]


def getRessourcesJson(json):
    return json["resources"]


def getCTFJson(json):
    return json["ctf_platforms"]


def getOperatingJson(json):
    return json["operating_systems"]


# Categroy For each Items
def getToolsCategory(json):
    return getToolsJson(json).keys()


def getRessourcesCategory(json):
    return getRessourcesJson(json).keys()


def getCTFCategory(json):
    return getCTFJson(json).keys()


def getOperatingCategory(json):
    return getOperatingJson(json).keys()


# List for each Items
def getToolsByCategory(json, category):
    return getToolsJson(json)[category]["tools"]


def getRessourcesByCategory(json, category):
    return getRessourcesJson(json)[category]["resources"]


def getCTFByCategory(json, category):
    return getCTFJson(json)[category]["ctf_platforms"]


def getOperatingByCategory(json, category):
    return getOperatingJson(json)[category]["operating_systems"]
