import click
from rawsec_cli.cli.command.listCommand import listCommand
from rawsec_cli.tools import loadInventoryJson
from rawsec_cli.cli.command.searchCommand import search


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj["json"] = loadInventoryJson()


cli.add_command(search)
cli.add_command(listCommand)

if __name__ == "__main__":
    cli(obj={})
