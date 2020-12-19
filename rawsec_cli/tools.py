"""Utils tools for rawsec project"""
from typing import Dict
from typing import List

import requests


def load_inventory_json() -> Dict:
    """
    Get rawsec inventory json.

    Returns
    -------
    Dict
        rawsec dict of project
    """
    r = requests.get("https://inventory.raw.pm/api/api.json")
    if r.status_code != 200 or "tools" not in r.json():
        return {}
    return r.json()


# Items
def get_tools_json(json: Dict) -> Dict:
    """
    Get tools in rawsec json.

    Parameters
    ----------
    json: Dict
        rawsec json.

    Returns
    -------
    Dict
        tools dict.
    """
    return json["tools"] if "tools" in json else {}


def get_resources_json(json: Dict) -> Dict:
    """
    Get resources in rawsec json.

    Parameters
    ----------
    json: Dict
        rawsec json.

    Returns
    -------
    Dict
        resources dict.
    """
    return json["resources"] if "resources" in json else {}


def get_ctf_json(json: Dict) -> Dict:
    """
    Get ctf in rawsec json.

    Parameters
    ----------
    json: Dict
        rawsec json.

    Returns
    -------
    Dict
        ctf dict.
    """
    return json["ctf_platforms"] if "ctf_platforms" in json else {}


def get_operating_json(json: Dict) -> Dict:
    """
    Get operating in rawsec json.

    Parameters
    ----------
    json: Dict
        rawsec json.

    Returns
    -------
    Dict
        operating dict.
    """
    return json["operating_systems"] if "operating_systems" in json else {}


# Category For each Items
def get_tools_category(json: Dict) -> List[str]:
    """
    Get tool category present on rawsec.

    Parameters
    ----------
    json: Dict
        rawsec json.

    Returns
    -------
    List[str]
        tool category list.
    """
    return list(get_tools_json(json).keys())


def get_resources_category(json: Dict) -> List[str]:
    """
    Get resources category present on rawsec.

    Parameters
    ----------
    json: Dict
        rawsec json.

    Returns
    -------
    List[str]
        resources category list.
    """
    return list(get_resources_json(json).keys())


def get_ctf_category(json: Dict) -> List[str]:
    """
    Get ctf category present on rawsec.

    Parameters
    ----------
    json: Dict
        rawsec json.

    Returns
    -------
    List[str]
        ctf category list.
    """
    return list(get_ctf_json(json).keys())


def get_operating_category(json: Dict) -> List[str]:
    """
    Get os category present on rawsec.

    Parameters
    ----------
    json: Dict
        rawsec json.

    Returns
    -------
    List[str]
        os category list.
    """
    return list(get_operating_json(json).keys())


# List for each Items
def get_tools_by_category(json: Dict, category: str) -> List[Dict]:
    """
    Get tools by category in rawsec json.

    Parameters
    ----------
    json: Dict
        rawsec json.
    category: str
        category.

    Returns
    -------
    List[Dict]
        tools by category list, [] if category is not available.
    """
    tools = get_tools_json(json)
    return (
        tools[category]["tools"]
        if category in tools and "tools" in tools[category]
        else []
    )


def get_resources_by_category(json: Dict, category: str) -> List[Dict]:
    """
    Get resources by category in rawsec json.

    Parameters
    ----------
    json: Dict
        rawsec json.
    category: str
        category.

    Returns
    -------
    List[Dict]
        resources by category list, [] if category is not available.
    """
    resources = get_resources_json(json)
    return (
        resources[category]["resources"]
        if category in resources and "resources" in resources[category]
        else []
    )


def get_ctf_by_category(json: Dict, category: str) -> List[Dict]:
    """
    Get ctf_platforms by category in rawsec json.

    Parameters
    ----------
    json: Dict
        rawsec json.
    category: str
        category.

    Returns
    -------
    List[Dict]
        ctf_platforms by category list, [] if category is not available.
    """
    ctf = get_ctf_json(json)
    return (
        ctf[category]["ctf_platforms"]
        if category in ctf and "ctf_platforms" in ctf[category]
        else []
    )


def get_operating_by_category(json: Dict, category: str) -> List[Dict]:
    """
    Get operating_systems by category in rawsec json.

    Parameters
    ----------
    json: Dict
        rawsec json.
    category: str
        category.

    Returns
    -------
    List[Dict]
        operating_systems by category list, [] if category is not available.
    """
    os = get_operating_json(json)
    return (
        os[category]["operating_systems"]
        if category in os and "operating_systems" in os[category]
        else []
    )


def get_all_tools(json: Dict) -> List[Dict]:
    """
    Get all tools in rawsec json.

    Parameters
    ----------
    json: Dict
        rawsec json.

    Returns
    -------
    List[Dict]
        tools list
    """
    list_projects = list()
    for category_tools in get_tools_category(json):
        for tool in get_tools_by_category(json, category_tools):
            list_projects.append(tool)
    return list_projects


def get_all_resources(json: Dict) -> List[Dict]:
    """
    Get all resources in rawsec json.

    Parameters
    ----------
    json: Dict
        rawsec json.

    Returns
    -------
    List[Dict]
        resources list.
    """
    list_projects = list()
    for category_resources in get_resources_category(json):
        for tool in get_resources_by_category(json, category_resources):
            list_projects.append(tool)
    return list_projects


def get_all_ctf(json: Dict) -> List[Dict]:
    """
    Get all ctf in rawsec json.

    Parameters
    ----------
    json: Dict
        rawsec json.

    Returns
    -------
    List[Dict]
        ctf list.

    """
    list_projects = list()
    for category_ctf in get_ctf_category(json):
        for tool in get_ctf_by_category(json, category_ctf):
            list_projects.append(tool)
    return list_projects


def get_all_operating(json: Dict) -> List[Dict]:
    """
    Get all os in rawsec json.

    Parameters
    ----------
    json: Dict
        rawsec json.
    Returns
    -------
    List[Dict]
        os list.

    """
    list_projects = list()
    for category_operating in get_operating_category(json):
        if category_operating == "project_transferred":
            continue
        for tool in get_operating_by_category(json, category_operating):
            list_projects.append(tool)
    return list_projects
