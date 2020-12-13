"""List command cli file"""
import sys

import click
from columnar import columnar

from rawsec_cli.filter import filterProjects
from rawsec_cli.tools import getAllCTF
from rawsec_cli.tools import getAllOperating
from rawsec_cli.tools import getAllResources
from rawsec_cli.tools import getAllTools
from rawsec_cli.tools import getCTFByCategory
from rawsec_cli.tools import getCTFCategory
from rawsec_cli.tools import getOperatingByCategory
from rawsec_cli.tools import getOperatingCategory
from rawsec_cli.tools import getResourcesByCategory
from rawsec_cli.tools import getResourcesCategory
from rawsec_cli.tools import getToolsByCategory
from rawsec_cli.tools import getToolsCategory


@click.group("list")
def listCommand():
    """
    List projects by category (tools, resources, ctf, os).\n
    full documentation: https://rawsec-cli.readthedocs.io/
    \f
    :return:
    """
    pass


@listCommand.command("tools")
@click.pass_context
@click.argument("category", required=False)
@click.option("--lang", "-l", help="Filter by Language")
@click.option(
    "--paid",
    "-p",
    is_flag=True,
    help="Filter by Price, when price is equal to paid.",
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
    help="Filter by blackarch when package is present on blackarch",
)
def tools(ctx, category, lang, paid, free, online, offline, blackarch):
    """
    List all tools inventoried on rawsec, you can add category.\n
    full documentation: https://rawsec-cli.readthedocs.io/
    \f
    :param ctx: click context
    :param str category: category tools
    :param str lang: filter by lang
    :param bool paid: paid
    :param bool free: free
    :param bool online:
    :param bool offline:
    :param bool blackarch: present or not
    :return:
    """
    wanted_keys = [
        "name",
        "website",
        "source",
        "description",
        "language",
        "paid",
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
        {k: tool[k] if k in tool else "" for k in wanted_keys}
        for tool in projects
    ]
    projects = filterProjects(
        projects,
        lang=lang,
        paid=paid,
        free=free,
        online=online,
        offline=offline,
        blackarch=blackarch,
    )
    projects = [list(project.values()) for project in projects]
    table = columnar(projects, headers=wanted_keys)
    click.echo(table)
    click.echo(len(projects))


# @tools.command("category")
# @click.pass_context
# def category(ctx, category):
#     click.echo("test")


@listCommand.command("resources")
@click.pass_context
@click.argument("category", required=False)
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
def resources(ctx, category, paid, free):
    """
    List all resources inventoried on rawsec, you can add category.\n
    full documentation: https://rawsec-cli.readthedocs.io/
    \f
    :param ctx: context
    :param str category:
    :param bool paid:
    :param bool free:
    :return:
    """
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

    projects = filterProjects(projects, paid=paid, free=free)
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
def ctf(ctx, category, lang, paid, free):
    """
    List all ctf platforms inventoried on rawsec, you can add category.\n
    full documentation: https://rawsec-cli.readthedocs.io/
    \f
    :param ctx: click context
    :param str category:
    :param str lang:
    :param bool paid:
    :param bool free:
    :return:
    """
    wanted_keys = [
        "name",
        "website",
        "source",
        "description",
        "language",
        "price",
    ]
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
        {k: tool[k] if k in tool else "" for k in wanted_keys}
        for tool in projects
    ]
    projects = filterProjects(projects, lang=lang, paid=paid, free=free)
    projects = [list(project.values()) for project in projects]
    table = columnar(projects, headers=wanted_keys)
    click.echo(table)
    click.echo(len(projects))


@listCommand.command()
@click.pass_context
@click.argument("category", required=False)
@click.option("--base", "-b", help="Filter by base")
def os(ctx, category, base):
    """
    List all os inventoried on rawsec, you can add category.\n
    full documentation: https://rawsec-cli.readthedocs.io/
    \f
    :param ctx: click context
    :param str category:
    :param str base:
    :return:
    """
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
    projects = [
        {k: os[k] if k in os else "" for k in wanted_keys} for os in projects
    ]
    if base:
        projects = [
            os for os in projects if os["base"].lower() == base.lower()
        ]
    projects = [list(project.values()) for project in projects]
    table = columnar(projects, headers=wanted_keys)
    click.echo(table)
    click.echo(len(projects))
