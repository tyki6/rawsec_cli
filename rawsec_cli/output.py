"""Output file"""
import csv
import json
import os
import sys
import webbrowser
from typing import List

import click
from columnar import columnar


def print_output(projects: List, output="list", file=None, wanted_keys=None):
    """
    Generate Output.

    Parameters
    ----------
    projects: List[Dict]
        project list.
    output: str
        output format.
    file: str or None
        file name, file extension will erased output variable.
    wanted_keys: List, optional
        only keys you want.

    Returns
    ----------
    None
        output
    """
    if wanted_keys is None:
        wanted_keys = []
    if file is not None:
        output = os.path.splitext(file)[1][1:]
    if output == "json":
        json_output(projects=projects, file=file)
    elif output == "csv":
        csv_output(projects=projects, file=file, wanted_keys=wanted_keys)
    elif output == "table":
        table_output(projects=projects, file=file, wanted_keys=wanted_keys)
    else:
        list_output(projects=projects, file=file)


def json_output(projects: list, file=None):
    """
    Generate json output format.

    Parameters
    ----------
    projects: List[Dict]
        project list.
    file: str, optional
        file name.
    """
    if file is not None:
        with open(file, "w") as f:
            json.dump({"projects": projects, "total": len(projects)}, f)
    else:
        click.echo(json.dumps({"projects": projects, "total": len(projects)}))


def csv_output(projects: list, wanted_keys: list, file=None):
    """
    Generate csv output format.

    Parameters
    ----------
    projects: List[Dict]
        projects list.
    wanted_keys: List[str]
        only keys you want.
    file: str, optional
        file name.
    """
    if file is not None:
        fileobj = open(file, "w")
    else:
        fileobj = sys.stdout
    file_writer = csv.writer(fileobj, quoting=csv.QUOTE_ALL)
    file_writer.writerow(wanted_keys)
    for project in projects:
        file_writer.writerow(project.values())


def table_output(projects: list, wanted_keys: list, file=None):
    """
    Generate txt output format, use columnar for generate table.
    Parameters
    ----------
    projects: List[Dict]
        projects list.
    wanted_keys: List[str]
        only keys you want.
    file: str, optional
        file name.
    """
    table_projects = list()
    for project in projects:
        line = list()
        for header in wanted_keys:
            if header not in project.keys():
                line.append("")
            else:
                line.append(project[header])
        table_projects.append(line)
    if sys.version_info[1] > 6:
        patterns = [
            ("https://.+", lambda text: text + " "),
            ("http://.+", lambda text: text + " "),
        ]
    else:
        patterns = []

    if len(projects) == 0:
        click.echo("Project not found!")
    else:
        table = columnar(
            table_projects,
            headers=wanted_keys,
            justify="c",
            patterns=patterns,
        )
        if file is not None:
            with open(file, "w") as f:
                f.write(table)
        else:
            if len(projects) == 1:
                if "website" in projects[0]:
                    webbrowser.open_new_tab(projects[0]["website"])
                elif "source" in projects[0]:
                    webbrowser.open_new_tab(projects[0]["source"])
            click.echo(table)
            click.echo("Total projects found: " + str(len(projects)))


def list_output(projects: list, file=None):
    """
    Generate txt list output format.

    Parameters
    ----------
    projects: List[Dict]
        projects list.
    file: str, optional
        file name.
    """
    str_output = ""
    for project in projects:
        str_name = project.get("name", "Unknown Name") + "\n"
        str_output += (
            click.style(str_name, fg="red") if file is None else str_name
        )
        str_description = (
            "    " + project.get("description", "No Description") + "\n"
        )
        str_output += (
            click.style(str_description, fg="blue")
            if file is None
            else str_description
        )
        keywords = ""
        for key in project.keys():
            if key == "name" or key == "description":
                continue
            elif (key == "source" or key == "website") and project[key] != "":
                str_output += "    " + project[key] + "\n"
            elif project[key] != "":
                keywords += f"[{key}: {project[key]}] "
        str_output += (
            click.style("    " + keywords + "\n", fg="white")
            if file is None
            else "    " + keywords + "\n"
        )
        str_output += "\n"

    if len(projects) == 0:
        click.echo("Project not found!")
    else:
        if file is not None:
            with open(file, "w") as f:
                f.write(str_output)
        else:
            if len(projects) == 1:
                if "website" in projects[0]:
                    webbrowser.open_new_tab(projects[0]["website"])
                elif "source" in projects[0]:
                    webbrowser.open_new_tab(projects[0]["source"])
            click.echo(str_output)
            click.echo("Total projects found: " + str(len(projects)))
