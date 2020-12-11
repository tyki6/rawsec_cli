import requests


def loadInventoryJson():
    r = requests.get("https://inventory.raw.pm/api/api.json")
    if r.status_code != 200 or "tools" not in r.json():
        return {}
    return r.json()


# Items
def getToolsJson(json):
    return json["tools"] if "tools" in json else {}


def getResourcesJson(json):
    return json["resources"] if "resources" in json else {}


def getCTFJson(json):
    return json["ctf_platforms"] if "ctf_platforms" in json else {}


def getOperatingJson(json):
    return json["operating_systems"] if "operating_systems" in json else {}


# Categroy For each Items
def getToolsCategory(json):
    return list(getToolsJson(json).keys())


def getResourcesCategory(json):
    return list(getResourcesJson(json).keys())


def getCTFCategory(json):
    return list(getCTFJson(json).keys())


def getOperatingCategory(json):
    return list(getOperatingJson(json).keys())


# List for each Items
def getToolsByCategory(json, category):
    tools = getToolsJson(json)
    return (
        tools[category]["tools"]
        if category in tools and "tools" in tools[category]
        else []
    )


def getResourcesByCategory(json, category):
    resources = getResourcesJson(json)
    return (
        resources[category]["resources"]
        if category in resources and "resources" in resources[category]
        else []
    )


def getCTFByCategory(json, category):
    ctf = getCTFJson(json)
    return (
        ctf[category]["ctf_platforms"]
        if category in ctf and "ctf_platforms" in ctf[category]
        else []
    )


def getOperatingByCategory(json, category):
    os = getOperatingJson(json)
    return (
        os[category]["operating_systems"]
        if category in os and "operating_systems" in os[category]
        else []
    )


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
