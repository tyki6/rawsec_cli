"""Main cli file"""
import sys

import click

from rawsec_cli import __commit__
from rawsec_cli import __version__
from rawsec_cli.cli.command.list_command import list_command
from rawsec_cli.cli.command.search_command import search
from rawsec_cli.tools import load_inventory_json

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.option("-V", "--version", is_flag=True)
@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.pass_context
def cli(ctx, version):
    """
    \b
    Rawsec's Cybersecurity Inventory is an inventory with 4 category(Tools, Resources, Ctf Platforms, OS).
    This cli can search a project,list all projects by category, you can filter your research with option --help for more information.
    Full documentation: https://rawsec-cli.readthedocs.io/
    \f

    Parameters
    ----------
    ctx: click Context
        click Context.
    version: bool
        version flag.

    Returns
    -------
    None
        return version + commit version you use.
    """
    if version:
        click.echo(
            f"rawsec-cli, version: {__version__}, commit: {__commit__}\nFull documentation: https://rawsec-cli.readthedocs.io/",
        )
        sys.exit()
    ctx.ensure_object(dict)
    ctx.obj["json"] = load_inventory_json()


cli.add_command(search)
cli.add_command(list_command)

if __name__ == "__main__":
    cli(obj={})
