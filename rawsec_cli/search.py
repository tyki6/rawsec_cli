"""Search rawsec project file"""
from rawsec_cli.tools import getAllCTF
from rawsec_cli.tools import getAllOperating
from rawsec_cli.tools import getAllResources
from rawsec_cli.tools import getAllTools


def searchProjectTools(json, project):
    """
    Search project in tool's category
    :param dict json: rawsec projects json
    :param str project: project name or description
    :return: list of projects
    :rtype: list
    """
    listProjects = list()
    for tool in getAllTools(json):
        if ("name" in tool and project.lower() in tool["name"].lower()) or (
            "description" in tool
            and project.lower() in tool["description"].lower()
        ):
            listProjects.append(tool)
    return listProjects


def searchProjectResources(json, project):
    """
    Search project in resources's category
    :param dict json: rawsec projects json
    :param str project: project name or description
    :return: list of projects
    :rtype: list
    """
    listProjects = list()
    for resource in getAllResources(json):
        if (
            "name" in resource and project.lower() in resource["name"].lower()
        ) or (
            "description" in resource
            and project.lower() in resource["description"].lower()
        ):
            listProjects.append(resource)
    return listProjects


def searchProjectCTF(json, project):
    """
    Search project in ctf's category
    :param dict json: rawsec projects json
    :param str project: project name or description
    :return: list of projects
    :rtype: list
    """
    listProjects = list()
    for ctf in getAllCTF(json):
        if ("name" in ctf and project.lower() in ctf["name"].lower()) or (
            "description" in ctf
            and project.lower() in ctf["description"].lower()
        ):
            listProjects.append(ctf)
    return listProjects


def searchProjectOperating(json, project):
    """
    Search project in os's category
    :param dict json: rawsec projects json
    :param str project: project name or description
    :return: list of projects
    :rtype: list
    """
    listProjects = list()
    for operating in getAllOperating(json):
        if "os" in operating and project.lower() in operating["os"].lower():
            listProjects.append(operating)
    return listProjects


def searchProject(json, project):
    """
    Search project in all category
    :param dict json: rawsec projects json
    :param str project: project name or description
    :return: list of projects
    :rtype: list
    """
    return (
        searchProjectTools(json, project)
        + searchProjectCTF(json, project)
        + searchProjectResources(json, project)
    )
