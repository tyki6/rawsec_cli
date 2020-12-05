import sys

import click
from columnar import columnar
from prettytable import PrettyTable
from tabulate import tabulate
from tools import getAllResources, getAllTools, getToolsByCategory, getToolsCategory, getResourcesByCategory, \
    getResourcesCategory, getCTFCategory, getCTFByCategory, getAllCTF, getOperatingCategory, getOperatingByCategory, \
    getAllOperating


@click.group("list")
def listCommand():
    pass


@click.group()
def submit():
    click.echo("submit")


@listCommand.command("tools")
@click.pass_context
@click.argument("category", required=False)
def tools(ctx, category):
    wanted_keys = ["name", "website", "source", "description", "language", "price", "online", "blackarch"]
    if category and category not in getToolsCategory(json=ctx.obj["json"]):
        click.echo("Category available:")
        for category in getToolsCategory(json=ctx.obj["json"]):
            click.echo(f"\t{category}")
        sys.exit("Not a good category")
    if category:
        projects = getToolsByCategory(ctx.obj["json"], category)
    else:
        projects = getAllTools(ctx.obj["json"])
    projects = [{k: tool[k] if k in tool else "" for k in wanted_keys} for tool in projects]
    projects = [list(project.values()) for project in projects]
    table = columnar(projects, headers=wanted_keys)
    click.echo(table)
    click.echo(len(projects))


@listCommand.command("resources")
@click.pass_context
@click.argument("category", required=False)
def resources(ctx, category):
    wanted_keys = ["name", "website", "source", "description", "price"]
    if category and category not in getResourcesCategory(json=ctx.obj["json"]):
        click.echo("Category available:")
        for category in getResourcesCategory(json=ctx.obj["json"]):
            click.echo(f"\t{category}")
        sys.exit("Not a good category")
    if category:
        projects = getResourcesByCategory(ctx.obj["json"], category)
    else:
        projects = getAllResources(ctx.obj["json"])

    resourcesList = list()
    for resource in projects:
        for link in resource["links"]:
            resource[list(link.keys())[0]] = link[list(link.keys())[0]]
        del resource["links"]

        resourceList = list()
        for keys in wanted_keys:
            if keys not in resource:
                resourceList.append("")
            else:
                resourceList.append(resource[keys])
        resourcesList.append(resourceList)
    table = columnar(resourcesList, headers=wanted_keys)
    click.echo(table)
    click.echo(len(projects))


@listCommand.command()
@click.pass_context
@click.argument("category", required=False)
def ctf(ctx, category):
    wanted_keys = ["name", "website", "source", "description", "language", "price"]
    if category and category not in getCTFCategory(json=ctx.obj["json"]):
        click.echo("Category available:")
        for category in getCTFCategory(json=ctx.obj["json"]):
            click.echo(f"\t{category}")
        sys.exit("Not a good category")
    if category:
        projects = getCTFByCategory(ctx.obj["json"], category)
    else:
        projects = getAllCTF(ctx.obj["json"])

    projects = [{k: tool[k] if k in tool else "" for k in wanted_keys} for tool in projects]
    projects = [list(project.values()) for project in projects]
    table = columnar(projects, headers=wanted_keys)
    click.echo(table)
    click.echo(len(projects))


@listCommand.command()
@click.pass_context
@click.argument("category", required=False)
def os(ctx, category):
    wanted_keys = ["os", "base", "description", "link"]
    if category and category not in getOperatingCategory(json=ctx.obj["json"]):
        click.echo("Category available:")
        for category in getOperatingCategory(json=ctx.obj["json"]):
            click.echo(f"\t{category}")
        sys.exit("Not a good category")
    if category:
        projects = getOperatingByCategory(ctx.obj["json"], category)
    else:
        projects = getAllOperating(ctx.obj["json"])
    projects = [{k: tool[k] if k in tool else "" for k in wanted_keys} for tool in projects]
    projects = [list(project.values()) for project in projects]
    table = columnar(projects, headers=wanted_keys)
    click.echo(table)
    click.echo(len(projects))
