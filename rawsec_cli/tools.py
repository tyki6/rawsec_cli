"""Utils tools for rawsec project"""
import requests


def loadInventoryJson():
    """
    Get inventory json
    :return: rawsec dict
    :rtype: dict
    """
    r = requests.get("https://inventory.raw.pm/api/api.json")
    if r.status_code != 200 or "tools" not in r.json():
        return {}
    return r.json()


# Items
def getToolsJson(json):
    """
    Get tools in rawsec json
    :param dict json: rawsec json
    :return: tools dict
    :rtype: dict
    """
    return json["tools"] if "tools" in json else {}


def getResourcesJson(json):
    """
    Get resources in rawsec json
    :param dict json: rawsec json
    :return: resources dict
    :rtype: dict
    """
    return json["resources"] if "resources" in json else {}


def getCTFJson(json):
    """
    Get ctf_platforms in rawsec json
    :param dict json: rawsec json
    :return: ctf_platforms dict
    :rtype: dict
    """
    return json["ctf_platforms"] if "ctf_platforms" in json else {}


def getOperatingJson(json):
    """
    Get operating_systems in rawsec json
    :param dict json: rawsec json
    :return: operating_systems dict
    :rtype: dict
    """
    return json["operating_systems"] if "operating_systems" in json else {}


# Categroy For each Items
def getToolsCategory(json):
    """
    Get tool category present on rawsec
    :param dict json: rawsec json
    :return: tool category list
    :rtype: list
    """
    return list(getToolsJson(json).keys())


def getResourcesCategory(json):
    """
    Get tool category present on rawsec
    :param dict json: rawsec json
    :return: tool category list
    :rtype: list
    """
    return list(getResourcesJson(json).keys())


def getCTFCategory(json):
    """
    Get ctf category present on rawsec
    :param dict json: rawsec json
    :return: ctf category list
    :rtype: list
    """
    return list(getCTFJson(json).keys())


def getOperatingCategory(json):
    """
    Get os category present on rawsec
    :param dict json: rawsec json
    :return: os category list
    :rtype: list
    """
    return list(getOperatingJson(json).keys())


# List for each Items
def getToolsByCategory(json, category):
    """
    Get tools by category in rawsec json
    :param dict json: rawsec json
    :param str category: category
    :return: tools by category list, [] is category is not available.
    :rtype: list
    """
    tools = getToolsJson(json)
    return (
        tools[category]["tools"]
        if category in tools and "tools" in tools[category]
        else []
    )


def getResourcesByCategory(json, category):
    """
    Get resources by category in rawsec json
    :param dict json: rawsec json
    :param str category: category
    :return: resources by category list, [] is category is not available.
    :rtype: list
    """
    resources = getResourcesJson(json)
    return (
        resources[category]["resources"]
        if category in resources and "resources" in resources[category]
        else []
    )


def getCTFByCategory(json, category):
    """
    Get ctf_platforms by category in rawsec json
    :param dict json: rawsec json
    :param str category: category
    :return: ctf_platforms by category list, [] is category is not available.
    :rtype: list
    """
    ctf = getCTFJson(json)
    return (
        ctf[category]["ctf_platforms"]
        if category in ctf and "ctf_platforms" in ctf[category]
        else []
    )


def getOperatingByCategory(json, category):
    """
    Get operating_systems by category in rawsec json
    :param dict json: rawsec json
    :param str category: category
    :return: operating_systems by category list, [] is category is not available.
    :rtype: list
    """
    os = getOperatingJson(json)
    return (
        os[category]["operating_systems"]
        if category in os and "operating_systems" in os[category]
        else []
    )


def getAllTools(json):
    """
    Get all tools in rawsec json
    :param dict json: rawsec json
    :return: tools list
    :rtype: list
    """
    listProjects = list()
    for categoryTools in getToolsCategory(json):
        for tool in getToolsByCategory(json, categoryTools):
            listProjects.append(tool)
    return listProjects


def getAllResources(json):
    """
    Get all resources in rawsec json
    :param dict json: rawsec json
    :return: resources list
    :rtype: list
    """
    listProjects = list()
    for categoryResources in getResourcesCategory(json):
        for tool in getResourcesByCategory(json, categoryResources):
            listProjects.append(tool)
    return listProjects


def getAllCTF(json):
    """
    Get all ctf in rawsec json
    :param dict json: rawsec json
    :return: ctf list
    :rtype: list
    """
    listProjects = list()
    for categoryCTF in getCTFCategory(json):
        for tool in getCTFByCategory(json, categoryCTF):
            listProjects.append(tool)
    return listProjects


def getAllOperating(json):
    """
    Get all os in rawsec json
    :param dict json: rawsec json
    :return: os list
    :rtype: list
    """
    listProjects = list()
    for categoryOperating in getOperatingCategory(json):
        if categoryOperating == "project_transferred":
            continue
        for tool in getOperatingByCategory(json, categoryOperating):
            listProjects.append(tool)
    return listProjects
