from rawsec_cli.tools import (
    getAllTools,
    getAllResources,
    getAllCTF,
    getAllOperating,
)


def searchProjectTools(json, project):
    listProjects = list()
    for tool in getAllTools(json):
        if ("name" in tool and project.lower() in tool["name"].lower()) or (
            "description" in tool and project.lower() in tool["description"].lower()
        ):
            listProjects.append(tool)
    return listProjects


def searchProjectResources(json, project):
    listProjects = list()
    for resource in getAllResources(json):
        if ("name" in resource and project.lower() in resource["name"].lower()) or (
            "description" in resource and project.lower() in resource["description"].lower()
        ):
            listProjects.append(resource)
    return listProjects


def searchProjectCTF(json, project):
    listProjects = list()
    for ctf in getAllCTF(json):
        if ("name" in ctf and project.lower() in ctf["name"].lower()) or (
            "description" in ctf and project.lower() in ctf["description"].lower()
        ):
            listProjects.append(ctf)
    return listProjects


def searchProjectOperating(json, project):
    listProjects = list()
    for operating in getAllOperating(json):
        if "os" in operating and project.lower() in operating["os"].lower():
            listProjects.append(operating)
    return listProjects


def searchProject(json, project):
    return (
        searchProjectTools(json, project)
        + searchProjectCTF(json, project)
        + searchProjectResources(json, project)
    )
