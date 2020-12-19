"""Search rawsec project file"""
from rawsec_cli.tools import get_all_ctf
from rawsec_cli.tools import get_all_operating
from rawsec_cli.tools import get_all_resources
from rawsec_cli.tools import get_all_tools


def search_project_tools(json, project):
    """
    Search project in tool's category
    :param dict json: rawsec projects json
    :param str project: project name or description
    :return: list of projects
    :rtype: list
    """
    list_projects = list()
    for tool in get_all_tools(json):
        if ("name" in tool and project.lower() in tool["name"].lower()) or (
            "description" in tool
            and project.lower() in tool["description"].lower()
        ):
            list_projects.append(tool)
    return list_projects


def search_project_resources(json, project):
    """
    Search project in resources's category
    :param dict json: rawsec projects json
    :param str project: project name or description
    :return: list of projects
    :rtype: list
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


def search_project_ctf(json, project):
    """
    Search project in ctf's category
    :param dict json: rawsec projects json
    :param str project: project name or description
    :return: list of projects
    :rtype: list
    """
    list_projects = list()
    for ctf in get_all_ctf(json):
        if ("name" in ctf and project.lower() in ctf["name"].lower()) or (
            "description" in ctf
            and project.lower() in ctf["description"].lower()
        ):
            list_projects.append(ctf)
    return list_projects


def search_project_operating(json, project):
    """
    Search project in os's category
    :param dict json: rawsec projects json
    :param str project: project name or description
    :return: list of projects
    :rtype: list
    """
    list_projects = list()
    for operating in get_all_operating(json):
        if "os" in operating and project.lower() in operating["os"].lower():
            list_projects.append(operating)
    return list_projects


def search_project(json, project):
    """
    Search project in all category
    :param dict json: rawsec projects json
    :param str project: project name or description
    :return: list of projects
    :rtype: list
    """
    return (
        search_project_tools(json, project)
        + search_project_ctf(json, project)
        + search_project_resources(json, project)
        + search_project_operating(json, project)
    )
