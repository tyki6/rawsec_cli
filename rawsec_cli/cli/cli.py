import click
from command.listCommand import listCommand
from tools import loadInventoryJson
from command.searchCommand import search


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj["json"] = loadInventoryJson()


cli.add_command(search)
cli.add_command(listCommand)

if __name__ == "__main__":
    cli(obj={})
