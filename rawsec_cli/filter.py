def filterProjects(
    projects,
    lang=None,
    price=False,
    free=False,
    online=False,
    offline=False,
    blackarch=False,
):
    if lang is not None and lang != "":
        projects = [
            project
            for project in projects
            if "language" in project and not lang.lower() != project["language"].lower()
        ]

    if price:
        projects = [
            project
            for project in projects
            if "price" in project and project["price"] != "Free"
        ]

    if free:
        projects = [
            project
            for project in projects
            if "price" in project and project["price"] == "Free"
        ]

    if online:
        projects = [
            project
            for project in projects
            if "online" in project and project["online"] != "False"
        ]

    if offline:
        projects = [
            project
            for project in projects
            if "online" in project and project["online"] == "False"
        ]

    if blackarch:
        projects = [
            project
            for project in projects
            if "blackarch" in project and project["blackarch"] != ""
        ]

    return projects
