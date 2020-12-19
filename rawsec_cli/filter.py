"""Filter file"""
from typing import Dict
from typing import List


def filter_projects(
    projects: List,
    lang=None,
    paid=False,
    free=False,
    online=False,
    offline=False,
    blackarch=False,
) -> List[Dict]:
    """
    Filter method.
    Parameters
    ----------
    projects: List
        project List.
    lang: str, optional
        Language name.
    paid: bool, optional
        paid or not.
    free: bool, optional
        free or not.
    online: bool, optional
        online or not.
    offline: bool, optional
        offline or not.
    blackarch: bool, optional
        present on blackarch.

    Returns
    -------
    List[Dict]
        project filter
    """
    if lang is not None and lang != "":
        projects = [
            project
            for project in projects
            if "language" in project
            and not lang.lower() != project["language"].lower()
        ]

    if paid:
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
