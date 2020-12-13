"""Search command cli file"""
import webbrowser

import click
from tabulate import tabulate

from rawsec_cli.filter import filterProjects
from rawsec_cli.search import searchProject


@click.command()
@click.argument("project")
@click.pass_context
@click.option("--lang", "-l", help="Filter by Language")
@click.option(
    "--paid",
    "-p",
    is_flag=True,
    help="Filter by Price, when price is equal to paid",
)
@click.option(
    "--free",
    "-f",
    is_flag=True,
    help="Filter by Price, when price is equal to free",
)
@click.option(
    "--online",
    "-on",
    is_flag=True,
    help="Filter by Online, when online is equal to true",
)
@click.option(
    "--offline",
    "-off",
    is_flag=True,
    help="Filter by Online, when online is equal to false",
)
@click.option(
    "--blackarch",
    "-b",
    is_flag=True,
    help="Filter by Blackarch when package is present on Blackarch",
)
def search(ctx, project, lang, paid, free, online, offline, blackarch):
    """
    Search a project inventoried on rawsec.\n
    Search in name and description.\n
    full documentation: https://rawsec-cli.readthedocs.io/
    \f
    :param ctx: click context
    :param str project: project name or description
    :param str lang: filter by language
    :param bool paid: paid
    :param bool free: free
    :param bool online: online
    :param bool offline: offline
    :param bool blackarch: present or not
    :return:
    """
    projects = searchProject(ctx.obj["json"], project)
    projects = filterProjects(
        projects,
        lang,
        paid,
        free,
        online,
        offline,
        blackarch,
    )

    if len(projects) == 1:
        if "website" in projects[0]:
            webbrowser.open_new_tab(projects[0]["website"])
        elif "source" in projects[0]:
            webbrowser.open_new_tab(projects[0]["source"])

    click.echo(tabulate(projects, "keys", tablefmt="grid"))
