from tools import getToolsCategory, getToolsByCategory, getRessourcesCategory, getRessourcesByCategory, getCTFCategory, \
    getCTFByCategory, getOperatingCategory, getOperatingByCategory


def searchProjectTools(json, project):
    listProjects = list()
    for categoryTools in getToolsCategory(json):
        for tool in getToolsByCategory(json, categoryTools):
            if project in tool["name"] or project in tool["description"]:
                listProjects.append(tool)
    return listProjects


def searchProjectRessources(json, project):
    listProjects = list()
    for categoryRessources in getRessourcesCategory(json):
        for ressource in getRessourcesByCategory(json, categoryRessources):
            if project in ressource["name"] or project in ressource["description"]:
                listProjects.append(ressource)
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
    return searchProjectTools(json, project) + searchProjectCTF(json, project) + searchProjectRessources(json, project)
