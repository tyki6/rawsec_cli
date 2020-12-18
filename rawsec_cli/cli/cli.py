"""Main cli file"""
import click

from rawsec_cli import __commit__
from rawsec_cli import __version__
from rawsec_cli.cli.command.listCommand import listCommand
from rawsec_cli.cli.command.searchCommand import search
from rawsec_cli.cli.command.submitCommand import submit
from rawsec_cli.tools import loadInventoryJson

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.option("-V", "--version", is_flag=True)
@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.pass_context
def cli(ctx, version):
    """
    Rawsec's Cybersecurity Inventory is an inventory with 4 category(Tools, Resources, Ctf Platforms, OS).\n
    This cli can search a project,list all projects by category, you can filter your research with option --help for more information.\n
    full documentation: https://rawsec-cli.readthedocs.io/
    \f
    :param ctx: click context
    :return:
    """
    if version:
        click.echo(
            f"rawsec-cli, version: {__version__}, commit: {__commit__}\nFull documentation: https://rawsec-cli.readthedocs.io/",
        )
    ctx.ensure_object(dict)
    ctx.obj["json"] = loadInventoryJson()


cli.add_command(search)
cli.add_command(listCommand)
cli.add_command(submit)

if __name__ == "__main__":
    cli(obj={})
