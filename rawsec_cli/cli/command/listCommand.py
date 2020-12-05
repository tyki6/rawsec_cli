import sys

import click
from columnar import columnar
from prettytable import PrettyTable
from tabulate import tabulate
from tools import getAllResources, getAllTools, getToolsByCategory, getToolsCategory


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
    if category not in getToolsCategory(json=ctx.obj["json"]):
        click.echo("Category available:")
        for category in getToolsCategory(json=ctx.obj["json"]):
            click.echo(f"\t{category}")
        sys.exit("Not a good category")
    if category:
        projects = getToolsByCategory(ctx.obj["json"], category)
    else:
        projects = getAllTools(ctx.obj["json"])
    projects = [{k: tool[k] if k in tool else None for k in wanted_keys} for tool in projects]
    projects = [list(project.values()) for project in projects]
    table = columnar(projects, headers=wanted_keys)
    click.echo(table)
    click.echo(len(projects))


@listCommand.command()
def ressources():
    click.echo('resources called')


@listCommand.command()
def ctf():
    click.echo('ctf_platforms')


@listCommand.command()
def os():
    click.echo('operating_systems')
