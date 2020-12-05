import requests


def loadInventoryJson():
    r = requests.get("https://inventory.raw.pm/api/api.json")
    # TODO error when call failed
    return r.json()


# Items
def getToolsJson(json):
    return json["tools"]


def getResourcesJson(json):
    return json["resources"]


def getCTFJson(json):
    return json["ctf_platforms"]


def getOperatingJson(json):
    return json["operating_systems"]


# Categroy For each Items
def getToolsCategory(json):
    return getToolsJson(json).keys()


def getResourcesCategory(json):
    return getResourcesJson(json).keys()


def getCTFCategory(json):
    return getCTFJson(json).keys()


def getOperatingCategory(json):
    return getOperatingJson(json).keys()


# List for each Items
def getToolsByCategory(json, category):
    return getToolsJson(json)[category]["tools"]


def getResourcesByCategory(json, category):
    return getResourcesJson(json)[category]["resources"]


def getCTFByCategory(json, category):
    return getCTFJson(json)[category]["ctf_platforms"]


def getOperatingByCategory(json, category):
    return getOperatingJson(json)[category]["operating_systems"]


def getAllTools(json):
    listProjects = list()
    for categoryTools in getToolsCategory(json):
        for tool in getToolsByCategory(json, categoryTools):
            listProjects.append(tool)
    return listProjects


def getAllResources(json):
    listProjects = list()
    for categoryResources in getResourcesCategory(json):
        for tool in getResourcesByCategory(json, categoryResources):
            listProjects.append(tool)
    return listProjects


def getAllCTF(json):
    listProjects = list()
    for categoryCTF in getCTFCategory(json):
        for tool in getCTFByCategory(json, categoryCTF):
            listProjects.append(tool)
    return listProjects


def getAllOperating(json):
    listProjects = list()
    for categoryOperating in getOperatingCategory(json):
        for tool in getOperatingByCategory(json, categoryOperating):
            listProjects.append(tool)
    return listProjects
