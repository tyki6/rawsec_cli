"""Search command cli file"""
import click

from rawsec_cli.filter import filter_projects
from rawsec_cli.output import print_output
from rawsec_cli.search import search_project


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
def search(
    ctx,
    project,
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
    Search a project inventoried on rawsec.
    Search in name and description.
    Full documentation: https://rawsec-cli.readthedocs.io/
    \f
    Parameters
    ----------
    ctx: Context
        Click context
    project: str, optional
        Keyword.
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
        Return in output format(Default: table) in output_file(Default: stdout) a list of rawsec project within description or name project keyword.
    """
    projects = search_project(ctx.obj["json"], project)
    projects = filter_projects(
        projects,
        lang,
        paid,
        free,
        online,
        offline,
        blackarch,
    )
    wanted_keys = list()
    for project in projects:
        wanted_keys += project.keys()
    print_output(
        projects=projects,
        output=output,
        file=output_file,
        wanted_keys=list(dict.fromkeys(wanted_keys)),
    )
