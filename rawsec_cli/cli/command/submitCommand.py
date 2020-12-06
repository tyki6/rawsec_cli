import click


@click.group()
def submit():
    type = click.prompt('Please enter a type', type=str)
    category = click.prompt('Please enter a Category', type=str)
