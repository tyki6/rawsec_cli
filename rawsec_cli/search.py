"""Search rawsec project file"""
from typing import Dict
from typing import List

from rawsec_cli.tools import get_all_ctf
from rawsec_cli.tools import get_all_operating
from rawsec_cli.tools import get_all_resources
from rawsec_cli.tools import get_all_tools


def search_project_tools(json: Dict, project: str) -> List[Dict]:
    """
    Search project in tool's category.

    Parameters
    ----------
    json: Dict
        rawsec projects json.
    project: str
        project name or description.

    Returns
    -------
    List[Dict]
        list of rawsec projects.
    """
    list_projects = list()
    for tool in get_all_tools(json):
        if ("name" in tool and project.lower() in tool["name"].lower()) or (
            "description" in tool
            and project.lower() in tool["description"].lower()
        ):
            list_projects.append(tool)
    return list_projects


def search_project_resources(json: Dict, project: str) -> List[Dict]:
    """
    Search project in resources's category.

    Parameters
    ----------
    json: Dict
        rawsec projects json.
    project: str
        project name or description.

    Returns
    -------
    List[Dict]
        list of rawsec projects.
    """
    list_projects = list()
    for resource in get_all_resources(json):
        if (
            "name" in resource and project.lower() in resource["name"].lower()
        ) or (
            "description" in resource
            and project.lower() in resource["description"].lower()
        ):
            list_projects.append(resource)
    return list_projects


def search_project_ctf(json: Dict, project: str) -> List[Dict]:
    """
    Search project in ctf's category.

    Parameters
    ----------
    json: Dict
        rawsec projects json.
    project: str
        project name or description.

    Returns
    -------
    List[Dict]
        list of rawsec projects.
    """
    list_projects = list()
    for ctf in get_all_ctf(json):
        if ("name" in ctf and project.lower() in ctf["name"].lower()) or (
            "description" in ctf
            and project.lower() in ctf["description"].lower()
        ):
            list_projects.append(ctf)
    return list_projects


def search_project_operating(json: Dict, project: str) -> List[Dict]:
    """
    Search project in os's category.

    Parameters
    ----------
    json: Dict
        rawsec projects json.
    project: str
        project name or description.

    Returns
    -------
    List[Dict]
        list of rawsec projects.
    """
    list_projects = list()
    for operating in get_all_operating(json):
        if (
            "name" in operating
            and project.lower() in operating["name"].lower()
        ):
            list_projects.append(operating)
    return list_projects


def search_project(json: Dict, project: str) -> List[Dict]:
    """
    Search project in all category.

    Parameters
    ----------
    json: Dict
        rawsec projects json.
    project: str
        project name or description.

    Returns
    -------
    List[Dict]
        list of rawsec projects.
    """
    return (
        search_project_tools(json, project)
        + search_project_ctf(json, project)
        + search_project_resources(json, project)
        + search_project_operating(json, project)
    )
