"""List command cli file"""
import sys

import click

from rawsec_cli.filter import filter_projects
from rawsec_cli.output import print_output
from rawsec_cli.tools import get_all_ctf
from rawsec_cli.tools import get_all_operating
from rawsec_cli.tools import get_all_resources
from rawsec_cli.tools import get_all_tools
from rawsec_cli.tools import get_ctf_by_category
from rawsec_cli.tools import get_ctf_category
from rawsec_cli.tools import get_operating_by_category
from rawsec_cli.tools import get_operating_category
from rawsec_cli.tools import get_resources_by_category
from rawsec_cli.tools import get_resources_category
from rawsec_cli.tools import get_tools_by_category
from rawsec_cli.tools import get_tools_category


@click.group("list")
def list_command():
    """
    \b
    List projects by category (tools, resources, ctf, os).
    Full documentation: https://rawsec-cli.readthedocs.io/
    \f
    Returns
    -------
    None
        List of project
    """
    pass


@list_command.command("tools")
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
@click.option(
    "--output",
    "-o",
    help="Output format",
    type=click.Choice(
        ["json", "csv", "table"],
        case_sensitive=False,
    ),
    default="table",
)
@click.option(
    "--output-file",
    "-of",
    help="Output file name if you want. Format: json, csv, table are supported.",
    default=None,
)
def tools(
    ctx,
    category,
    lang,
    paid,
    free,
    online,
    offline,
    blackarch,
    output,
    output_file,
):
    """
    \b
    List all tools inventoried on rawsec, you can add category.
    Full documentation: https://rawsec-cli.readthedocs.io/
    \f
    Parameters
    ----------
    ctx: Context
        Click context
    category: str, optional
        Category name.
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
    output: str, optional
        output format.
    output_file: str, optional
        output file name, extension file will override output parameter.

    Returns
    -------
    None
        Return in output format(Default: table) in output_file(Default: stdout) a list of rawsec tools.
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

    if category and category not in get_tools_category(json=ctx.obj["json"]):
        click.echo("Category available:")
        for category in get_tools_category(json=ctx.obj["json"]):
            click.echo(f"\t{category}")
        sys.exit("Not a good category")
    if category:
        projects = get_tools_by_category(ctx.obj["json"], category)
    else:
        projects = get_all_tools(ctx.obj["json"])
    projects = [
        {k: tool[k] if k in tool else "" for k in wanted_keys}
        for tool in projects
    ]
    projects = filter_projects(
        projects,
        lang=lang,
        paid=paid,
        free=free,
        online=online,
        offline=offline,
        blackarch=blackarch,
    )
    print_output(
        projects=projects,
        output=output,
        file=output_file,
        wanted_keys=wanted_keys,
    )


@list_command.command("resources")
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
@click.option(
    "--output",
    "-o",
    help="Output format",
    type=click.Choice(
        ["json", "csv", "table"],
        case_sensitive=False,
    ),
    default="table",
)
@click.option(
    "--output-file",
    "-of",
    help="Output file name if you want. Format: json, csv, table are supported.",
    default=None,
)
def resources(ctx, category, paid, free, output, output_file):
    """
    \b
    List all resources inventoried on rawsec, you can add category.
    Full documentation: https://rawsec-cli.readthedocs.io/
    \f
    Parameters
    ----------
    ctx: Context
        Click context.
    category: str, optional
        Category name.
    paid: bool, optional
        paid or not.
    free: bool, optional
        free or not.
    output: str, optional
        output format.
    output_file: str, optional
        output file name, extension file will override output parameter.

    Returns
    -------
    None
        Return in output format(Default: table) in output_file(Default: stdout) a list of rawsec resources.
    """
    wanted_keys = ["name", "website", "source", "description", "price"]
    if category and category not in get_resources_category(
        json=ctx.obj["json"],
    ):
        click.echo("Category available:")
        for category in get_resources_category(json=ctx.obj["json"]):
            click.echo(f"\t{category}")
        sys.exit("Not a good category")
    if category:
        projects = get_resources_by_category(ctx.obj["json"], category)
    else:
        projects = get_all_resources(ctx.obj["json"])

    projects = filter_projects(projects, paid=paid, free=free)
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
    print_output(
        projects=projects,
        output=output,
        file=output_file,
        wanted_keys=wanted_keys,
    )


@list_command.command()
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
@click.option(
    "--output",
    "-o",
    help="Output format",
    type=click.Choice(
        ["json", "csv", "table"],
        case_sensitive=False,
    ),
    default="table",
)
@click.option(
    "--output-file",
    "-of",
    help="Output file name if you want. Format: json, csv, table are supported.",
    default=None,
)
def ctf(ctx, category, lang, paid, free, output, output_file):
    """
    \b
    List all ctf platforms inventoried on rawsec, you can add category.
    Full documentation: https://rawsec-cli.readthedocs.io/
    \f
    Parameters
    ----------
    ctx: Context
        Click context.
    category: str, optional
        Category name.
    lang: str, optional
        Language name
    paid: bool, optional
        paid or not.
    free: bool, optional
        free or not.
    output: str, optional
        output format.
    output_file: str, optional
        output file name, extension file will override output parameter.

    Returns
    -------
    None
        Return in output format(Default: table) in output_file(Default: stdout) a list of rawsec ctf.
    """
    wanted_keys = [
        "name",
        "website",
        "source",
        "description",
        "language",
        "price",
    ]
    if category and category not in get_ctf_category(json=ctx.obj["json"]):
        click.echo("Category available:")
        for category in get_ctf_category(json=ctx.obj["json"]):
            click.echo(f"\t{category}")
        sys.exit("Not a good category")
    if category:
        projects = get_ctf_by_category(ctx.obj["json"], category)
    else:
        projects = get_all_ctf(ctx.obj["json"])

    projects = [
        {k: tool[k] if k in tool else "" for k in wanted_keys}
        for tool in projects
    ]
    projects = filter_projects(projects, lang=lang, paid=paid, free=free)
    print_output(
        projects=projects,
        output=output,
        file=output_file,
        wanted_keys=wanted_keys,
    )


@list_command.command()
@click.pass_context
@click.argument("category", required=False)
@click.option("--base", "-b", help="Filter by base")
@click.option(
    "--output",
    "-o",
    help="Output format",
    type=click.Choice(
        ["json", "csv", "table"],
        case_sensitive=False,
    ),
    default="table",
)
@click.option(
    "--output-file",
    "-of",
    help="Output file name if you want. Format: json, csv, table are supported.",
    default=None,
)
def os(ctx, category, base, output, output_file):
    """
    \b
    List all os inventoried on rawsec, you can add category.
    Full documentation: https://rawsec-cli.readthedocs.io/
    \f
    Parameters
    ----------
    ctx: Context
        Click context.
    category: str, optional
        Category name.
    base: str, optional
        Base name(ex: Linux).
    output: str, optional
        output format.
    output_file: str, optional
        output file name, extension file will override output parameter.

    Returns
    -------
    None
        Return in output format(Default: table) in output_file(Default: stdout) a list of rawsec ctf.
    """
    wanted_keys = ["os", "base", "description", "link"]
    if category and category not in get_operating_category(
        json=ctx.obj["json"],
    ):
        click.echo("Category available:")
        for category in get_operating_category(json=ctx.obj["json"]):
            click.echo(f"\t{category}")
        sys.exit("Not a good category")
    if category:
        if category == "project_transferred":
            wanted_keys = ["from", "to"]
        projects = get_operating_by_category(ctx.obj["json"], category)
    else:
        projects = get_all_operating(ctx.obj["json"])
    projects = [
        {k: os[k] if k in os else "" for k in wanted_keys} for os in projects
    ]
    if base:
        projects = [
            os for os in projects if os["base"].lower() == base.lower()
        ]
    print_output(
        projects=projects,
        output=output,
        file=output_file,
        wanted_keys=wanted_keys,
    )
