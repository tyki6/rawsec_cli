"""Utils tools for rawsec project"""
import requests


def load_inventory_json():
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
def get_tools_json(json):
    """
    Get tools in rawsec json
    :param dict json: rawsec json
    :return: tools dict
    :rtype: dict
    """
    return json["tools"] if "tools" in json else {}


def get_resources_json(json):
    """
    Get resources in rawsec json
    :param dict json: rawsec json
    :return: resources dict
    :rtype: dict
    """
    return json["resources"] if "resources" in json else {}


def get_ctf_json(json):
    """
    Get ctf_platforms in rawsec json
    :param dict json: rawsec json
    :return: ctf_platforms dict
    :rtype: dict
    """
    return json["ctf_platforms"] if "ctf_platforms" in json else {}


def get_operating_json(json):
    """
    Get operating_systems in rawsec json
    :param dict json: rawsec json
    :return: operating_systems dict
    :rtype: dict
    """
    return json["operating_systems"] if "operating_systems" in json else {}


# Categroy For each Items
def get_tools_category(json):
    """
    Get tool category present on rawsec
    :param dict json: rawsec json
    :return: tool category list
    :rtype: list
    """
    return list(get_tools_json(json).keys())


def get_resources_category(json):
    """
    Get tool category present on rawsec
    :param dict json: rawsec json
    :return: tool category list
    :rtype: list
    """
    return list(get_resources_json(json).keys())


def get_ctf_category(json):
    """
    Get ctf category present on rawsec
    :param dict json: rawsec json
    :return: ctf category list
    :rtype: list
    """
    return list(get_ctf_json(json).keys())


def get_operating_category(json):
    """
    Get os category present on rawsec
    :param dict json: rawsec json
    :return: os category list
    :rtype: list
    """
    return list(get_operating_json(json).keys())


# List for each Items
def get_tools_by_category(json, category):
    """
    Get tools by category in rawsec json
    :param dict json: rawsec json
    :param str category: category
    :return: tools by category list, [] is category is not available.
    :rtype: list
    """
    tools = get_tools_json(json)
    return (
        tools[category]["tools"]
        if category in tools and "tools" in tools[category]
        else []
    )


def get_resources_by_category(json, category):
    """
    Get resources by category in rawsec json
    :param dict json: rawsec json
    :param str category: category
    :return: resources by category list, [] is category is not available.
    :rtype: list
    """
    resources = get_resources_json(json)
    return (
        resources[category]["resources"]
        if category in resources and "resources" in resources[category]
        else []
    )


def get_ctf_by_category(json, category):
    """
    Get ctf_platforms by category in rawsec json
    :param dict json: rawsec json
    :param str category: category
    :return: ctf_platforms by category list, [] is category is not available.
    :rtype: list
    """
    ctf = get_ctf_json(json)
    return (
        ctf[category]["ctf_platforms"]
        if category in ctf and "ctf_platforms" in ctf[category]
        else []
    )


def get_operating_by_category(json, category):
    """
    Get operating_systems by category in rawsec json
    :param dict json: rawsec json
    :param str category: category
    :return: operating_systems by category list, [] is category is not available.
    :rtype: list
    """
    os = get_operating_json(json)
    return (
        os[category]["operating_systems"]
        if category in os and "operating_systems" in os[category]
        else []
    )


def get_all_tools(json):
    """
    Get all tools in rawsec json
    :param dict json: rawsec json
    :return: tools list
    :rtype: list
    """
    list_projects = list()
    for category_tools in get_tools_category(json):
        for tool in get_tools_by_category(json, category_tools):
            list_projects.append(tool)
    return list_projects


def get_all_resources(json):
    """
    Get all resources in rawsec json
    :param dict json: rawsec json
    :return: resources list
    :rtype: list
    """
    list_projects = list()
    for category_resources in get_resources_category(json):
        for tool in get_resources_by_category(json, category_resources):
            list_projects.append(tool)
    return list_projects


def get_all_ctf(json):
    """
    Get all ctf in rawsec json
    :param dict json: rawsec json
    :return: ctf list
    :rtype: list
    """
    list_projects = list()
    for category_ctf in get_ctf_category(json):
        for tool in get_ctf_by_category(json, category_ctf):
            list_projects.append(tool)
    return list_projects


def get_all_operating(json):
    """
    Get all os in rawsec json
    :param dict json: rawsec json
    :return: os list
    :rtype: list
    """
    list_projects = list()
    for category_operating in get_operating_category(json):
        if category_operating == "project_transferred":
            continue
        for tool in get_operating_by_category(json, category_operating):
            list_projects.append(tool)
    return list_projects
