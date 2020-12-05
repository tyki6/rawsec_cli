import sys

import click
from columnar import columnar
from filter import filterProjects
from tools import (
    getAllResources,
    getAllTools,
    getToolsByCategory,
    getToolsCategory,
    getResourcesByCategory,
    getResourcesCategory,
    getCTFCategory,
    getCTFByCategory,
    getAllCTF,
    getOperatingCategory,
    getOperatingByCategory,
    getAllOperating,
)


@click.group("list")
def listCommand():
    pass


@click.group()
def submit():
    click.echo("submit")


@listCommand.command("tools")
@click.pass_context
@click.argument("category", required=False)
@click.option("--lang", "-l", help="Filter by Language")
@click.option("--price", "-p", is_flag=True, help="Filter by Price=True")
@click.option("--free", "-f", is_flag=True, help="Filter by Price: Free")
@click.option("--online", "-on", is_flag=True, help="Filter by Online: True")
@click.option("--offline", "-off", is_flag=True, help="Filter by Online: False")
@click.option("--blackarch", "-b", is_flag=True, help="Filter by blackarch: present")
def tools(ctx, category, lang, price, free, online, offline, blackarch):
    wanted_keys = [
        "name",
        "website",
        "source",
        "description",
        "language",
        "price",
        "online",
        "blackarch",
    ]
    if category and category not in getToolsCategory(json=ctx.obj["json"]):
        click.echo("Category available:")
        for category in getToolsCategory(json=ctx.obj["json"]):
            click.echo(f"\t{category}")
        sys.exit("Not a good category")
    if category:
        projects = getToolsByCategory(ctx.obj["json"], category)
    else:
        projects = getAllTools(ctx.obj["json"])
    projects = [
        {k: tool[k] if k in tool else "" for k in wanted_keys} for tool in projects
    ]
    projects = filterProjects(
        projects,
        lang=lang,
        price=price,
        free=free,
        online=online,
        offline=offline,
        blackarch=blackarch,
    )
    projects = [list(project.values()) for project in projects]
    table = columnar(projects, headers=wanted_keys)
    click.echo(table)
    click.echo(len(projects))


@listCommand.command("resources")
@click.pass_context
@click.argument("category", required=False)
@click.option("--price", "-p", is_flag=True, help="Filter by Price=True")
@click.option("--free", "-f", is_flag=True, help="Filter by Price: Free")
def resources(ctx, category, price, free):
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

    projects = filterProjects(projects, price=price, free=free)
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
@click.option("--lang", "-l", help="Filter by Language")
@click.option("--price", "-p", is_flag=True, help="Filter by Price=True")
@click.option("--free", "-f", is_flag=True, help="Filter by Price=Free")
def ctf(ctx, category, lang, price, free):
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

    projects = [
        {k: tool[k] if k in tool else "" for k in wanted_keys} for tool in projects
    ]
    projects = filterProjects(projects, lang=lang, price=price, free=free)
    projects = [list(project.values()) for project in projects]
    table = columnar(projects, headers=wanted_keys)
    click.echo(table)
    click.echo(len(projects))


@listCommand.command()
@click.pass_context
@click.argument("category", required=False)
@click.option("--base", "-b", help="Filter by base")
def os(ctx, category, base):
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
    projects = [{k: os[k] if k in os else "" for k in wanted_keys} for os in projects]
    if base:
        projects = [os for os in projects if os["base"].lower() == base.lower()]
    projects = [list(project.values()) for project in projects]
    table = columnar(projects, headers=wanted_keys)
    click.echo(table)
    click.echo(len(projects))
