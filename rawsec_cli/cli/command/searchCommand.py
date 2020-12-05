import webbrowser

import click
from search import searchProject
from tabulate import tabulate
from prettytable import PrettyTable

@click.command()
@click.argument('project')
@click.pass_context
@click.option("--lang", "-l", help="Filter by Language")
@click.option("--price", "-p", is_flag=True, help="Filter by Price=True")
@click.option("--free", "-f", is_flag=True, help="Filter by Price: Free")
@click.option("--online", "-on", is_flag=True, help="Filter by Online: True")
@click.option("--offline", "-off", is_flag=True, help="Filter by Online: False")
@click.option("--blackarch", "-b", is_flag=True, help="Filter by blackarch: present")
def search(ctx, project, lang, price, free, online, offline, blackarch):
    projects = searchProject(ctx.obj["json"], project)
    if lang:
        projects = [project for project in projects if not lang.lower() != project["language"].lower()]

    if price:
        projects = [project for project in projects if "price" in project and project["price"] != "Free"]

    if free:
        projects = [project for project in projects if "price" in project and project["price"] == "Free"]

    if online:
        projects = [project for project in projects if "online" in project and project["online"] != "False"]

    if offline:
        projects = [project for project in projects if "online" in project and project["online"] == "False"]

    if blackarch:
        projects = [project for project in projects if "blackarch" in project and project["blackarch"] != ""]

    if len(projects) == 1:
        if "website" in projects[0]:
            webbrowser.open_new_tab(projects[0]["website"])
        elif "source" in projects[0]:
            webbrowser.open_new_tab(projects[0]["source"])

    click.echo(tabulate(projects, "keys", tablefmt="grid"))
