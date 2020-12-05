from tools import getToolsCategory, getToolsByCategory, getResourcesCategory, getResourcesByCategory, getCTFCategory, \
    getCTFByCategory, getOperatingCategory, getOperatingByCategory, getAllTools


def searchProjectTools(json, project):
    listProjects = list()
    for tool in getAllTools(json):
        if project in tool["name"] or project in tool["description"]:
            listProjects.append(tool)
    return listProjects


def searchProjectResources(json, project):
    listProjects = list()
    # for tool in getAllTools(json):
    #     if project in resource["name"] or project in resource["description"]:
    #         listProjects.append(resource)
    return listProjects


def searchProjectCTF(json, project):
    listProjects = list()
    for categoryCTF in getCTFCategory(json):
        for ctf in getCTFByCategory(json, categoryCTF):
            if project in ctf["name"] or project in ctf["description"]:
                listProjects.append(ctf)
    return listProjects


def searchProjectOperating(json, project):
    listProjects = list()
    for categoryOperating in getOperatingCategory(json):
        for operating in getOperatingByCategory(json, categoryOperating):
            if project in operating["os"]:
                listProjects.append(operating)
    return listProjects


def searchProject(json, project):
    return searchProjectTools(json, project) + searchProjectCTF(json, project) + searchProjectResources(json, project)
