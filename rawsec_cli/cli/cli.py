import click
from tools import loadInventoryJson
from command.searchCommand import search


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj['json'] = loadInventoryJson()


cli.add_command(search)


@cli.group("list")
def listCommand():
    click.echo("list")


@cli.group()
def submit():
    click.echo("submit")


@listCommand.command("tools")
def tools(ctx):
    click.echo('tools')
    click.echo(ctx.obj)


@listCommand.command()
def ressources():
    click.echo('resources called')


@listCommand.command()
def ctf():
    click.echo('ctf_platforms')


@listCommand.command()
def os():
    click.echo('operating_systems')


if __name__ == '__main__':
    cli(obj={})
