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
def getTools(json, category):
    return getToolsJson(json)[category]["tools"]


def getRessources(json, category):
    return getRessourcesJson(json)[category]["resources"]


def getCTF(json, category):
    return getCTFJson(json)[category]["ctf_platforms"]


def getOperating(json, category):
    return getOperatingJson(json)[category]["operating_systems"]

def searchProjectTools(json, project):
    listProjects = list()
    for categoryTools in getToolsCategory(json):
        for tool in getTools(json, categoryTools):
            if project in tool["name"]:
                listProjects.append(tool)
    return listProjects

def searchProjectRessources(json, project):
    listProjects = list()
    for categoryRessources in getRessourcesCategory(json):
        for ressource in getRessources(json, categoryRessources):
            if project in ressource["name"]:
                listProjects.append(ressource)
    return listProjects

def searchProjectCTF(json, project):
    listProjects = list()
    for categoryCTF in getCTFCategory(json):
        for ctf in getCTF(json, categoryCTF):
            if project in ctf["name"]:
                listProjects.append(ctf)
    return listProjects

def searchProjectOperating(json, project):
    listProjects = list()
    for categoryOperating in getOperatingCategory(json):
        for operating in getOperating(json, categoryOperating):
            print(operating)
            if project in operating["os"]:
                listProjects.append(operating)
    return listProjects

def searchProject(json, project):
    return searchProjectTools(json, project) + searchProjectCTF(json, project) + searchProjectRessources(json, project)