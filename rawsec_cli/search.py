from rawsec_cli.tools import getAllTools, getAllResources, getAllCTF, getAllOperating


def searchProjectTools(json, project):
    listProjects = list()
    for tool in getAllTools(json):
        if ("name" in tool and project in tool["name"]) or ("description" in tool and project in tool["description"]):
            listProjects.append(tool)
    return listProjects


def searchProjectResources(json, project):
    listProjects = list()
    for resource in getAllResources(json):
        if ("name" in resource and project in resource["name"]) or ("description" in resource and project in resource["description"]):
            listProjects.append(resource)
    return listProjects


def searchProjectCTF(json, project):
    listProjects = list()
    for ctf in getAllCTF(json):
        if ("name" in ctf and project in ctf["name"]) or ("description" in ctf and project in ctf["description"]):
            listProjects.append(ctf)
    return listProjects


def searchProjectOperating(json, project):
    listProjects = list()
    for operating in getAllOperating(json):
        if "os" in operating and project in operating["os"]:
            listProjects.append(operating)
    return listProjects


def searchProject(json, project):
    return (
        searchProjectTools(json, project)
        + searchProjectCTF(json, project)
        + searchProjectResources(json, project)
    )
