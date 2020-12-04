import click
from tools import loadInventoryJson, searchProject


@click.group()
@click.option("--filter")
@click.pass_context
def cli(ctx, filter):
    click.echo("test")
    ctx.ensure_object(dict)
    ctx.obj['json'] = loadInventoryJson()


@cli.group()
def list():
    click.echo("list")


@cli.command('search')
def test():
    click.echo("test")


@cli.command('search')
@click.argument('project')
@click.pass_context
@click.option("--lang", "-l", help="Filter by Language")
@click.option("--price", "-p", help="Filter by Price=True")
@click.option("--free", "-f", help="Filter by Price: Free")
@click.option("--online", "-on", help="Filter by Online: True")
@click.option("--offline", "-off", help="Filter by Online: False")
def search(ctx, project, lang, price, free, online, offline):
    click.echo("search")
    print(searchProject(ctx.obj["json"], project))


@cli.group()
def submit():
    click.echo("submit")


@list.command("tools")
def tools(ctx):
    click.echo('tools')
    click.echo(ctx.obj)


@list.command()
def ressources():
    click.echo('resources called')


@list.command()
def ctf():
    click.echo('ctf_platforms')


@list.command()
def os():
    click.echo('operating_systems')


if __name__ == '__main__':
    cli(obj={})
